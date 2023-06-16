import sys

import pytesseract
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import cv2
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap, QImage
from PyQt5.QtGui import QImage
import cv2, imutils
from PIL.ImageQt import ImageQt
from PIL import Image


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 image - pythonspot.com'
        self.left = 100
        self.top = 100
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        img = cv2.imread('number2.JPG')

        ret, th1 = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY)
        # Create widget
        height, width, channel = th1.shape
        bytesPerLine = 3 * width
        qImg = QImage(th1.tobytes(), width, height, bytesPerLine, QImage.Format_BGR888).rgbSwapped()

        print(pytesseract.image_to_string(th1))
        text_value = pytesseract.image_to_string(th1)
        print('Text is :', text_value)

        label = QLabel(self)
        pixmap = QPixmap(qImg)
        label.setPixmap(pixmap)
        self.resize(pixmap.width(), pixmap.height())

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())