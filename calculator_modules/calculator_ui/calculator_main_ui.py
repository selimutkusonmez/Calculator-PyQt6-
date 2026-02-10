import sys
from PyQt6.QtCore import Qt,QRegularExpression,QSize,pyqtSignal
from PyQt6.QtWidgets import (
     QApplication,QWidget,QMainWindow,QLineEdit,QPushButton,QTextEdit,QLabel,QGridLayout,QFrame,QTableWidget,QTableWidgetItem,QGroupBox,QComboBox,QMessageBox,QFileDialog,QListWidget,QTabWidget,QVBoxLayout,QSizePolicy)
from PyQt6.QtGui import QIcon,QPixmap,QIntValidator,QDoubleValidator,QRegularExpressionValidator,QKeyEvent,QPainter
import subprocess


from calculator_modules.calculator_styles.style_reader import read_style
from config import JPG_PATH

class MainUI(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        self.setWindowIcon(QIcon(JPG_PATH))
        self.setWindowTitle("Calculator")

        self.layout = QGridLayout()
        self.setLayout(self.layout)

        self.upper_groupbox = QGroupBox()
        self.upper_groupbox.setObjectName("upper_groupbox")
        self.upper_groupbox_layout = QGridLayout()
        self.upper_groupbox.setLayout(self.upper_groupbox_layout)
        self.layout.addWidget(self.upper_groupbox,0,0)

        self.upper_screen = QLineEdit()
        self.upper_screen.setReadOnly(True)
        self.upper_screen.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.upper_screen.setObjectName("upper_screen")
        self.upper_screen.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.upper_screen.setMinimumSize(50,50)
        self.upper_groupbox_layout.addWidget(self.upper_screen,0,0)

        self.lower_screen = QLineEdit()
        self.lower_screen.setReadOnly(True)
        self.lower_screen.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.lower_screen.setObjectName("lower_screen")
        self.lower_screen.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.lower_screen.setMinimumSize(50,50)
        self.upper_groupbox_layout.addWidget(self.lower_screen,1,0)

        self.lower_groupbox = QGroupBox()
        self.lower_groupbox.setMinimumSize(300,250)
        self.lower_groupbox.setObjectName("lower_groupbox")
        self.lower_groupbox_layout = QGridLayout()
        self.lower_groupbox.setLayout(self.lower_groupbox_layout)
        self.layout.addWidget(self.lower_groupbox,1,0)

        self.c_button = QPushButton("C")
        self.c_button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.c_button.clicked.connect(self.buttons_func)
        self.lower_groupbox_layout.addWidget(self.c_button,0,0)
        

        self.square_button = QPushButton("X2")
        self.square_button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.square_button.clicked.connect(self.buttons_func)
        self.lower_groupbox_layout.addWidget(self.square_button,0,1)
        

        self.button = QPushButton("")
        self.button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.button.clicked.connect(self.buttons_func)
        self.lower_groupbox_layout.addWidget(self.button,0,2)
        

        self.erase_button = QPushButton("ers")
        self.erase_button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.erase_button.clicked.connect(self.buttons_func)
        self.lower_groupbox_layout.addWidget(self.erase_button,0,3)
        

        self.mod_button = QPushButton("%")
        self.mod_button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.mod_button.clicked.connect(self.buttons_func)
        self.lower_groupbox_layout.addWidget(self.mod_button,1,0)
        

        self.one_divided_by_x_button = QPushButton("1/X")
        self.one_divided_by_x_button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.one_divided_by_x_button.clicked.connect(self.buttons_func)
        self.lower_groupbox_layout.addWidget(self.one_divided_by_x_button,1,1)
        

        self.square_root_button = QPushButton("SqrtX")
        self.square_root_button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.square_root_button.clicked.connect(self.buttons_func)
        self.lower_groupbox_layout.addWidget(self.square_root_button,1,2)
        

        self.plus_button = QPushButton("+")
        self.plus_button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.plus_button.clicked.connect(self.buttons_func)
        self.lower_groupbox_layout.addWidget(self.plus_button,1,3)
        

        self.one_button = QPushButton("1")
        self.one_button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.one_button.clicked.connect(self.buttons_func)
        self.lower_groupbox_layout.addWidget(self.one_button,2,0)
        

        self.two_button = QPushButton("2")
        self.two_button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.two_button.clicked.connect(self.buttons_func)
        self.lower_groupbox_layout.addWidget(self.two_button,2,1)
        
        
        self.three_button = QPushButton("3")
        self.three_button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.three_button.clicked.connect(self.buttons_func)
        self.lower_groupbox_layout.addWidget(self.three_button,2,2)
        

        self.minus_button = QPushButton("-")
        self.minus_button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.minus_button.clicked.connect(self.buttons_func)
        self.lower_groupbox_layout.addWidget(self.minus_button,2,3)
        

        self.four_button = QPushButton("4")
        self.four_button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.four_button.clicked.connect(self.buttons_func)
        self.lower_groupbox_layout.addWidget(self.four_button,3,0)
        

        self.five_button = QPushButton("5")
        self.five_button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.five_button.clicked.connect(self.buttons_func)
        self.lower_groupbox_layout.addWidget(self.five_button,3,1)
        

        self.six_button = QPushButton("6")
        self.six_button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.six_button.clicked.connect(self.buttons_func)
        self.lower_groupbox_layout.addWidget(self.six_button,3,2)
        

        self.divide_button = QPushButton("/")
        self.divide_button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.divide_button.clicked.connect(self.buttons_func)
        self.lower_groupbox_layout.addWidget(self.divide_button,3,3)
        

        self.seven_buton = QPushButton("7")
        self.seven_buton.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.seven_buton.clicked.connect(self.buttons_func)
        self.lower_groupbox_layout.addWidget(self.seven_buton,4,0)
        

        self.eight_button = QPushButton("8")
        self.eight_button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.eight_button.clicked.connect(self.buttons_func)
        self.lower_groupbox_layout.addWidget(self.eight_button,4,1)
        

        self.nine_button = QPushButton("9")
        self.nine_button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.nine_button.clicked.connect(self.buttons_func)
        self.lower_groupbox_layout.addWidget(self.nine_button,4,2)
        

        self.multiply_button = QPushButton("*")
        self.multiply_button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.multiply_button.clicked.connect(self.buttons_func)
        self.lower_groupbox_layout.addWidget(self.multiply_button,4,3)
        

        self.zeron_button = QPushButton("0")
        self.zeron_button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.zeron_button.clicked.connect(self.buttons_func)
        self.lower_groupbox_layout.addWidget(self.zeron_button,5,1)
        

        self.float_button = QPushButton(",")
        self.float_button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.float_button.clicked.connect(self.buttons_func)
        self.lower_groupbox_layout.addWidget(self.float_button,5,2)
        

        self.equals_button = QPushButton("=")
        self.equals_button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.equals_button.clicked.connect(self.buttons_func)
        self.lower_groupbox_layout.addWidget(self.equals_button,5,3)
        

        self.restart_button = QPushButton("Res")
        self.restart_button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.restart_button.clicked.connect(self.restart_button_func)
        self.lower_groupbox_layout.addWidget(self.restart_button,5,0)
        

        self.setStyleSheet(read_style("main_ui.qss"))
        
    def buttons_func(self):
        button = self.sender()





    def restart_button_func(self):
        QApplication.quit()
        subprocess.Popen([sys.executable, *sys.argv])

