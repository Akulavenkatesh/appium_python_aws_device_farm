import unittest
from time import sleep
from random import randint
from appium import webdriver
import desired_capabilities


class TestSampleApp(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        desired_caps = desired_capabilities.get_desired_capabilities()
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def _populate(self):
        els = [self.driver.find_element_by_accessibility_id('TextField1'),
               self.driver.find_element_by_accessibility_id('TextField2')]

        self._sum = 0
        for i in range(2):
            rnd = randint(0, 10)
            els[i].send_keys(rnd)
            self._sum += rnd

    def test_ui_computation(self):
        sleep(5)
        try:
            self.driver.switch_to.alert.accept()
            sleep(3)
        except:
            pass
        self._populate()
        self.driver.find_element_by_accessibility_id('ComputeSumButton').click()
        sum = self.driver.find_element_by_accessibility_id('Answer').text
        self.assertEqual(int(sum), self._sum)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()