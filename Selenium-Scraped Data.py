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
