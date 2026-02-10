from PyQt6.QtGui import QKeyEvent
from PyQt6.QtCore import Qt

def key_press_event_function(key,text,self):

    if Qt.Key.Key_0 <= key <= Qt.Key.Key_9:
            if text == "0" : return self.zero_button

            elif text == "1" : return self.one_button

            elif text == "2" : return self.two_button

            elif text == "3" : return self.three_button

            elif text == "4" : return self.four_button

            elif text == "5" : return self.five_button

            elif text == "6" : return self.six_button

            elif text == "7" : return self.seven_buton

            elif text == "8" : return self.eight_button

            elif text == "9" : return self.nine_button
    elif key == Qt.Key.Key_Plus:
            return self.plus_button
    
    elif key == Qt.Key.Key_Minus:
            return self.minus_button
    
    elif key == Qt.Key.Key_Asterisk:
            return self.multiply_button
    
    elif key == Qt.Key.Key_Slash:
            return self.divide_button
    
    elif key == Qt.Key.Key_Comma:
            return self.float_button
    
    elif key == Qt.Key.Key_Backspace:
            return self.erase_button
    
    elif key == Qt.Key.Key_Return or key == Qt.Key.Key_Enter:
            return self.equals_button
    else : return None