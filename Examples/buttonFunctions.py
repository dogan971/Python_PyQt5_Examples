import sys
from PyQt5 import QtWidgets
class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.textLabel = QtWidgets.QLabel("Bana hiç tıklanmadı")
        self.button = QtWidgets.QPushButton("Tıkla")
        self.value = 0
        self.init_ui()

    def init_ui(self):
        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.button)
        v_box.addWidget(self.textLabel)
        v_box.addStretch()
        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()
        self.setLayout(h_box)
        self.button.clicked.connect(self.click)
        self.show()
    def click(self):
        self.value += 1
        self.textLabel.setText(f"Bana {self.value} Kere Tıklandı")

        

app = QtWidgets.QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())

