import sys
import os
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QMessageBox, QStackedLayout
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt

# Añadir el directorio raíz del proyecto al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from controllers.login_controller import authenticate_user
from views.recovery import PasswordRecoveryWindow
from views.create_account import CreateAccountWindow

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Inicio de Sesión con Microsoft')
        self.setGeometry(100, 100, 800, 600)

        # Configurar la imagen de fondo
        self.imageLabel = QLabel(self)
        image_path = os.path.abspath('./Graphic_Interface/fondofinal.png')
        pixmap = QPixmap(image_path)
        if pixmap.isNull():
            print(f"No se pudo cargar la imagen de la ruta: {image_path}")
        self.imageLabel.setPixmap(pixmap)
        self.imageLabel.setScaledContents(True)

        # Layout principal
        mainLayout = QStackedLayout(self)

        # Layout para el inicio de sesión
        loginLayout = QVBoxLayout()

        # Configurar el ícono de usuario
        self.userIcon = QLabel(self)
        user_icon_path = os.path.abspath('./Graphic_Interface/file.png')
        user_pixmap = QPixmap(user_icon_path)
        if user_pixmap.isNull():
            print(f"No se pudo cargar la imagen de usuario de la ruta: {user_icon_path}")
        self.userIcon.setPixmap(user_pixmap)
        self.userIcon.setAlignment(Qt.AlignCenter)
        self.userIcon.setFixedSize(150, 150)
        self.userIcon.setScaledContents(True)
        loginLayout.addWidget(self.userIcon, alignment=Qt.AlignCenter)

        # Añadir un espacio después de la imagen de usuario
        loginLayout.addSpacing(20)

        # Campo de entrada para el nombre de usuario
        self.username = QLineEdit(self)
        self.username.setPlaceholderText('Correo electrónico, teléfono o Skype')
        self.username.setFont(QFont("Arial", 16))
        self.username.setStyleSheet("""
            QLineEdit {
                padding: 15px;
                font-size: 16px;
                border: 2px solid #333;
                border-radius: 5px;
                background: #fff;
            }
        """)
        self.username.setFixedWidth(350)
        loginLayout.addWidget(self.username, alignment=Qt.AlignCenter)

        # Añadir un espacio después del campo de usuario
        loginLayout.addSpacing(10)
        
        # Campo de entrada para la contraseña
        self.password = QLineEdit(self)
        self.password.setPlaceholderText('Contraseña')
        self.password.setFont(QFont("Arial", 16))
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setStyleSheet("""
            QLineEdit {
                padding: 15px;
                font-size: 16px;
                border: 2px solid #333;
                border-radius: 5px;
                background: #fff;
            }
        """)
        self.password.setFixedWidth(350)
        loginLayout.addWidget(self.password, alignment=Qt.AlignCenter)

        # Añadir un espacio después del campo de contraseña
        loginLayout.addSpacing(20)

        # Botón de inicio de sesión
        self.loginButton = QPushButton('Siguiente', self)
        self.loginButton.clicked.connect(self.handleLogin)
        self.loginButton.setFixedSize(150, 40)
        self.loginButton.setStyleSheet("""
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
        loginLayout.addWidget(self.loginButton, alignment=Qt.AlignCenter)

        # Conectar la tecla Enter al botón de inicio de sesión
        self.username.returnPressed.connect(self.handleLogin)
        self.password.returnPressed.connect(self.handleLogin)
        self.loginButton.setDefault(True)

        # Añadir un espacio después del botón de inicio de sesión
        loginLayout.addSpacing(10)

        # Enlace para recuperación de contraseña
        self.forgotPasswordLink = QLabel("<a style='color: #ffffff' href='#'>¿Olvidaste tu contraseña?</a>", self)
        self.forgotPasswordLink.setFont(QFont("Arial", 12))
        self.forgotPasswordLink.setAlignment(Qt.AlignCenter)
        self.forgotPasswordLink.setStyleSheet("""
            QLabel {
                color: #ffffff;  # Cambiar el color del enlace a blanco
            }
            QLabel:hover {
                color: #cccccc;
            }
        """)
        self.forgotPasswordLink.linkActivated.connect(self.openRecoveryWindow)
        loginLayout.addWidget(self.forgotPasswordLink, alignment=Qt.AlignCenter)

        # Añadir un espacio después del enlace de recuperación de contraseña
        loginLayout.addSpacing(10)

        # Enlace para crear una cuenta
        self.createAccountLink = QLabel("<a style='color: #ffffff' href='#'>Crear una cuenta</a>", self)
        self.createAccountLink.setFont(QFont("Arial", 12))
        self.createAccountLink.setAlignment(Qt.AlignCenter)
        self.createAccountLink.setStyleSheet("""
            QLabel {
                color: #ffffff;  # Cambiar el color del enlace a blanco
            }
            QLabel:hover {
                color: #cccccc;
            }
        """)
        self.createAccountLink.linkActivated.connect(self.openCreateAccountWindow)
        loginLayout.addWidget(self.createAccountLink, alignment=Qt.AlignCenter)

        # Widget de inicio de sesión
        loginWidget = QWidget(self)
        loginWidget.setLayout(loginLayout)
        loginWidget.setStyleSheet("background: transparent;")
        loginWidget.setFixedSize(450, 500)

        # Layout para superponer el loginWidget sobre el fondo
        overlayLayout = QVBoxLayout()
        overlayLayout.addStretch(1)
        overlayLayout.addWidget(loginWidget, alignment=Qt.AlignCenter)
        overlayLayout.addStretch(1)

        # Widget de superposición
        overlayWidget = QWidget(self)
        overlayWidget.setLayout(overlayLayout)

        mainLayout.addWidget(overlayWidget)

        self.setLayout(mainLayout)

    def resizeEvent(self, event):
        """Ajusta el tamaño de la imagen de fondo cuando la ventana se redimensiona."""
        self.imageLabel.setFixedSize(self.size())

    def handleLogin(self):
        """Maneja el evento de inicio de sesión."""
        username = self.username.text()
        password = self.password.text()
        if authenticate_user(username, password):
            QMessageBox.information(self, 'Éxito', 'Inicio de sesión exitoso')
        else:
            QMessageBox.warning(self, 'Error', 'Nombre de usuario, correo electrónico o contraseña incorrectos')

    def openRecoveryWindow(self):
        """Abre la ventana de recuperación de contraseña."""
        self.recoveryWindow = PasswordRecoveryWindow()
        self.recoveryWindow.show()

    def openCreateAccountWindow(self):
        """Abre la ventana de creación de cuenta."""
        self.createAccountWindow = CreateAccountWindow()
        self.createAccountWindow.show()

    def keyPressEvent(self, event):
        """Maneja las pulsaciones de teclas."""
        if event.key() == Qt.Key_F11:
            if self.isFullScreen():
                self.showNormal()
            else:
                self.showFullScreen()
        else:
            super().keyPressEvent(event)
