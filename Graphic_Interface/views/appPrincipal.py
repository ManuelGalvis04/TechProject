# import sys
# import os
# from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QMessageBox, QStackedLayout
# from PyQt5.QtGui import QFont, QPixmap
# from PyQt5.QtCore import Qt

# # Lista global para almacenar los usuarios
# users = []

# class LoginWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         """Inicializa la interfaz de usuario."""
#         self.setWindowTitle('Inicio de Sesión con Microsoft')
#         self.setGeometry(100, 100, 800, 600)

#         # Configurar la imagen de fondo
#         self.imageLabel = QLabel(self)
#         image_path = os.path.abspath('./windows_logo.png')
#         pixmap = QPixmap(image_path)
#         if pixmap.isNull():
#             print(f"No se pudo cargar la imagen de la ruta: {image_path}")
#         self.imageLabel.setPixmap(pixmap)
#         self.imageLabel.setScaledContents(True)

#         # Layout principal
#         mainLayout = QStackedLayout(self)

#         # Layout para el inicio de sesión
#         loginLayout = QVBoxLayout()

#         # Configurar el ícono de usuario
#         self.userIcon = QLabel(self)
#         user_icon_path = os.path.abspath('./Graphic_Interface/file.png')
#         user_pixmap = QPixmap(user_icon_path)
#         if user_pixmap.isNull():
#             print(f"No se pudo cargar la imagen de usuario de la ruta: {user_icon_path}")
#         self.userIcon.setPixmap(user_pixmap)
#         self.userIcon.setAlignment(Qt.AlignCenter)
#         self.userIcon.setFixedSize(150, 150)
#         self.userIcon.setScaledContents(True)
#         loginLayout.addWidget(self.userIcon, alignment=Qt.AlignCenter)

#         # Añadir un espacio después de la imagen de usuario
#         loginLayout.addSpacing(20)

#         # Campo de entrada para el nombre de usuario
#         self.username = QLineEdit(self)
#         self.username.setPlaceholderText('Correo electrónico, teléfono o Skype')
#         self.username.setFont(QFont("Arial", 16))
#         self.username.setStyleSheet("""
#             QLineEdit {
#                 padding: 15px;
#                 font-size: 16px;
#                 border: 2px solid #333;
#                 border-radius: 5px;
#                 background: #fff;
#             }
#         """)
#         self.username.setFixedWidth(350)
#         loginLayout.addWidget(self.username, alignment=Qt.AlignCenter)

#         # Añadir un espacio después del campo de usuario
#         loginLayout.addSpacing(10)
        
#         # Campo de entrada para la contraseña
#         self.password = QLineEdit(self)
#         self.password.setPlaceholderText('Contraseña')
#         self.password.setFont(QFont("Arial", 16))
#         self.password.setEchoMode(QLineEdit.Password)
#         self.password.setStyleSheet("""
#             QLineEdit {
#                 padding: 15px;
#                 font-size: 16px;
#                 border: 2px solid #333;
#                 border-radius: 5px;
#                 background: #fff;
#             }
#         """)
#         self.password.setFixedWidth(350)
#         loginLayout.addWidget(self.password, alignment=Qt.AlignCenter)

#         # Añadir un espacio después del campo de contraseña
#         loginLayout.addSpacing(20)

#         # Botón de inicio de sesión
#         self.loginButton = QPushButton('Siguiente', self)
#         self.loginButton.clicked.connect(self.handleLogin)
#         self.loginButton.setFixedSize(150, 40)
#         self.loginButton.setStyleSheet("""
#             QPushButton {
#                 font-size: 16px;
#                 border-radius: 5px;
#                 background: #0078d7;
#                 color: #fff;
#             }
#             QPushButton:hover {
#                 background: #005a9e;
#             }
#         """)
#         loginLayout.addWidget(self.loginButton, alignment=Qt.AlignCenter)

#         # Conectar la tecla Enter al botón de inicio de sesión
#         self.username.returnPressed.connect(self.handleLogin)
#         self.password.returnPressed.connect(self.handleLogin)
#         self.loginButton.setDefault(True)

#         # Añadir un espacio después del botón de inicio de sesión
#         loginLayout.addSpacing(10)

#         # Enlace para recuperación de contraseña
#         self.forgotPasswordLink = QLabel("<a style='color: #ffffff' href='#'>¿Olvidaste tu contraseña?</a>", self)
#         self.forgotPasswordLink.setFont(QFont("Arial", 12))
#         self.forgotPasswordLink.setAlignment(Qt.AlignCenter)
#         self.forgotPasswordLink.setStyleSheet("""
#             QLabel {
#                 color: #ffffff;  # Cambiar el color del enlace a blanco
#             }
#             QLabel:hover {
#                 color: #cccccc;
#             }
#         """)
#         self.forgotPasswordLink.linkActivated.connect(self.openRecoveryWindow)
#         loginLayout.addWidget(self.forgotPasswordLink, alignment=Qt.AlignCenter)

