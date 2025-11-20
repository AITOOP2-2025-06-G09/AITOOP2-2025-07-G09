## UI
import cv2
from PySide6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                               QPushButton, QLabel, QMessageBox)
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self, model):
        super().__init__()
        self.model = model
        self.setWindowTitle("画像合成アプリ")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        # 画像表示エリア
        self.image_label = QLabel("操作ボタンを押してください")
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image_label.setStyleSheet("border: 2px dashed gray; background-color: #eee;")
        self.image_label.setMinimumSize(640, 480)
        self.layout.addWidget(self.image_label)

        # ボタンエリア
        btn_layout = QHBoxLayout()
        
        self.btn_load = QPushButton("1. 画像読込")
        self.btn_load.clicked.connect(self.on_load)
        btn_layout.addWidget(self.btn_load)

        self.btn_cam = QPushButton("2. カメラ撮影")
        self.btn_cam.clicked.connect(self.on_camera)
        btn_layout.addWidget(self.btn_cam)

        self.btn_proc = QPushButton("3. 合成実行")
        self.btn_proc.clicked.connect(self.on_process)
        btn_layout.addWidget(self.btn_proc)

        self.btn_save = QPushButton("4. 保存")
        self.btn_save.clicked.connect(self.on_save)
        btn_layout.addWidget(self.btn_save)

        self.layout.addLayout(btn_layout)

    def display_image(self, cv_img):
        """OpenCV画像をPySideで表示"""
        if cv_img is None: return
        rgb_img = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_img.shape
        bytes_per_line = ch * w
        qt_img = QImage(rgb_img.data, w, h, bytes_per_line, QImage.Format.Format_RGB888)
        self.image_label.setPixmap(QPixmap.fromImage(qt_img).scaled(
            self.image_label.size(), Qt.AspectRatioMode.KeepAspectRatio))

    def on_load(self):
        img = self.model.load_base_image()
        if img is not None:
            self.display_image(img)
            QMessageBox.information(self, "成功", "画像を読み込みました")
        else:
            QMessageBox.warning(self, "エラー", "google.png が見つかりません")

    def on_camera(self):
        QMessageBox.information(self, "案内", "OKを押すとカメラが起動します。\n'q'キーで撮影してください。")
        img = self.model.start_camera_capture()
        if img is not None: self.display_image(img)

    def on_process(self):
        img = self.model.process_synthesis()
        if img is not None: 
            self.display_image(img)
            QMessageBox.information(self, "成功", "合成しました！")
        else:
            QMessageBox.warning(self, "エラー", "画像が足りません")

    def on_save(self):
        path = self.model.save_result()
        if path: QMessageBox.information(self, "保存", f"保存しました: {path}")