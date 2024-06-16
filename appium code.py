import unittest
from appium import webdriver

class TestProductListDisplay(unittest.TestCase):
    def setUp(self):
        self.desired_caps = {
            "platformName": "Android",
            "deviceName": "emulator-5554",
            "appPackage": "com.example.yourapp",
            "appActivity": "com.example.yourapp.MainActivity",
            "automationName": "UiAutomator2"
        }
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", self.desired_caps)

    def test_product_list_display(self):
        product_list = self.driver.find_elements_by_xpath("//android.widget.ListView/android.view.ViewGroup")
        self.assertGreater(len(product_list), 0, "Product list is not displayed")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
