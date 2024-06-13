from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QLineEdit, QPushButton
import sys


class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(700, 700)

        # Add chat area widget
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 580, 320)
        self.chat_area.setReadOnly(True)

        # Add input area widget
        self.input_area = QLineEdit(self)
        self.input_area.setGeometry(10, 340, 580, 40)

        # Add send button widget
        self.button = QPushButton('Send', self)
        self.button.setGeometry(595, 340, 100, 40)

        self.show()


class Chatbot:
    pass


app = QApplication(sys.argv)
main_window = ChatbotWindow()
sys.exit(app.exec())
