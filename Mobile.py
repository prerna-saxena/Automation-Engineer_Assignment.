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
