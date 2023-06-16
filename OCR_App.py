from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel, QTextEdit,QScrollArea
import sys
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QImage
import cv2, imutils
import pytesseract
from PyQt5.QtGui import QPixmap


class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.title = "PyQt5 OCR Application"
        self.top = 200
        self.left = 500
        self.width = 400
        self.height = 300
        imagePath = None

        self.InitWindow()

    def InitWindow(self):
        self.scroll = QScrollArea()

        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        vbox = QVBoxLayout()

        self.btn1 = QPushButton("Load Image")
        self.btn1.clicked.connect(self.getImage)
        vbox.addWidget(self.btn1)

        self.label = QLabel("")
        vbox.addWidget(self.label)
        vbox.addStretch()

        self.plain = QTextEdit()
        vbox.addWidget(self.plain)

        self.plain.move(0, 305)
        self.plain.resize(30, 50)
        self.btn2 = QPushButton("Get OCR")
        self.btn2.clicked.connect(self.getOcr)
        vbox.addWidget(self.btn2)
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.setLayout(vbox)


    def getImage(self):
        global imagePath
        fname = QFileDialog.getOpenFileName(self, 'Open file')
        imagePath = fname[0]
        pixmap = QPixmap(imagePath)
        self.label.setPixmap(QPixmap(pixmap))
        self.resize(pixmap.width(), pixmap.height())
        # self.image = cv2.imread(fname)
        #self.getOcr(fname)
        return imagePath

    def getOcr(self):
        print(imagePath)
        self.image = cv2.imread(imagePath)
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        pixmap = QPixmap(imagePath)
        self.label.setPixmap(QPixmap(pixmap))
        self.resize(pixmap.width(), pixmap.height())
        print(pytesseract.image_to_string(gray))
        text_value = pytesseract.image_to_string(gray)
        print('Text is :', text_value)
        self.plain.setText(text_value)
        return text_value

App = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(App.exec_())