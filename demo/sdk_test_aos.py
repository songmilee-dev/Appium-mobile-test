'''
sdk test
'''
import os
import time
import unittest

from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from demo.util.matchers import ImageMatcher


class DevPlayAndroidTest(unittest.TestCase):
    def setUp(self):
        # set path
        app = os.path.join(os.path.dirname(__file__), '../app', 'sdk_test.apk')
        app = os.path.abspath(app)

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

        self.matcher = ImageMatcher(self.driver)

    def testSDKLogin(self):
        # 최고 20초 대기
        driver = self.driver
        wait = WebDriverWait(driver, timeout=30)
        time.sleep(5)

        # write the selenium by the test scenario
        try:
            self.findAppStartButton()
            self.findProjectSampleButton()
            self.tapAgeTestButtonAndConfirm()
            self.confirmAgeTest()
            self.tapPrivacyPolicy()
            self.tapPermissionNoti()
            self.tapPermission()
            self.tapGuestLogin()
            self.findMid()
        except Exception as e:
            print(e)

    def findAppStartButton(self):
        print("task one")

        print("swipes")
        # 아래에서 위로 변하는 좌표를 줘야 swipe 발생함
        self.driver.swipe(800, 900, 500, 100)
        time.sleep(2)

        center = self.matcher.findTemplateFromScreenshot('1.jpg')
        print(center)

        self.driver.tap([center])
        print("tap")
        time.sleep(3)

    def findProjectSampleButton(self):
        print("task two")

        center = self.matcher.findTemplateFromScreenshot("2.jpg")

        print("task two center", center)

        self.driver.tap([center])
        time.sleep(3)

    def tapAgeTestButtonAndConfirm(self):
        print("tap Age Test Button and Confirm")
        self.tapAgeTest()

    def tapAgeTest(self):
        print("Age test")

        center = self.matcher.findTemplateFromScreenshot("3.png")
        print(center)
        self.driver.tap([center])

        time.sleep(3)

    def confirmAgeTest(self):
        print("Confirm Age Test")

        center = self.matcher.findTemplateFromScreenshot("4.jpg")
        print(center)
        self.driver.tap([center])

        time.sleep(3)

    def tapPrivacyPolicy(self):
        print("Privacy Policy")

        center = self.matcher.findTemplateFromScreenshot("5.jpg")
        print(center)
        self.driver.tap([center])

        time.sleep(3)

    def tapPermissionNoti(self):
        print("Permission Noti")
        time.sleep(5)

        center = self.matcher.findTemplateFromScreenshot("6.png")
        print(center)

        new_center = (center[0], center[1] + 100)
        self.driver.tap([new_center])
        time.sleep(3)

    def tapPermission(self):
        print("Tap Permission")

        center = self.matcher.findTemplateFromScreenshot("7.png")
        self.driver.tap([center])
        time.sleep(3)

    def tapGuestLogin(self):
        print("Guest login")

        center = self.matcher.findTemplateFromScreenshot("8.jpg")
        self.driver.tap([center])
        time.sleep(3)

    def findMid(self):
        print("Find Mid")

        try:
            center = self.matcher.findTemplateFromScreenshot("9.jpg")
            print(center)
            time.sleep(5)
        except Exception as e:
            print("Cannot Find Mid", e)


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(DevPlayAndroidTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
