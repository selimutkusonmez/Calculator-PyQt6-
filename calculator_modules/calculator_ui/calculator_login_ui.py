import sys
from PyQt6.QtCore import Qt,QRegularExpression,QSize
from PyQt6.QtWidgets import (
     QApplication,QWidget,QMainWindow,QLineEdit,QPushButton,QTextEdit,QLabel,QGridLayout,QFrame,QTableWidget,QTableWidgetItem,QGroupBox,QComboBox,QMessageBox,QFileDialog,QListWidget,QTabWidget,QVBoxLayout)
from PyQt6.QtGui import QIcon,QPixmap,QIntValidator,QDoubleValidator,QRegularExpressionValidator,QKeyEvent,QPainter
import subprocess
import webbrowser

from calculator_modules.calculator_styles.style_reader import read_style
from calculator_modules.calculator_functions.calculator_login_functions import *

class LoginUI(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        
        self.setFixedSize(300,400)

        self.layout = QGridLayout()
        self.setLayout(self.layout)

        self.login_ui_groupbox = QGroupBox("Login")
        self.login_ui_groupbox_layout = QGridLayout()
        self.login_ui_groupbox.setLayout(self.login_ui_groupbox_layout)
        self.layout.addWidget(self.login_ui_groupbox)

        self.username_label = QLabel("Username")
        self.login_ui_groupbox_layout.addWidget(self.username_label,0,0)

        self.username_input = QLineEdit()
        self.login_ui_groupbox_layout.addWidget(self.username_input,0,1)

        self.password_label = QLabel("Password")
        self.login_ui_groupbox_layout.addWidget(self.password_label,1,0)

        self.password_input = QLineEdit()
        self.login_ui_groupbox_layout.addWidget(self.password_input,1,1)

        self.error_space = QLineEdit()
        self.error_space.setObjectName("error_space")
        self.error_space.setReadOnly(True)
        self.error_space.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.login_ui_groupbox_layout.addWidget(self.error_space,2,0,1,2)

        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.login_button_func)
        self.login_ui_groupbox_layout.addWidget(self.login_button,3,0,1,2)

        self.my_linkedin_button = QPushButton("My Linkedin")
        self.my_linkedin_button.clicked.connect(self.my_linkedin_button_func)
        self.login_ui_groupbox_layout.addWidget(self.my_linkedin_button,4,0,1,2)

        self.my_github_button = QPushButton("My Github")
        self.my_github_button.clicked.connect(self.my_github_button_func)
        self.login_ui_groupbox_layout.addWidget(self.my_github_button,5,0,1,2)

        self.restart_app_button = QPushButton("Restart App")
        self.restart_app_button.clicked.connect(self.restart_app_button_func)
        self.login_ui_groupbox_layout.addWidget(self.restart_app_button,6,0,1,2)

        self.setStyleSheet(read_style("login_ui.qss"))

    def login_button_func(self):
        self.error_space.setText(login(self.username_input.text(),self.password_input.text()))
        

    def restart_app_button_func(self):
        QApplication.quit()
        subprocess.Popen([sys.executable, *sys.argv])

    def my_linkedin_button_func(self):
        webbrowser.open("https://www.linkedin.com/in/selim-utku-sönmez/")
    
    def my_github_button_func(self):
        webbrowser.open("https://github.com/selimutkusonmez")

