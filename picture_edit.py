# Import necessary module and classes:
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow,QWidget,QLabel,QAction,QFileDialog,QDesktopWidget,QMessageBox,QSizePolicy,QToolBar,QStatusBar,QDockWidget,QVBoxLayout,QPushButton)
from PyQt5.QtGui import(QIcon, QPixmap,QTransform,QPainter)
from PyQt5.QtCore import (Qt, QSize, QRect)
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter

# Create class that hold own GUI:
class PictureEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initialize_ui()
        self.show()
        
    def initialize_ui(self):
        """
        Initialize the window and display its contents to the screen
        """
        self.setFixedSize(700, 700)
        self.setWindowTitle("5.2 Picute Editor")
        self.central_main_widget()
        self.create_tools_docks()
        self.create_menu()
        self.create_toolbar()
        self.picture_editor_widget()
    
    def create_menu(self):
        """
        Create menu for this project.
        """
        # I: Creating Actions 
        # 01: actions for "File" menu:
        self.setIconSize(QSize(20, 20))
        self.open_act = QAction(QIcon("icons/open.png","Open",self))
        self.open_act.setShortcut("Ctrl+O")
        self.open_act.setStatusTip("Open new picture")
        self.open_act.triggered.connect(self.open_image)
        
        self.save_act = QAction(QIcon('icons/save.png'),"Save",self)
        self.save_act.setShortcut("Ctrl+S")
        self.save_act.setStatusTip("Save the picture")
        self.save_act.triggered.connect(self.save_image)
        
        self.print_act = QAction(QIcon('icons/print.png'),"Print",self)
        self.print_act.setShortcut("Ctrl+P")
        self.print_act.setStatusTip("Print the current picture.")
        self.print_act.triggered.connect(self.print_image)
        
        self.exit_act = QAction(QIcon('icons/exit.png'),"Exit",self)
        self.exit_act.setShortcut("Ctrl+Q")
        self.exit_act.setStatusTip("Close the program (T_T).")
        self.exit_act.triggered.connect(self.close)