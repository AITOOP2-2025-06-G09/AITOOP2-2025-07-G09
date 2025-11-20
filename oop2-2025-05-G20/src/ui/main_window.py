from PySide6.QtWidgets import (
    QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QImage, QPixmap, QFont


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("💗 プリクラ風画像アプリ 💗")
        self.resize(900, 700)

        # ---------------------------
        #  フォント設定（丸っこい感じ）
        # ---------------------------
        font = QFont("Rounded Mplus 1c", 12)
        self.setFont(font)

        # ---------------------------
        #  全体のプリクラ風テーマ CSS
        # ---------------------------
        self.setStyleSheet("""
            QWidget {
                background-color: #ffeefe;  /* ピンク系グラデ */
                font-family: 'Rounded Mplus 1c';
            }

            QPushButton {
                background-color: #ffb7dd;
                border: 3px solid #ff8ac1;
                border-radius: 25px;
                padding: 12px 25px;
                font-size: 20px;
                color: #ffffff;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #ff9ccf;
            }

            QLabel {
                color: #d63384;
                font-size: 22px;
                font-weight: bold;
            }
        """)

        # ---------------------------
        #  画像表示エリア（中央）
        # ---------------------------
        self.image_label = QLabel("📸 ここに撮影画像が表示されます 💖")
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setFixedSize(700, 500)
        self.image_label.setStyleSheet("""
            QLabel {
                background-color: #ffffff;
                border: 4px dashed #ff8ac1;
                border-radius: 20px;
            }
        """)

        # ---------------------------
        #  ボタン（下部に配置）
        # ---------------------------
        self.btn_capture = QPushButton("📸 とる")
        self.btn_process = QPushButton("💖 合成する")

        button_area = QHBoxLayout()
        button_area.addWidget(self.btn_capture)
        button_area.addWidget(self.btn_process)
        button_area.setSpacing(40)
        button_area.setAlignment(Qt.AlignCenter)

        # ---------------------------
        #  メイン配置
        # ---------------------------
        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        layout.addSpacing(20)
        layout.addLayout(button_area)

        center = QWidget()
        center.setLayout(layout)
        self.setCentralWidget(center)

    # ------------------------------------------------------
    #  OpenCV画像を QLabel に表示（プリクラ機能維持）
    # ------------------------------------------------------
    def show_image(self, cv_img):
        if cv_img is None:
            return

        h, w, ch = cv_img.shape
        bytes_per_line = ch * w
        qimg = QImage(cv_img.data, w, h, bytes_per_line, QImage.Format_BGR888)
        pixmap = QPixmap.fromImage(qimg)

        scaled_pixmap = pixmap.scaled(
            self.image_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation
        )
        self.image_label.setPixmap(scaled_pixmap)