#         # Añadir un espacio después del enlace de recuperación de contraseña
#         loginLayout.addSpacing(10)

#         # Enlace para crear una cuenta
#         self.createAccountLink = QLabel("<a style='color: #ffffff' href='#'>Crear una cuenta</a>", self)
#         self.createAccountLink.setFont(QFont("Arial", 12))
#         self.createAccountLink.setAlignment(Qt.AlignCenter)
#         self.createAccountLink.setStyleSheet("""
#             QLabel {
#                 color: #ffffff;  # Cambiar el color del enlace a blanco
#             }
#             QLabel:hover {
#                 color: #cccccc;
#             }
#         """)
#         self.createAccountLink.linkActivated.connect(self.openCreateAccountWindow)
#         loginLayout.addWidget(self.createAccountLink, alignment=Qt.AlignCenter)

#         # Widget de inicio de sesión
#         loginWidget = QWidget(self)
#         loginWidget.setLayout(loginLayout)
#         loginWidget.setStyleSheet("background: transparent;")
#         loginWidget.setFixedSize(450, 500)

#         # Layout para superponer el loginWidget sobre el fondo
#         overlayLayout = QVBoxLayout()
#         overlayLayout.addStretch(1)
#         overlayLayout.addWidget(loginWidget, alignment=Qt.AlignCenter)
#         overlayLayout.addStretch(1)

#         # Widget de superposición
#         overlayWidget = QWidget(self)
#         overlayWidget.setLayout(overlayLayout)

#         mainLayout.addWidget(overlayWidget)

#         self.setLayout(mainLayout)

#     def resizeEvent(self, event):
#         """Ajusta el tamaño de la imagen de fondo cuando la ventana se redimensiona."""
#         self.imageLabel.setFixedSize(self.size())

#     def handleLogin(self):
#         """Maneja el evento de inicio de sesión."""
#         username = self.username.text()
#         password = self.password.text()
#         for user in users:
#             if user['email'] == username and user['password'] == password:
#                 QMessageBox.information(self, 'Éxito', 'Inicio de sesión exitoso')
#                 return
#         QMessageBox.warning(self, 'Error', 'Nombre de usuario, correo electrónico o contraseña incorrectos')

#     def openRecoveryWindow(self):
#         """Abre la ventana de recuperación de contraseña."""
#         self.recoveryWindow = PasswordRecoveryWindow()
#         self.recoveryWindow.show()

#     def openCreateAccountWindow(self):
#         """Abre la ventana de creación de cuenta."""
#         self.createAccountWindow = CreateAccountWindow()
#         self.createAccountWindow.show()

#     def keyPressEvent(self, event):
#         """Maneja las pulsaciones de teclas."""
#         if event.key() == Qt.Key_F11:
#             if self.isFullScreen():
#                 self.showNormal()
#             else:
#                 self.showFullScreen()
#         else:
#             super().keyPressEvent(event)

# class PasswordRecoveryWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         """Inicializa la interfaz de usuario para la recuperación de contraseña."""
#         self.setWindowTitle('Recuperación de Contraseña')
#         self.setFixedSize(700, 300)  # Tamaño fijo para centrar la ventana

#         # Centrar la ventana en la pantalla
#         screen_geometry = QApplication.desktop().screenGeometry()
#         x = (screen_geometry.width() - self.width()) // 2
#         y = (screen_geometry.height() - self.height()) // 2
#         self.move(x, y)

#         layout = QVBoxLayout()

#         # Etiqueta de información
#         self.infoLabel = QLabel("Introduce tu correo electrónico para recuperar tu contraseña", self)
#         self.infoLabel.setFont(QFont("Arial", 12))
#         layout.addWidget(self.infoLabel, alignment=Qt.AlignCenter)

#         # Campo de entrada para el correo electrónico
#         self.emailInput = QLineEdit(self)
#         self.emailInput.setPlaceholderText('Correo electrónico')
#         self.emailInput.setFont(QFont("Arial", 14))
#         self.emailInput.setStyleSheet("""
#             QLineEdit {
#                 padding: 15px;
#                 font-size: 14px;
#                 border: 2px solid #333;
#                 border-radius: 5px;
#                 background: #fff;
#             }
#         """)
#         self.emailInput.setFixedWidth(300)
#         layout.addWidget(self.emailInput, alignment=Qt.AlignCenter)

