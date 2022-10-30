#This script uses pyqt5
#On launch it opens a GUI window that has 4 buttons. Each button logs "Button pressed" to the console.
#All buttons are evenly spaced and centered in the window.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn1 = QPushButton('Button 1', self)
        btn1.move(50, 50)
        btn1.clicked.connect(self.buttonClicked)

        btn2 = QPushButton('Button 2', self)
        btn2.move(50, 100)
        btn2.clicked.connect(self.buttonClicked)

        btn3 = QPushButton('Button 3', self)
        btn3.move(50, 150)
        btn3.clicked.connect(self.buttonClicked)

        btn4 = QPushButton('Button 4', self)
        btn4.move(50, 200)
        btn4.clicked.connect(self.buttonClicked)


        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Window')
        self.show()


    def buttonClicked(self):
        sender = self.sender()
        print(sender.text() + ' was pressed')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())








