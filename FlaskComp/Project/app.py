from flask import Flask, request, render_template, session, send_file
from flask_mail import Mail, Message
import pandas as pd
import os
import uuid

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Configuración del servidor de correo
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Puedes cambiar esto a Outlook si es necesario
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'usuariocorreo@gmail.com'
app.config['MAIL_PASSWORD'] = 'contraseñausuario'

mail = Mail(app)

# Ruta de la página principal donde se sube el archivo
@app.route('/')
def upload_file():
    return render_template('upload.html')

# Ruta para procesar el archivo subido y mostrar el texto procesado
@app.route('/uploader', methods=['POST'])
def uploader():
    if 'file' not in request.files:
        return "No se ha seleccionado ningún archivo."
    
    file = request.files['file']

    if file.filename == '':
        return "No se ha seleccionado ningún archivo."
    
    semana = request.form.get('semana')  # Obtener la semana del formulario
    session['semana'] = semana  # Almacenar la semana en la sesión

    if file:
        # Cargar el archivo CSV o Excel
        if file.filename.endswith('.csv'):
            df = pd.read_csv(file, delimiter=';', encoding='latin1')
        else:
            df = pd.read_excel(file)

        # Procesar los datos
        df['VOL'] = df['VOL'].str.replace('.', '', regex=False).str.replace(',', '.').astype(float)
        df['%'] = df['%'].str.replace('.', '', regex=False).str.replace(',', '.').astype(float)


         # Asegurarse de que TZ se maneje como texto
        df['TZ'] = df['TZ'].astype(str)  # Convertir a string
        grouped = df.groupby(['MAT', 'COD'])

        # Crear el texto de salida
        output_text = "Cordial saludo, \nPor favor enviar las siguientes compuestas para AZUFRE con SGS.\n\n"
        for (mat, cod), group in grouped:
            output_text += f"COMPUESTA {cod}-{mat} AZ\n\n"
            output_text += "TZ\tVOL\t%\tCOD\t\tMAT\t\tPAT\n"
            for _, row in group.iterrows():
                output_text += f"{(row['TZ'])}\t{row['VOL']:.2f}\t{row['%']}\t{row['COD']}\t{row['MAT']}\t{row['PAT']}\n"
            total_vol = group['VOL'].sum()
            output_text += f"\t{total_vol:.2f}\n\n"

        # Guardar el texto en un archivo temporal
        if not os.path.exists('outputs'):
            os.makedirs('outputs')
        
        file_name = f"output_{uuid.uuid4().hex}.txt"  # Crear un nombre de archivo único
        file_path = os.path.join('outputs', file_name)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(output_text)

        # Variables de correo dinámicas
        from_email = app.config['MAIL_USERNAME']
        to_email = request.form.get('email', 'correodestinatario@gmail.com')  # Por defecto un destinatario si no se ha proporcionado
        subject = f"Compuestas de AZUFRE - {file_name}"

        # Pasar todas las variables a la plantilla HTML
        return render_template('display_file.html', 
                               file_name=file_name, 
                               content=output_text,
                               from_email=from_email,
                               to_email=to_email,
                               subject=subject)

# Ruta para enviar el correo con el contenido procesado
# @app.route('/send_email', methods=['POST'])
# def send_email():
#     to_email = request.form['email']
#     file_name = request.form['file_name']  # Recuperar el nombre del archivo del formulario

#     file_path = os.path.join('outputs', file_name)
#     if not os.path.exists(file_path):
#         return "El archivo no existe."

#     with open(file_path, 'r', encoding='utf-8') as f:
#         content = f.read()

#     msg = Message('Archivo generado', sender=app.config['MAIL_USERNAME'], recipients=[to_email])
#     msg.body = content
#     mail.send(msg)

#     return "Correo enviado correctamente."

# Ruta para enviar el correo con el contenido procesado
@app.route('/send_email', methods=['POST'])
def send_email():
    # Destinatario estático
    to_email = 'correodestinatario@gmail.com'
    
    file_name = request.form['file_name']  # Recuperar el nombre del archivo del formulario
    file_path = os.path.join('outputs', file_name)
    
    if not os.path.exists(file_path):
        return "El archivo no existe."

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    semana = session.get('semana', 'desconocida')  # Recuperar la semana de la sesión, con un valor por defecto

    # Enviar el correo con el contenido procesado
    msg = Message(f'SGS COMPUESTA SEMANA {semana}', sender=app.config['MAIL_USERNAME'], recipients=[to_email])
    msg.body = content
    mail.send(msg)

    return "Correo enviado correctamente."


if __name__ == '__main__':
    # app.secret_key = 'your_secret_key'
    app.run(debug=True)
