import sys


from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QRadioButton,QVBoxLayout,QPushButton

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        self.radioText = QLabel("Which language do you like more?")
        
        self.java = QRadioButton("Java")
        self.python = QRadioButton("Python")
        self.javascript = QRadioButton("Ecmascript")
        
        self.text_area = QLabel("")
        self.button = QPushButton("Submit")
        v_box = QVBoxLayout()
        v_box.addWidget(self.radioText)
        v_box.addWidget(self.java)
        v_box.addWidget(self.python)
        v_box.addWidget(self.javascript)
        v_box.addStretch()
        v_box.addWidget(self.text_area)
        v_box.addWidget(self.button)
        self.setLayout(v_box)
        
        self.button.clicked.connect(lambda : self.click(self.java.isChecked(),self.python.isChecked(),self.javascript.isChecked(),self.text_area))
        self.show()

    def click(self,java,python,ecmascript,text_area):
        if java:
            text_area.setText("Java")
        elif python:
            text_area.setText("Python")
        elif ecmascript:
            text_area.setText("JS")
        else:
            text_area.setText("Choose ur any radioButton")

app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())