import sys


from PyQt5.QtWidgets import QMenu,QApplication,QAction,qApp,QMainWindow


class Menu(QMainWindow):
    def __init__(self):
        super().__init__()

        menubar = self.menuBar()
        file = menubar.addMenu("File")
        edit = menubar.addMenu("Edit")
        self.setWindowTitle("Menus")
        # Actions Operations
        open_file = QAction("Open",self)
        open_file.setShortcut("Ctrl+O")
        save_file = QAction("Save",self)
        save_file.setShortcut("Ctrl+S")
        exit = QAction("Exit",self)
        exit.setShortcut("Ctrl+Q")
        # Add Actions
        file.addAction(open_file)
        file.addAction(save_file)
        file.addAction(exit)
        clear = QAction("Clear",self)
        
        # Add Second Menu
        searchAndUpdate = edit.addMenu("Search And Update")
        search = QAction("Search",self)
        searchAndUpdate.addAction(search)
        update = QAction("Update",self)
        searchAndUpdate.addAction(update)
        edit.addAction(clear)


        exit.triggered.connect(self.exit)
        file.triggered.connect(self.response)
        self.show()
    def exit(self):
        qApp.quit()
    def response(self,action):
        if action.text() == "Open":
           print("Open")
        elif action.text() == "Save":
            print("Save")
        elif action.text() == "Exit":
            print("Exit")



app = QApplication(sys.argv)
menu = Menu()
sys.exit(app.exec_())