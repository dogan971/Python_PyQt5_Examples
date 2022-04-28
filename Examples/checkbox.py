import sys


from PyQt5.QtWidgets import QWidget,QApplication,QCheckBox,QPushButton,QLabel,QVBoxLayout

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.checkbox = QCheckBox("do u like python ?")
        self.text_area = QLabel("")
        self.button = QPushButton("Click me")

        v_box = QVBoxLayout()
        v_box.addWidget(self.checkbox)
        v_box.addWidget(self.text_area)
        v_box.addWidget(self.button)
        self.setLayout(v_box) 
        self.button.clicked.connect(lambda : self.click(self.checkbox.isChecked(),self.text_area))
        self.show()

    def click(self,ischecked,text_area):
        if ischecked:
            text_area.setText("Wonderful")
        else:
            text_area.setText("Why??")
        
app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())