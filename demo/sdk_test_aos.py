'''
sdk test
'''
import os
import time
import unittest

from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from demo.util.matchers import ImageMatcher
from demo.util.time_series import TimeSeries


class DevPlayAndroidTest(unittest.TestCase):
    capture_dir = os.path.join(os.path.dirname(__file__), '/capture')

    def setImgDirPath(self):
        img_dir = '%s/img/' % os.getcwd()
        self.cap_dir = img_dir + 'device_img/'
        self.temp_dir = img_dir + 'search_img/aos/'

    def setUp(self):
        self.setImgDirPath()

        # set path
        app = os.path.join(os.path.dirname(__file__), '../app', 'sdk_test.apk')
        app = os.path.abspath(app)

        #set up util
        self.matcher = ImageMatcher()
        self.ts = TimeSeries()

        # set up appium
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                'app': app,
                'platformName': 'Android',
                'platformVersion': '10',
                'deviceName': '9c3be731',
                'automationName': 'Appium',
                'appPackage': 'com.devsisters.test.whatever',
                'appActivity': 'com.devsisters.plugin.OvenUnityPlayerActivity',
            })

    def testSDKLogin(self):
        # 최고 20초 대기
        driver = self.driver
        wait = WebDriverWait(driver, timeout=30)

        # write the selenium by the test scenario
        try:
            self.findAppStartButton(driver)
            self.findProjectSampleButton()

        except Exception as e:
            print(e)

    def findAppStartButton(self, driver):
        print("task one")

        print("swipes")
        # 아래에서 위로 변하는 좌표를 줘야 swipe가 발생함
        driver.swipe(500, 900, 100, 100)

        screenshot = '%s-screenshot.png' % self.ts.makeTimeSeriesName()

        print(self.cap_dir + screenshot)
        driver.save_screenshot(self.cap_dir+screenshot)

        center = self.matcher.detectImage(self.cap_dir + screenshot, self.temp_dir + '1.jpg')
        print(center)

        self.driver.tap([center])
        print("tap")
        time.sleep(3)

    def findProjectSampleButton(self):
        print("task two")

        screenshot = '%s-screenshot.png' % self.ts.makeTimeSeriesName()
        self.driver.save_screenshot(self.cap_dir + screenshot)

        center = self.matcher.detectImage(self.cap_dir + screenshot, self.temp_dir + "2.jpg")

        print("task two center", center)

        self.driver.tap([center])
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(DevPlayAndroidTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
