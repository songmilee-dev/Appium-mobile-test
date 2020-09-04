import os

import cv2

from demo.util.time_series import TimeSeries


class ImageMatcher:
    # setup
    def __init__(self, driver):
        self.driver = driver
        self.ts = TimeSeries()
        img_dir = '%s/img/' % os.getcwd()
        self.cap_dir = img_dir + 'device_img/'
        self.temp_dir = img_dir + 'search_img/aos/'

    def findTemplateFromScreenshot(self, template_name):
        screenshot = '%s-screenshot.png' % self.ts.makeTimeSeriesName()
        self.driver.save_screenshot(self.cap_dir + screenshot)

        center = self.detectImage(self.cap_dir + screenshot, self.temp_dir + template_name)

        return center

    def detectImage(self, screenPath, detectPath):
        print(screenPath, detectPath)
        source_img = cv2.imread(screenPath)
        source_img_gray = cv2.cvtColor(source_img, cv2.COLOR_BGR2GRAY)

        template = cv2.imread(detectPath, 0)

        w, h = template.shape[::-1]

        method = eval('cv2.TM_CCOEFF')
        res = cv2.matchTemplate(source_img_gray, template, method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        center = (top_left[0] + int(w / 2), top_left[1] + int(h / 4))

        color = (255, 160, 122)
        cv2.rectangle(source_img, top_left, bottom_right, color, thickness=8)

        detectshotPath = screenPath[:-4] + '-detect.png'
        cv2.imwrite(detectshotPath, source_img)

        return center
