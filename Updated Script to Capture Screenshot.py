import unittest
import os
from appium import webdriver

class TestCaptureScreenshot(unittest.TestCase):
    def setUp(self):
        self.desired_caps = {
            "platformName": "Android",
            "deviceName": "emulator-5554",
            "appPackage": "com.example.yourapp",
            "appActivity": "com.example.yourapp.MainActivity",
            "automationName": "UiAutomator2"
        }
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", self.desired_caps)

    def test_capture_screenshot(self):
        # Wait for the app to load
        self.driver.implicitly_wait(10)

        # Capture screenshot
        screenshot_dir = os.path.abspath(os.path.dirname(__file__))
        screenshot_file = os.path.join(screenshot_dir, "product_list_screenshot.png")
        self.driver.save_screenshot(screenshot_file)
        print(f"Screenshot saved as: {screenshot_file}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
