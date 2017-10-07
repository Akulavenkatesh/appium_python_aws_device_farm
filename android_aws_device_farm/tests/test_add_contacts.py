import unittest
from time import sleep
from appium import webdriver
import desired_capabilities


class TestAddContacts(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        desired_caps = desired_capabilities.get_desired_capabilities()
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def test_add_contacts(self):
        el = self.driver.find_element_by_accessibility_id("Add Contact")
        el.click()
        textfields = self.driver.find_elements_by_class_name("android.widget.EditText")
        textfields[0].send_keys("Appium User")
        textfields[2].send_keys("someone@appium.io")
        self.assertEqual('Appium User', textfields[0].text)
        self.assertEqual('someone@appium.io', textfields[2].text)
        self.driver.find_element_by_accessibility_id("Save").click()
        try:
            self.driver.find_element_by_id('android:id/button1').click()
        except:
            pass
        self.driver.find_element_by_android_uiautomator('new UiSelector().clickable(true)').click()
        self.driver.press_keycode(3)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
