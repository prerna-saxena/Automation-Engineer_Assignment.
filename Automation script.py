from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from appium import webdriver as appium_webdriver
from PIL import Image
import pytesseract
import json
import csv
import time

# Web Automation using Selenium
def scrape_web_data():
    # Setup WebDriver (adjust the path to the location of your WebDriver)
    driver = webdriver.Chrome(executable_path='/path/to/chromedriver')

    # Access the e-commerce site
    driver.get('https://www.example.com')  # Replace with the actual URL

    # Search for "Hindi Books"
    search_box = driver.find_element(By.NAME, 'search')  # Adjust the search box locator
    search_box.send_keys('Hindi Books')
    search_box.send_keys(Keys.RETURN)

    time.sleep(3)  # Wait for the page to load

    # Scrape book details
    books = driver.find_elements(By.CSS_SELECTOR, 'div.book-item')  # Adjust the selector

    book_data = []

    for book in books:
        name = book.find_element(By.CSS_SELECTOR, 'h2.book-title').text  # Adjust the selector
        price = book.find_element(By.CSS_SELECTOR, 'span.book-price').text  # Adjust the selector
        rating = book.find_element(By.CSS_SELECTOR, 'div.book-rating').text  # Adjust the selector

        book_data.append({
            'name': name,
            'price': price,
            'rating': rating
        })

    # Save data to JSON
    with open('books.json', 'w', encoding='utf-8') as f:
        json.dump(book_data, f, ensure_ascii=False, indent=4)

    # Save data to CSV
    with open('books.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['name', 'price', 'rating'])
        writer.writeheader()
        writer.writerows(book_data)

    # Close the browser
    driver.quit()

    print("Web scraping completed and data saved.")

# Mobile Automation using Appium
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

# OCR Processing using Tesseract
def extract_text_from_image(image_path):
    # Load the screenshot
    img = Image.open(image_path)

    # Perform OCR on the image
    text = pytesseract.image_to_string(img, lang='eng')

    print("Extracted Text:")
    print(text)
    return text

# Main function to run all tasks
def main():
    scrape_web_data()
    screenshot_path = capture_mobile_screenshot()
    extracted_text = extract_text_from_image(screenshot_path)

    # Further processing and comparison can be done here
    # ...

if __name__ == "__main__":
    main()
