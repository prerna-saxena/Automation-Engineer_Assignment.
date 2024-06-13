from appium import webdriver as appium_webdriver
from PIL import Image
import time

def capture_mobile_screenshot():
    # Desired capabilities for the Appium server
    desired_caps = {
        "platformName": "Android",
        "deviceName": "emulator-5554",  # Change this to your device name
        "appPackage": "com.example.app",  # Change to your app's package
        "appActivity": "com.example.app.MainActivity"  # Change to your app's main activity
    }

    # Connect to Appium server
    driver = appium_webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    # Wait for the app to load
    time.sleep(5)

    # Capture screenshot of the product list
    screenshot_path = 'product_list.png'
    driver.save_screenshot(screenshot_path)

    # Close the driver
    driver.quit()

    print("Screenshot captured and saved.")
    return screenshot_path

# Uncomment to capture screenshot
# screenshot_path = capture_mobile_screenshot()
3. Text Extraction with OCR
Here's the Python script to extract text from the screenshot and compare it with web-scraped data:

python
Copy code
import pytesseract

def extract_text_from_image(image_path):
    # Load the screenshot
    img = Image.open(image_path)

    # Perform OCR on the image
    text = pytesseract.image_to_string(img, lang='eng')

    print("Extracted Text:")
    print(text)
    return text

def parse_ocr_text(ocr_text):
    # Assuming OCR text format is consistent and parsing it to extract product names and prices
    lines = ocr_text.split('\n')
    products = []
    for line in lines:
        parts = line.split()
        if len(parts) > 1:
            price = parts[-1]
            name = ' '.join(parts[:-1])
            products.append({'name': name, 'price': price})
    return products

def compare_data(web_data, ocr_data):
    matches = []
    discrepancies = []
    ocr_dict = {item['name']: item['price'] for item in ocr_data}

    for item in web_data:
        web_name = item['name']
        web_price = item['price']
        ocr_price = ocr_dict.get(web_name)
        
        if ocr_price:
            if web_price == ocr_price:
                matches.append({
                    'name': web_name,
                    'price': web_price
                })
            else:
                discrepancies.append({
                    'name': web_name,
                    'web_price': web_price,
                    'ocr_price': ocr_price
                })
    
    return matches, discrepancies

def generate_report(matches, discrepancies):
    report_path = 'price_comparison_report.csv'
    with open(report_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Category', 'Name', 'Web Price', 'OCR Price'])
        
        writer.writerow(['Matches'])
        for match in matches:
            writer.writerow(['Match', match['name'], match['price'], match['price']])
        
        writer.writerow(['Discrepancies'])
        for discrepancy in discrepancies:
            writer.writerow(['Discrepancy', discrepancy['name'], discrepancy['web_price'], discrepancy['ocr_price']])
    
    print(f"Report generated at {report_path}")

# Uncomment to run the full workflow
# web_data = scrape_web_data()
# screenshot_path = capture_mobile_screenshot()
# ocr_text = extract_text_from_image(screenshot_path)
# ocr_data = parse_ocr_text(ocr_text)
# matches, discrepancies = compare_data(web_data, ocr_data)
# generate_report(matches, discrepancies)
