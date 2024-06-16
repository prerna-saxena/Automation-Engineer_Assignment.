import cv2
import pytesseract

# Path to Tesseract executable (if not in your PATH environment variable)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Path to your captured screenshot
screenshot_path = 'product_list_screenshot.png'

# Load the screenshot using OpenCV
img = cv2.imread(screenshot_path)

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply thresholding to preprocess the image
_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

# Use pytesseract to extract text from image
text = pytesseract.image_to_string(thresh)

# Print extracted text
print("Extracted Text:")
print(text)
