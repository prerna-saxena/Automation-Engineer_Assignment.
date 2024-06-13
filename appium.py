from appium import webdriver
from selenium.webdriver.common.by import By
from PIL import Image
import time

# Desired capabilities for the Appium server
desired_caps = {
    "platformName": "Android",
    "deviceName": "emulator-5554",  # Change this to your device name
    "appPackage": "com.example.app",  # Change to your app's package
    "appActivity": "com.example.app.MainActivity"  # Change to your app's main activity
}

# Connect to Appium server
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# Wait for the app to load
time.sleep(5)

# Capture screenshot of the product list
screenshot_path = 'product_list.png'
driver.save_screenshot(screenshot_path)

# Verify the screenshot is saved
img = Image.open(screenshot_path)
img.show()

# Close the driver
driver.quit()

print("Screenshot captured and saved.")
