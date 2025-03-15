from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QMessageBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication

from controllers.create_account_controller import create_user

class CreateAccountWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Crear una Cuenta')
        self.setFixedSize(700, 400)

        # Centrar la ventana en la pantalla
        screen_geometry = QApplication.desktop().screenGeometry()
        x = (screen_geometry.width() - self.width()) // 2
        y = (screen_geometry.height() - self.height()) // 2
        self.move(x, y)

        layout = QVBoxLayout()

        # Etiqueta de información
        self.infoLabel = QLabel("Introduce los datos para crear una nueva cuenta", self)
        self.infoLabel.setFont(QFont("Arial", 12))
        layout.addWidget(self.infoLabel, alignment=Qt.AlignCenter)

        # Campos de entrada para crear una cuenta
        self.usernameInput = QLineEdit(self)
        self.usernameInput.setPlaceholderText('Nombre de usuario')
        self.usernameInput.setFont(QFont("Arial", 14))
        self.usernameInput.setStyleSheet("""
            QLineEdit {
                padding: 15px;
                font-size: 14px;
                border: 2px solid #333;
                border-radius: 5px;
                background: #fff;
            }
        """)
        self.usernameInput.setFixedWidth(300)
        layout.addWidget(self.usernameInput, alignment=Qt.AlignCenter)

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

        self.passwordInput = QLineEdit(self)
        self.passwordInput.setPlaceholderText('Contraseña')
        self.passwordInput.setFont(QFont("Arial", 14))
        self.passwordInput.setEchoMode(QLineEdit.Password)
        self.passwordInput.setStyleSheet("""
            QLineEdit {
                padding: 15px;
                font-size: 14px;
                border: 2px solid #333;
                border-radius: 5px;
                background: #fff;
            }
        """)
        self.passwordInput.setFixedWidth(300)
        layout.addWidget(self.passwordInput, alignment=Qt.AlignCenter)

        # Botón de crear cuenta
        self.createButton = QPushButton('Crear Cuenta', self)
        self.createButton.clicked.connect(self.handleCreateAccount)
        self.createButton.setFixedSize(150, 40)
        self.createButton.setStyleSheet("""
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
        layout.addWidget(self.createButton, alignment=Qt.AlignCenter)

        self.setLayout(layout)

    def handleCreateAccount(self):
        """Maneja el evento de creación de cuenta."""
        username = self.usernameInput.text()
        email = self.emailInput.text()
        password = self.passwordInput.text()
        
        if username and email and password:
            success, message = create_user(username, email, password)
            if success:
                QMessageBox.information(self, 'Cuenta Creada', message)
                self.close()
            else:
                QMessageBox.warning(self, 'Error', message)
        else:
            QMessageBox.warning(self, 'Error', 'Por favor, rellena todos los campos')
