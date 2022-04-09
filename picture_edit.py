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
        
        
        