from tkinter import messagebox

class RecoveryController:
    def __init__(self, view):
        self.view = view

    def handleRecovery(self):
        """Maneja el evento de recuperación de contraseña."""
        email = self.view.get_email()
        if email:
            # Aquí puedes agregar la lógica para enviar un correo de recuperación
            messagebox.showinfo('Recuperación de Contraseña', f'Se ha enviado un correo de recuperación a {email}')
            self.view.window.destroy()
        else:
            messagebox.showwarning('Error', 'Por favor, introduce un correo electrónico válido')
