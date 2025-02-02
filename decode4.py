from pyzbar.pyzbar import decode
import cv2
import numpy as np

# Read the image
image = cv2.imread("image04.png")

# Decode the barcode
barcodes = decode(image)
for barcode in barcodes:
    data = barcode.data.decode("utf-8")
    print(f"Barcode Data: {data}")
   
   
    points = barcode.polygon
    points = [(point.x, point.y) for point in points]
    cv2.polylines(image, [np.array(points, dtype=np.int32)], True, (0, 255, 0), 2)

    # Annotate the decoded data beside the bounding box
    x, y = points[0]  # Take the first point of the bounding box
    cv2.putText(image, data, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)  # Green text

# Display the image with the barcode highlighted and annotated
cv2.imshow("Barcode with Annotation", image)

# Wait for a key press
key = cv2.waitKey(0)

# Save the annotated image when a key is pressed
output_file = "decoded_barcode.png"
cv2.imwrite(output_file, image)
print(f"Annotated image saved as {output_file}")

cv2.destroyAllWindows()