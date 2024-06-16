import unittest
from appium import webdriver

class TestProductDetails(unittest.TestCase):
    def setUp(self):
        self.desired_caps = {
            "platformName": "Android",
            "deviceName": "emulator-5554",
            "appPackage": "com.example.yourapp",
            "appActivity": "com.example.yourapp.MainActivity",
            "automationName": "UiAutomator2"
        }
        self.driver = webdriver
