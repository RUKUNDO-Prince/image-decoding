from pylibdmtx.pylibdmtx import decode
import cv2


image = cv2.imread("image02.jpg", cv2.IMREAD_GRAYSCALE) 


decoded_objects = decode(image, timeout=500)

for obj in decoded_objects:
    data = obj.data.decode("utf-8")
    print("Decoded Data:", data)


output_file = "decoded_datamatrix_code.png"
cv2.imwrite(output_file, image)
print(f" Annotated image saved as {output_file}")

cv2.imshow("Barcode with Annotation", image)
cv2.waitKey(0)
cv2.destroyAllWindows()