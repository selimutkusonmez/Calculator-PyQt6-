import sys
from PyQt6.QtCore import Qt,QRegularExpression,QSize
from PyQt6.QtWidgets import (
     QApplication,QWidget,QMainWindow,QLineEdit,QPushButton,QTextEdit,QLabel,QGridLayout,QFrame,QTableWidget,QTableWidgetItem,QGroupBox,QComboBox,QMessageBox,QFileDialog,QListWidget,QTabWidget,QVBoxLayout)
from PyQt6.QtGui import QIcon,QPixmap,QIntValidator,QDoubleValidator,QRegularExpressionValidator,QKeyEvent,QPainter

from calculator_modules.calculator_ui.calculator_login_ui import LoginUI

print("sa")

class AppManager:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.login_ui = LoginUI()
    
    def init_login_ui(self):
        print("sa")
        self.login_ui.showMaximized()
        sys.exit(self.app.exec())
    
    def handle_login_result(self):
        return
    
if __name__ == "__main__":
    manager = AppManager()
    manager.init_login_ui()