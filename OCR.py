import pytesseract

# Load the screenshot
img = Image.open(screenshot_path)

# Perform OCR on the image
text = pytesseract.image_to_string(img, lang='eng')

# Print the extracted text
print("Extracted Text:")
print(text)
