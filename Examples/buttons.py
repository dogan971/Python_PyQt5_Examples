import sys


from PyQt5 import QtWidgets

def window():
    app = QtWidgets.QApplication(sys.argv)
    
    window = QtWidgets.QWidget()
    window.setWindowTitle("PyQt5 - 2")
    button = QtWidgets.QPushButton(window)
    button.setText("Push")
    button.move(200,80)
    label = QtWidgets.QLabel(window)
    label.setText("Hello World..!")
    label.move(200,30)
    window.setGeometry(100,100,500,500)
    window.show()
    sys.exit(app.exec_())

window()