import unittest
from appium import webdriver

class TestAppLaunch(unittest.TestCase):
    def setUp(self):
        self.desired_caps = {
            "platformName": "Android",
            "deviceName": "emulator-5554",
            "appPackage": "com.example.yourapp",
            "appActivity": "com.example.yourapp.MainActivity",
            "automationName": "UiAutomator2"
        }
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", self.desired_caps)

    def test_app_launch(self):
        self.assertIsNotNone(self.driver.current_activity)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
