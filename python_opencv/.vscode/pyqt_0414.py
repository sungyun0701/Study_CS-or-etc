# pip install PyQt5 --use-feature=2020-resolver
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

class MyApp(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()

# 윈도우 프로그램 만들때 매개변수가 없어도 self를 넣어줘야 한다.
    def initUI(self):
        # self.setWindowTitle('My First Application')
        
        # self.move(300, 300)
        # self.resize(400, 200)
        self.setWindowTitle('Button Test')
        btn1 = QPushButton('no1', self)
        # btn1.setCheckable(True)
        # btn1.toggle()
        btn2 = QPushButton('no2',self)
        # btn2.setText('no2')
        btn3 = QPushButton('no3', self)
        # btn3.setEnabled(False)
        
        vbox = QVBoxLayout()
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        # vbox.addWidget(btn3)

        self.setLayout(vbox)
        self.setGeometry(2200,300,400,200)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
