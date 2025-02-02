import cv2
import numpy as np
import zxing
from pyzbar.pyzbar import decode

# Initialize the ZXing reader
reader = zxing.BarCodeReader()

# Load the Aztec code image
image_path = "image05.png"  # Replace with your image path
image = cv2.imread(image_path)

# Decode the Aztec code using ZXing
decoded = reader.decode(image_path)

# Check if the Aztec code was successfully decoded
if decoded:
    print(f"Decoded Data: {decoded.parsed}")
    print(f"Barcode Format: {decoded.format}")

    # Draw the bounding box around the Aztec code (if points are available)
    if decoded.points and isinstance(decoded.points, list):
        try:
            points = [tuple(map(int, p)) for p in decoded.points]
            cv2.polylines(image, [np.array(points, dtype=np.int32)], True, (0, 255, 0), 2)

            # Annotate the decoded data beside the bounding box
            x, y = points[0]  # Take the first point of the bounding box
            cv2.putText(image, decoded.parsed, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        except Exception as e:
            print(f"Error processing bounding box points: {e}")

    # Display the image with the Aztec code highlighted and annotated
    cv2.imshow("Aztec Code with Annotation", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Save the annotated image
    output_file = "decoded_aztec.png"
    cv2.imwrite(output_file, image)
    print(f"Annotated image saved as {output_file}")

else:
    print("Failed to decode the Aztec code with ZXing. Trying pyzbar...")

    # Try decoding with pyzbar
    decoded_objects = decode(image)
    
    if decoded_objects:
        for obj in decoded_objects:
            print(f"Decoded Data: {obj.data.decode('utf-8')}")
            print(f"Barcode Format: {obj.type}")

            # Get bounding box
            points = obj.polygon
            if points:
                points = [(p.x, p.y) for p in points]
                cv2.polylines(image, [np.array(points, dtype=np.int32)], True, (0, 255, 0), 2)

        # Display the image with bounding box
        cv2.imshow("Decoded Image", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        # Save the result
        output_file = "decoded_aztec_pyzbar.png"
        cv2.imwrite(output_file, image)
        print(f"Annotated image saved as {output_file}")
    else:
        print("Failed to decode the Aztec code with pyzbar as well.")