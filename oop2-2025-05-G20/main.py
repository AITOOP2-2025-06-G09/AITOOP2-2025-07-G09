## from src.lecture05_01 import lecture05_01

## if __name__ == "__main__":
##    lecture05_01()

from PySide6.QtWidgets import QApplication
from src.ui.main_window import MainWindow
from src.controllers.main_controller import MainController

def main():
    app = QApplication([])
    ui = MainWindow()
    controller = MainController(ui)

    ui.show()
    app.exec()

if __name__ == "__main__":
    main()