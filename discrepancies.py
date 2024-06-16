
To match the OCR-derived data (extracted from the screenshot using OCR) with the Selenium-scraped data (extracted directly from the mobile application using Selenium) and identify any price discrepancies

Steps to Match and Identify Price Discrepancies
1. Retrieve Selenium-Scraped Data
First, To modify the existing Selenium script to scrape product names and prices from the mobile application.


from appium import webdriver
import time

# Set up desired capabilities for Appium
desired_caps = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "appPackage": "com.example.yourapp",
    "appActivity": "com.example.yourapp.MainActivity",
    "automationName": "UiAutomator2"
}

# Initialize the driver
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

try:
    # Wait for the app to load
    time.sleep(5)
    
    # Scrape product names and prices using Selenium
    products = driver.find_elements_by_xpath("//android.widget.ListView/android.view.ViewGroup")
    
    scraped_data = []
    for product in products:
        name = product.find_element_by_id("com.example.yourapp:id/product_name").text
        price = product.find_element_by_id("com.example.yourapp:id/product_price").text
        scraped_data.append({"name": name, "price": price})

finally:
    # Quit the driver
    driver.quit()
2. Extract OCR-Derived Data
Next, integrate the OCR code snippet from the previous response to extract text (which includes product names and prices) from the screenshot captured using OCR:


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
ocr_text = pytesseract.image_to_string(thresh)

# Print extracted text
print("OCR Extracted Text:")
print(ocr_text)
3. Match and Compare Data
Once you have both sets of data (Selenium-scraped and OCR-derived), you can compare the prices to identify any discrepancies. Here’s how you can proceed with matching and comparing:


# Assuming 'scraped_data' is a list of dictionaries with keys 'name' and 'price'
# Example data structure of 'scraped_data':
# scraped_data = [{"name": "Product A", "price": "100.00"}, {"name": "Product B", "price": "50.00"}, ...]

# Split OCR text into lines to process each line
ocr_lines = ocr_text.splitlines()

# Initialize lists to store matched and unmatched data
matched_data = []
unmatched_data = []

# Compare OCR-derived data with Selenium-scraped data
for scraped_item in scraped_data:
    scraped_name = scraped_item['name']
    scraped_price = scraped_item['price']
    
    found = False
    
    # Search for scraped_name in OCR-derived text lines
    for line in ocr_lines:
        if scraped_name in line:
            # Extract price from OCR line (assuming it follows the format near the name)
            # Implement your logic to extract price from the OCR line based on your OCR text format
            # Here's a hypothetical example assuming the price follows the name directly
            ocr_price = line.split(scraped_name)[-1].strip()
            
            # Compare prices
            if scraped_price == ocr_price:
                matched_data.append({"name": scraped_name, "scraped_price": scraped_price, "ocr_price": ocr_price})
            else:
                unmatched_data.append({"name": scraped_name, "scraped_price": scraped_price, "ocr_price": ocr_price})
            
            found = True
            break
    
    # If scraped_name is not found in OCR text
    if not found:
        unmatched_data.append({"name": scraped_name, "scraped_price": scraped_price, "ocr_price": "Not found"})

# Print results
print("Matched Data:")
for item in matched_data:
    print(item)

print("\nUnmatched Data:")
for item in unmatched_data:
    print(item)

Explanation:
OCR Processing: The OCR text extracted from the screenshot is split into lines (ocr_lines). 
Comparison Logic: For each product scraped using Selenium (scraped_data), search for its name in ocr_lines. If found, extract the price and compare it with the scraped price.
Data Structures: matched_data and unmatched_data lists are used to store products with matched and unmatched prices respectively.
Output: Print out matched and unmatched data to identify any discrepancies between Selenium-scraped prices and OCR-derived prices.
