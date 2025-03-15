from database import get_db_connection
import pyodbc
def create_user(username, email, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        # Verificar si el correo electrónico ya existe
        cursor.execute("SELECT 1 FROM UserCredentials WHERE Email = ?", email)
        if cursor.fetchone():
            return False, "El correo electrónico ya está registrado."

        # Crear la cuenta de usuario
        cursor.execute("EXEC CreateUserAccount ?, ?, ?", username, email, password)
        conn.commit()
        return True, "Cuenta creada exitosamente."
    except pyodbc.IntegrityError as e:
        # Manejo de excepciones de integridad (por ejemplo, duplicados)
        if e.args[0] == '23000':
            return False, "El correo electrónico ya está registrado."
        else:
            return False, "Error al crear la cuenta."
    except Exception as e:
        return False, f"Error inesperado: {e}"
    finally:
        conn.close()
