## 画像処理
import cv2

class ImageProcessor:

    def replace_white(self, google_img_path, capture_img):
        google_img = cv2.imread(google_img_path)

        g_h, g_w, _ = google_img.shape
        c_h, c_w, _ = capture_img.shape

        for x in range(g_w):
            for y in range(g_h):
                b, g, r = google_img[y, x]
                if (b, g, r) == (255, 255, 255):
                    google_img[y, x] = capture_img[y % c_h, x % c_w]

        return google_img
