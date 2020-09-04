import cv2


class ImageMatcher():
    def detectImage(self, screenPath, detectPath):
        source_img = cv2.imread(screenPath, 0)
        template = cv2.imread(detectPath, 0)

        print("source_img", source_img)
        w, h = template.shape[::-1]

        method = eval('cv2.TM_CCOEFF')
        res = cv2.matchTemplate(source_img, template, method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        center = (top_left[0] + int(w / 2), top_left[1] + int(h / 4))

        color = (255, 250, 0)
        cv2.rectangle(source_img, top_left, bottom_right, color, thickness=8)

        detectshotPath = screenPath[:-4] + '-detect.png'
        cv2.imwrite(detectshotPath, source_img)

        return center
