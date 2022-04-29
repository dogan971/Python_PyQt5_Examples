import os
import sys
from PyQt5.QtWidgets import QWidget,QApplication,QTextEdit,QLabel,QPushButton,QVBoxLayout,QFileDialog,QHBoxLayout,QVBoxLayout,QAction,qApp,QMainWindow


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


class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.window = Notepad()
        self.setCentralWidget(self.window)
        
        self.create_menus()

        self.setWindowTitle("Metin Editörü")
        self.show()
    def create_menus(self):
        menubar = self.menuBar()
        file = menubar.addMenu("File")
        open_file = QAction("Open The File",self)
        open_file.setShortcut("Ctrl+O")
        save = QAction("Save",self)
        save.setShortcut("Ctrl+S")
        clear = QAction("Clear",self)
        exit = QAction("Exit",self)
        exit.setShortcut("Ctrl+Q")

        file.triggered.connect(self.response)

        file.addActions([open_file,save,clear,exit])

    def response(self,action):
        if action.text() == "Open The File":
            self.window.open_clicked()
        elif action.text() == "Save":
            self.window.save_clicked()
        elif action.text() == "Clear":
            self.window.clear_clicked()
        elif action.text() == "Exit":
            qApp.quit()

app = QApplication(sys.argv)
menu = Menu()
sys.exit(app.exec_())


            