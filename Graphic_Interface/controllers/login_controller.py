from database import get_db_connection


def authenticate_user(email, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("EXEC ValidateUserLogin @Email=?, @Password=?", email, password)
    result = cursor.fetchone()
    conn.close()
    return result is not None and result.Result == 'Login Successful'
