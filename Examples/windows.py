import sys
from PyQt5 import QtWidgets,QtGui

def Window():
    app = QtWidgets.QApplication(sys.argv) # app zorunlu
    windows = QtWidgets.QWidget() # pencere oluşturma 
    windows.setWindowTitle("PyQt5 - 1") # başlık 
    # -----------------------------------------------------------------------------
    label = QtWidgets.QLabel(windows) # label oluşturma 
    label.setText("Example") # label yazısı 
    label.move(150,30) # label i hareket ettirme
    label2 = QtWidgets.QLabel(windows)
    label2.setPixmap(QtGui.QPixmap("76ca2a302328bffce4a62c723ab51acb.png")) # Resim Ekleme
    label2.move(200,70)
    # -----------------------------------------------------------------------------
    windows.setGeometry(100,100,500,500) # window boyutu ayarlama
    windows.show() # gösterme 
    sys.exit(app.exec_()) # x e basana kadar çalıştırma
Window()