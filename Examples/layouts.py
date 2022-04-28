import sys
from PyQt5 import QtWidgets

def window():
    app = QtWidgets.QApplication(sys.argv)
    okayButton = QtWidgets.QPushButton("Okey")
    cancelButton = QtWidgets.QPushButton("Cancel")
    # Vertical Layout
    # v_box = QtWidgets.QVBoxLayout()
    # v_box.addWidget(okayButton)
    # v_box.addWidget(cancelButton)
    # v_box.addStretch() # Yukarı sabitledi
    # Horizantol Layout
    # h_box = QtWidgets.QHBoxLayout()
    # h_box.addWidget(okayButton)
    # h_box.addWidget(cancelButton)
    # h_box.addStretch() # sola sabitliyor
   
   # 2 sini bir arada kullanmak 
    h_box = QtWidgets.QHBoxLayout()
    h_box.addStretch() # Sağa yasladık
    h_box.addWidget(okayButton)
    h_box.addWidget(cancelButton)
    v_box = QtWidgets.QVBoxLayout()
    v_box.addStretch()
    v_box.addLayout(h_box)   
    # window
    window = QtWidgets.QWidget()
    window.setWindowTitle("PyQt5 - 3")
    window.setLayout(v_box)
    window.setGeometry(100,100,500,500)
    window.show()
    sys.exit(app.exec_())

window()