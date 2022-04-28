import os
import sys
from PyQt5.QtWidgets import QWidget,QApplication,QTextEdit,QLabel,QPushButton,QVBoxLayout,QFileDialog,QHBoxLayout,QVBoxLayout


class Notepad(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.text_area = QTextEdit()
        self.clear = QPushButton("Clear")
        self.open = QPushButton("Open")
        self.save = QPushButton("Save")
        h_box = QHBoxLayout()
        h_box.addWidget(self.clear)
        h_box.addWidget(self.open)
        h_box.addWidget(self.save)
        v_box = QVBoxLayout()
        v_box.addWidget(self.text_area)
        v_box.addLayout(h_box)
        self.setLayout(v_box)
        self.clear.clicked.connect(self.clear_clicked)
        self.open.clicked.connect(self.open_clicked)
        self.save.clicked.connect(self.save_clicked)
        self.show()
    def clear_clicked(self):
        self.text_area.clear()
    
    def open_clicked(self):
        file_name = QFileDialog.getOpenFileName(self,"Open The File",os.getenv("DESKTOP"))
        with open(file_name[0],"r",encoding="utf-8") as file:
            self.text_area.setText(file.read())
    def save_clicked(self):
        file_name = QFileDialog.getSaveFileName(self,"Save the file",os.getenv("DESKTOP"))
        with open(file_name[0],"w",encoding="utf-8") as file:
            file.write(self.text_area.toPlainText())
app = QApplication(sys.argv)
notepad = Notepad()
sys.exit(app.exec_())


            