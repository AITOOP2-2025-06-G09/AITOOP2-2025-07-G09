## UI
from PySide6.QtWidgets import QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("白色置換アプリ")

        self.label = QLabel("画像がここに表示されます")
        self.label.setAlignment(Qt.AlignCenter)

        self.btn_capture = QPushButton("カメラキャプチャ")
        self.btn_process = QPushButton("白色置換開始")

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.btn_capture)
        layout.addWidget(self.btn_process)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def show_image(self, cv_img):
        from PySide6.QtGui import QImage, QPixmap
        
        h, w, ch = cv_img.shape
        bytes_per_line = ch * w
        qimg = QImage(cv_img.data, w, h, bytes_per_line, QImage.Format_BGR888)
        self.label.setPixmap(QPixmap.fromImage(qimg))
