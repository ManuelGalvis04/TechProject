# views/recovery.py
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QMessageBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class PasswordRecoveryWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Recuperar Contraseña')
        self.setFixedSize(500, 300)

        layout = QVBoxLayout()

        # Etiqueta de información
        self.infoLabel = QLabel("Introduce tu correo electrónico para recuperar tu contraseña", self)
        self.infoLabel.setFont(QFont("Arial", 12))
        layout.addWidget(self.infoLabel, alignment=Qt.AlignCenter)

        # Campo de entrada para el correo electrónico
        self.emailInput = QLineEdit(self)
        self.emailInput.setPlaceholderText('Correo electrónico')
        self.emailInput.setFont(QFont("Arial", 14))
        self.emailInput.setStyleSheet("""
            QLineEdit {
                padding: 15px;
                font-size: 14px;
                border: 2px solid #333;
                border-radius: 5px;
                background: #fff;
            }
        """)
        self.emailInput.setFixedWidth(300)
        layout.addWidget(self.emailInput, alignment=Qt.AlignCenter)

        # Botón de recuperación de contraseña
        self.recoverButton = QPushButton('Recuperar Contraseña', self)
        self.recoverButton.setFixedSize(200, 40)
        self.recoverButton.setStyleSheet("""
            QPushButton {
                font-size: 16px;
                border-radius: 5px;
                background: #0078d7;
                color: #fff;
            }
            QPushButton:hover {
                background: #005a9e;
            }
        """)
        layout.addWidget(self.recoverButton, alignment=Qt.AlignCenter)

        self.setLayout(layout)
