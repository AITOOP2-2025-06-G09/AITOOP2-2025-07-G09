## ロジック
from models.image_processor import ImageProcessor
import cv2

class MainController:
    def __init__(self, ui):
        self.ui = ui
        self.processor = ImageProcessor()
        self.capture_img = None

        ui.btn_capture.clicked.connect(self.capture)
        ui.btn_process.clicked.connect(self.process)

    def capture(self):
        from my_module.K24117.lecture05_camera_image_capture import MyVideoCapture
        cap = MyVideoCapture()
        cap.run()
        self.capture_img = cap.get_img()
        self.ui.show_image(self.capture_img)

    def process(self):
        if self.capture_img is None:
            return
        
        result = self.processor.replace_white(
            "images/google.png",
            self.capture_img
        )
        self.ui.show_image(result)
        cv2.imwrite("my_module/K24117/output_images/lecture05_01_output.png", result)
