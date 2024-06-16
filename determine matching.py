determine matching

import cv2
import pytesseract
import os
from appium import webdriver
import time

# Path to Tesseract executable (if not in your PATH environment variable)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Path to your captured screenshot
screenshot_path = 'product_list_screenshot.png'

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
    
    # Load the screenshot using OpenCV
    img = cv2.imread(screenshot_path)
    
    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Apply thresholding to preprocess the image
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
    
    # Use pytesseract to extract text from image
    ocr_text = pytesseract.image_to_string(thresh)
    
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
        
        # Search for scraped_name in OCR text lines
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
    
    # Generate and print report
    print("\nMatching Prices:")
    for item in matched_data:
        print(f"Name: {item['name']}, Scraped Price: {item['scraped_price']}, OCR Price: {item['ocr_price']}")
    
    print("\nMismatching Prices:")
    for item in unmatched_data:
        print(f"Name: {item['name']}, Scraped Price: {item['scraped_price']}, OCR Price: {item['ocr_price']}")
    
    # Optionally, write report to a file
    report_filename = 'price_comparison_report.txt'
    with open(report_filename, 'w') as report_file:
        report_file.write("Matching Prices:\n")
        for item in matched_data:
            report_file.write(f"Name: {item['name']}, Scraped Price: {item['scraped_price']}, OCR Price: {item['ocr_price']}\n")
        
        report_file.write("\nMismatching Prices:\n")
        for item in unmatched_data:
            report_file.write(f"Name: {item['name']}, Scraped Price: {item['scraped_price']}, OCR Price: {item['ocr_price']}\n")
    
    print(f"\nReport generated: {os.path.abspath(report_filename)}")

finally:
    # Quit the driver
    driver.quit()
