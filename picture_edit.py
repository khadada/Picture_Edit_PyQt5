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
        # self.central_main_widget()
        # self.create_tools_docks()
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
        self.open_act = QAction(QIcon("icons/open.png"),"Open",self)
        self.open_act.setShortcut("Ctrl+O")
        self.open_act.setStatusTip("Open new picture")
        self.open_act.triggered.connect(self.open_picture)
        
        self.save_act = QAction(QIcon('icons/save.png'),"Save",self)
        self.save_act.setShortcut("Ctrl+S")
        self.save_act.setStatusTip("Save the picture")
        self.save_act.triggered.connect(self.save_picture)
        
        self.print_act = QAction(QIcon('icons/print.png'),"Print",self)
        self.print_act.setShortcut("Ctrl+P")
        self.print_act.setStatusTip("Print the current picture.")
        #self.print_act.triggered.connect(self.print_image)
        
        self.exit_act = QAction(QIcon('icons/exit.png'),"Exit",self)
        self.exit_act.setShortcut("Ctrl+Q")
        self.exit_act.setStatusTip("Close the program (T_T).")
        self.exit_act.triggered.connect(self.close)
        
        # 02: actions for "Edit" menu:
        self.rotate90_act = QAction("Rotate 90°",self)
        self.rotate90_act.setStatusTip("Rotate the picture 90° clockwise.")
        #self.rotate90_act.triggered.connect(self.rotate_picture_90)
        
        self.rotate180_act = QAction("Rotate 180°",self)
        self.rotate180_act.setStatusTip("Rotate the picture 180° clockwise.")
        #self.rotate180_act.triggered.connect(self.rotate_picture_180)
        
        self.flip_h_act = QAction(QIcon('icons/flip_h.png'),"Flip Horizontal",self)
        self.flip_h_act.setStatusTip("Flip the picture across horizontal axis.")
        #self.flip_h_act.triggered.connect(self.flip_picture_horizontal)
        
        self.flip_v_act = QAction(QIcon('icons/flip_v.png'),"Flip Verticlal",self)
        self.flip_v_act.setStatusTip("Flip the picture across vertical axis.")
        #self.flip_v_act.triggered.connect(self.flip_picture_vertical)
        
        self.resize_act = QAction("Resize Half",self)
        self.resize_act.setStatusTip("Resize picture to half of the original size.")
        #self.resize_act.triggered.connect(self.resize_picture_half)
        
        self.clear_act = QAction(QIcon('icons/clear.png'),"Clear Picture",self)
        self.clear_act.setStatusTip("Clear the current picture")
        self.clear_act.setShortcut("Ctrl+Shift+c")
        #self.clear_act.triggered.connect(self.clear_picture)
        
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
        # view_menu.addAction(self.toggle_dock_tools_act)
        
        # 07: Create About menu and add its actions:
        about_action = QAction(QIcon("icons/about.png"), 'About', self)
        about_action.setShortcut("Ctrl+Shift+H")
        about_action.triggered.connect(self.about_us)
        about_menu = menu_bar.addMenu("About")
        about_menu.addAction(about_action)
        
        # 08: Create Status bar to display info tips:
        self.setStatusBar(QStatusBar(self))
    
    def create_toolbar(self):
        """
        Create toobar for picture editor 
        """
        tool_bar = QToolBar()
        tool_bar.setIconSize(QSize(25, 25))
        self.addToolBar(tool_bar)
        
        # Adding actions to toolbar
        tool_bar.addAction(self.open_act)
        tool_bar.addAction(self.save_act)
        tool_bar.addAction(self.print_act)
        tool_bar.addAction(self.clear_act)
        tool_bar.addSeparator()
        tool_bar.addAction(self.exit_act)
    
    def create_tools_docks(self):
        """
        Use View -> Edit picture tools menu and click the dock widget on or off.
        Tools dock can be placen on the left or right og the main window.
        """
        # Setup QDockWigdet:
        self.dock_tools_view = QDockWidget()
        self.dock_tools_view.setWindowTitle("Edit Picture Tools")
        self.dock_tools_view.setAllowedAreas(Qt.LeftDockWidgetArea|Qt.RightDockWidgetArea)
        # Create container QWidget to hold all widgets inside dock widget 
        self.tools_container = QWidget()
        # Btn for 90° :
        self.rotate_90 = QPushButton('Rotate 90°')
        self.rotate_90.setMinimumSize(QSize(150, 50))
        self.rotate_90.setStatusTip("Rotate picture 90° clockwise")
        self.rotate_90.clicked.connect(self.rotate_picture_90)
        # Btn for 180° :
        self.rotate_180 = QPushButton('Rotate 180°')
        self.rotate_180.setMinimumSize(QSize(150, 50))
        self.rotate_180.setStatusTip("Rotate picture 180° clockwise")
        self.rotate_180.clicked.connect(self.rotate_picture_180)
        # Btn for flip horizontal :
        self.flip_btn_h = QPushButton('Flip Horizontal')
        self.flip_btn_h.setMinimumSize(QSize(150, 50))
        self.flip_btn_h.setStatusTip("Flip picture across horizontal axis")
        self.flip_btn_h.clicked.connect(self.flip_picture_horizontal)
        # Btn for flip vertical :
        self.flip_btn_v = QPushButton('Flip Vertical')
        self.flip_btn_v.setMinimumSize(QSize(150, 50))
        self.flip_btn_v.setStatusTip("Flip picture across vertical axis")
        self.flip_btn_v.clicked.connect(self.flip_picture_vertical)
        # Btn for resize :
        self.resize_btn = QPushButton('Resize Half')
        self.resize_btn.setMinimumSize(QSize(150, 50))
        self.resize_btn.setStatusTip("Resize picture to half of the original size.")
        self.resize_btn.clicked.connect(self.resize_picture_half)
        # Setup vertical layout to contain all the push buttons above:
        dock_layout_h = QVBoxLayout()
        dock_layout_h.addWidget(self.rotate_90)
        dock_layout_h.addWidget(self.rotate_180)
        dock_layout_h.addStretch(1)
        dock_layout_h.addWidget(self.flip_btn_h)
        dock_layout_h.addWidget(self.flip_btn_v)
        dock_layout_h.addStretch(1)
        dock_layout_h.addWidget(self.resize_btn)
        dock_layout_h.addStretch(6)
        # Set the main layout for container of tools_container
        # then set the main widget of dock widget
        self.tools_container.setLayout(dock_layout_h)
        self.dock_tools_view.setWidget(self.tools_container)
        # set initial location of dock widget:
        self.addDockWidget(Qt.RightDockWidgetArea, self.dock_tools_view)
        # Handles the visibility of the dock widget:
        self.toggle_dock_tools_act = self.dock_tools_view.toggleViewAction()
    
    def picture_editor_widget(self):
        """
        Setup instance of widgets for picture editor GUI.
        """    
        self.picture = QPixmap()
        self.picture_labl = QLabel()
        self.picture_labl.setAlignment(Qt.AlignCenter)
        # Use setSizePolicy to specify now the widget can be resized,
        # horizontally and vertically. Here , the picture will stretch horizontally
        # but not verticaly
        self.picture_labl.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Ignored)
        self.setCentralWidget(self.picture_labl)
    
    def open_picture(self):
        """
        Open an picture file and display its content in label widget.
        Display error message if image can't be opened
        """ 
        picture_file,_ = QFileDialog.getOpenFileName(self,"Open Picture","","JPG Files (*jpeg *.jpg);;PNG Files (*.png);;Bitmap Files (*.bmp);;GIF Files (*.gif)")
        if picture_file:
            self.picture = QPixmap(picture_file)
            self.picture_labl.setPixmap(self.picture.scaled(self.picture.size(),Qt.KeepAspectRatio,Qt.SmoothTransformation))
        else:
            QMessageBox.information(self,"Error Occur","Unable to open the picture.",QMessageBox.Ok)   
        self.print_act.setEnabled(True)
    
    def save_picture(self):
        """
        Save The Picture.
        Display error message if picture can't be saved.
        """
        picture_name,_ = QFileDialog.getSaveFileName(self,"Save Picture","","JPG Files (*jpeg *.jpg);;PNG Files (*.png);;Bitmap Files (*.bmp);;GIF Files (*.gif)")
        if picture_name and self.picture.isNull() == False:
            self.picture.save(picture_name)
        else:
            QMessageBox.warning(self,"Error Occur", "Unable to save the picture.",QMessageBox.Ok)
    
    
    def about_us(self):
        """
        Display information about the Developer who code this GUI.
        """
        QMessageBox.about(self,"About Picture Editor","Beginner's Pratical Guid to Create GUI\n\nThis program was create by:Khald Melizi\n\nPhone: +213780360303\n\nEmail:lkhadada@gmail.com\n\nDate:09/04/2022\n\nIn: Temacine W. Touggourt.")
    
        
# Run the program:
if __name__ == "__main__":
    app = QApplication(sys.argv)
    picture_program = PictureEditor()
    sys.exit(app.exec_())