#         # Botón para recuperar la contraseña
#         self.recoverButton = QPushButton('Recuperar Contraseña', self)
#         self.recoverButton.clicked.connect(self.handleRecovery)
#         self.recoverButton.setFixedSize(200, 40)
#         self.recoverButton.setStyleSheet("""
#             QPushButton {
#                 font-size: 14px;
#                 border-radius: 5px;
#                 background: #0078d7;
#                 color: #fff;
#             }
#             QPushButton:hover {
#                 background: #005a9e;
#             }
#         """)
#         layout.addWidget(self.recoverButton, alignment=Qt.AlignCenter)

#         self.setLayout(layout)

#     def handleRecovery(self):
#         """Maneja el evento de recuperación de contraseña."""
#         email = self.emailInput.text()
#         if email:
#             QMessageBox.information(self, 'Recuperación de Contraseña', f'Se ha enviado un correo de recuperación a {email}')
#             self.close()  # Cerrar la ventana después de hacer clic en OK
#         else:
#             QMessageBox.warning(self, 'Error', 'Por favor, introduce un correo electrónico válido')

# class CreateAccountWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         """Inicializa la interfaz de usuario para la creación de una cuenta."""
#         self.setWindowTitle('Crear una Cuenta')
#         self.setFixedSize(700, 400)

#         # Centrar la ventana en la pantalla
#         screen_geometry = QApplication.desktop().screenGeometry()
#         x = (screen_geometry.width() - self.width()) // 2
#         y = (screen_geometry.height() - self.height()) // 2
#         self.move(x, y)

#         layout = QVBoxLayout()

#         # Etiqueta de información
#         self.infoLabel = QLabel("Introduce los datos para crear una nueva cuenta", self)
#         self.infoLabel.setFont(QFont("Arial", 12))
#         layout.addWidget(self.infoLabel, alignment=Qt.AlignCenter)

#         # Campos de entrada para crear una cuenta
#         self.usernameInput = QLineEdit(self)
#         self.usernameInput.setPlaceholderText('Nombre de usuario')
#         self.usernameInput.setFont(QFont("Arial", 14))
#         self.usernameInput.setStyleSheet("""
#             QLineEdit {
#                 padding: 15px;
#                 font-size: 14px;
#                 border: 2px solid #333;
#                 border-radius: 5px;
#                 background: #fff;
#             }
#         """)
#         self.usernameInput.setFixedWidth(300)
#         layout.addWidget(self.usernameInput, alignment=Qt.AlignCenter)

#         self.emailInput = QLineEdit(self)
#         self.emailInput.setPlaceholderText('Correo electrónico')
#         self.emailInput.setFont(QFont("Arial", 14))
#         self.emailInput.setStyleSheet("""
#             QLineEdit {
#                 padding: 15px;
#                 font-size: 14px;
#                 border: 2px solid #333;
#                 border-radius: 5px;
#                 background: #fff;
#             }
#         """)
#         self.emailInput.setFixedWidth(300)
#         layout.addWidget(self.emailInput, alignment=Qt.AlignCenter)

#         self.passwordInput = QLineEdit(self)
#         self.passwordInput.setPlaceholderText('Contraseña')
#         self.passwordInput.setFont(QFont("Arial", 14))
#         self.passwordInput.setEchoMode(QLineEdit.Password)
#         self.passwordInput.setStyleSheet("""
#             QLineEdit {
#                 padding: 15px;
#                 font-size: 14px;
#                 border: 2px solid #333;
#                 border-radius: 5px;
#                 background: #fff;
#             }
#         """)
#         self.passwordInput.setFixedWidth(300)
#         layout.addWidget(self.passwordInput, alignment=Qt.AlignCenter)

#         # Botón para crear la cuenta
#         self.createButton = QPushButton('Crear Cuenta', self)
#         self.createButton.clicked.connect(self.handleCreateAccount)
#         self.createButton.setFixedSize(200, 40)
#         self.createButton.setStyleSheet("""
#             QPushButton {
#                 font-size: 14px;
#                 border-radius: 5px;
#                 background: #0078d7;
#                 color: #fff;
#             }
#             QPushButton:hover {
#                 background: #005a9e;
#             }
#         """)
#         layout.addWidget(self.createButton, alignment=Qt.AlignCenter)

#         self.setLayout(layout)

#     def handleCreateAccount(self):
#         """Maneja el evento de creación de cuenta."""
#         username = self.usernameInput.text()
#         email = self.emailInput.text()
#         password = self.passwordInput.text()
#         if username and email and password:
#             # Guardar el nuevo usuario en la lista
#             users.append({'username': username, 'email': email, 'password': password})
#             QMessageBox.information(self, 'Cuenta Creada', f'Se ha creado una nueva cuenta para {email}')
#             self.close()  # Cerrar la ventana después de hacer clic en OK
#         else:
#             QMessageBox.warning(self, 'Error', 'Por favor, rellena todos los campos')

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = LoginWindow()
#     window.show()
#     sys.exit(app.exec_())
