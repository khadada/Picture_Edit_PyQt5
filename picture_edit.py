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
        
        # 02: actions for "Edit" menu:
        self.rotate90_act = QAction("Rotate 90°",self)
        self.rotate90_act.setStatusTip("Rotate the picture 90° clockwise.")
        self.rotate90_act.triggered.connect(self.rotate_picture_90)
        
        self.rotate180_act = QAction("Rotate 180°",self)
        self.rotate180_act.setStatusTip("Rotate the picture 180° clockwise.")
        self.rotate180_act.triggered.connect(self.rotate_picture_180)
        
        self.flip_h_act = QAction("Flip Horizontal",self)
        self.flip_h_act.setStatusTip("Flip the picture across horizontal axis.")
        self.flip_h_act.triggered.connect(self.flip_picture_horizontal)
        
        self.flip_v_act = QAction("Flip Verticlal",self)
        self.flip_v_act.setStatusTip("Flip the picture across vertical axis.")
        self.flip_v_act.triggered.connect(self.flip_picture_vertical)
        
        self.resize_act = QAction("Resize Half",self)
        self.resize_act.setStatusTip("Resize picture to half of the original size.")
        self.resize_act.triggered.connect(self.resize_picture_half)
        
        self.clear_act = QAction(QIcon('icons/clear.png'),"Clear Picture",self)
        self.clear_act.setStatusTip("Clear the current picture")
        self.clear_act.setShortcut("Ctrl+Shift+c")
        self.clear_act.triggered.connect(self.clear_picture)
        
        # 03: Create Menu Bar
        menu_bar = self.menuBar()
        menu_bar.setNativeMenuBar(False)
        
        # 04: Create File menu and add its actions:
        file_menu = menu_bar.addMenu("File")
        file_menu.addAction(self.open_act)
        file_menu.addAction(self.save_act)
        file_menu.addSeparator()
        file_menu.addAction(self.print_act)
        file_menu.addSeparator()
        file_menu.addAction(self.exit_act)
        
        # 05: Create Edit menu and add its actions:
        edit_menu = menu_bar.addMenu("Edit")
        edit_menu.addAction(self.rotate90_act)
        edit_menu.addAction(self.rotate180_act)
        edit_menu.addSeparator()
        edit_menu.addAction(self.flip_h_act)
        edit_menu.addAction(self.flip_v_act)
        edit_menu.addSeparator()
        edit_menu.addAction(self.resize_act)
        edit_menu.addSeparator()
        edit_menu.addAction(self.clear_act)
        
        # 06: Create View menu and add its actions:
        view_menu = menu_bar.addMenu("View")
        view_menu.addAction(self.toggle_dock_tools_act)