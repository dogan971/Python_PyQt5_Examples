import sqlite3
import sys


from PyQt5 import QtWidgets


class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.connect_db()

    
    def connect_db(self):
        connect = sqlite3.connect("database.db")
        self.cursor = connect.cursor()
        self.cursor.execute("Create table if not exists uyeler (user_name TEXT,password TEXT)")
        connect.commit()

    

    def init_ui(self):
        self.user_name = QtWidgets.QLineEdit()
        self.password = QtWidgets.QLineEdit()
        self.password.setEchoMode(QtWidgets.QLineEdit.Password) # password şifreleme
        self.loginButton = QtWidgets.QPushButton("Login")
        self.text_area = QtWidgets.QLabel("")

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.user_name)
        v_box.addWidget(self.password)
        v_box.addWidget(self.text_area)
        v_box.addStretch()
        v_box.addWidget(self.loginButton)

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)


        self.setLayout(v_box)
        self.setWindowTitle("Login Panel")
        self.loginButton.clicked.connect(self.login)
        self.show()

    def login(self):
        name = self.user_name.text()
        password = self.password.text()
        self.cursor.execute("Select * From uyeler where user_name = ? and password = ?",(name,password))
        list = self.cursor.fetchall()
        if len(list) == 0:
            self.text_area.setText("Böyle bir kullanıcı yok")
        else:
            self.text_area.setText("Giriş Yapıldı.")
            

app = QtWidgets.QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())