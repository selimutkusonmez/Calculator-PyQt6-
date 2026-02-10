import sys
from PyQt6.QtCore import Qt,QRegularExpression,QSize
from PyQt6.QtWidgets import (
     QApplication,QWidget,QMainWindow,QLineEdit,QPushButton,QTextEdit,QLabel,QGridLayout,QFrame,QTableWidget,QTableWidgetItem,QGroupBox,QComboBox,QMessageBox,QFileDialog,QListWidget,QTabWidget,QVBoxLayout)
from PyQt6.QtGui import QIcon,QPixmap,QIntValidator,QDoubleValidator,QRegularExpressionValidator,QKeyEvent,QPainter

from calculator_modules.calculator_ui import *


class AppManager:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.login_ui = LoginUI()
        self.login_ui.login_code.connect(self.handle_login_result)
    
    def init_login_ui(self):
        self.login_ui.show()
        sys.exit(self.app.exec())
    
    def handle_login_result(self,login_code):
        if login_code == 1:
            self.login_ui.close()
            self.main_ui = MainUI()
            self.main_ui.show()

        else:
            print(login_code)
            return
    
if __name__ == "__main__":
    manager = AppManager()
    manager.init_login_ui()