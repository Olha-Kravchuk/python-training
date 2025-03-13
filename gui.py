import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtGui import QIcon
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My cool first GUI")
        self.setGeometry(700, 300, 500, 500)
        self.setWindowIcon(QIcon("ko.png"))

        # label = QLabel("Hallo", self)
        # label.setFont(QFont("Arial", 40))
        # label.setGeometry(0, 0, 500, 100)
        # label.setStyleSheet("color: #292929;"
        #                     "background-color: #6fdcf7;"
        #                     "font-weight: bold;"
        #                     "font-style: italic;"
        #                     "text-decoration: underline;")
        # label.setAlignment(Qt.AlignmentFlag.AlignTop)
        # label.setAlignment(Qt.AlignmentFlag.AlignBottom)
        # label.setAlignment(Qt.AlignmentFlag.AlignVCenter)

        # label.setAlignment(Qt.AlignmentFlag.AlignRight)
        # label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        # label.setAlignment(Qt.AlignmentFlag.AlignLeft)

        # label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignBottom)

        label2 = QLabel(self)
        label2.setGeometry(0, 0, 250, 250)
        label2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        pixmap = QPixmap("26.jpg")
        label2.setPixmap(pixmap)
        label2.setScaledContents(True)
        label2.setGeometry((self.width() - label2.width()) // 2, 
                           (self.height() - label2.height()) // 2, 
                           label2.width(), 
                           label2.height())

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

# if __name__ == "__main__":
#     main()