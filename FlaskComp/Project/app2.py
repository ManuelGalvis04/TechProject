import os
import pandas as pd
import win32com.client as win32
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# Ruta principal para mostrar el formulario de subida
@app.route('/')
def upload_file():
    return render_template('upload.html')

# Ruta para procesar el archivo subido y enviar el correo
@app.route('/uploader', methods=['POST'])
def uploader():
    if 'file' not in request.files:
        return "No se seleccionó ningún archivo."
    
    file = request.files['file']

    if file.filename == '':
        return "El archivo no tiene nombre."

    # Crear carpeta de uploads si no existe
    uploads_dir = 'uploads'
    if not os.path.exists(uploads_dir):
        os.makedirs(uploads_dir)

    # Guardar el archivo temporalmente
    file_path = os.path.join(uploads_dir, file.filename)
    file.save(file_path)

    # Crear carpeta de outputs si no existe
    outputs_dir = 'outputs'
    if not os.path.exists(outputs_dir):
        os.makedirs(outputs_dir)

    # Procesar el archivo y generar el cuerpo del correo
    processed_file_path = os.path.join(outputs_dir, 'archivo_procesado.txt')
    output_text = process_file(file_path)

    # Guardar el texto procesado en un archivo
    with open(processed_file_path, 'w', encoding='utf-8') as f:
        f.write(output_text)

    # Enviar el correo
    recipient_email = 'galvismanuel208@gmail.com'  # Cambia esto por el email del destinatario
    subject = 'COMPUESTA SGS SEMANA 58'  # Asunto del correo
    send_email_with_outlook(processed_file_path, recipient_email, subject)

    return "El archivo ha sido procesado y el correo ha sido enviado."

# Función para procesar el archivo y generar el cuerpo del correo
def process_file(file_path):
    # Cargar el archivo CSV o Excel
    if file_path.endswith('.csv'):
        df = pd.read_csv(file_path, delimiter=';', encoding='latin1')
    elif file_path.endswith('.xlsx'):
        df = pd.read_excel(file_path)
    else:
        return "Formato de archivo no soportado."

    # Limpiar los datos
    df['VOL'] = df['VOL'].str.replace('.', '', regex=False).str.replace(',', '.').astype(float)
    df['%'] = df['%'].str.replace('.', '', regex=False).str.replace(',', '.').astype(float)

    # Agrupar por 'MAT' y 'COD'
    grouped = df.groupby(['MAT', 'COD'])
    output_text = ""

    for (mat, cod), group in grouped:
        output_text += f"COMPUESTA {cod}-{mat} AZ\n\n"
        output_text += f"{'TZ'.center(10)}{'VOL'.center(10)}{'%'.center(10)}{'COD'.center(10)}{'MAT'.center(15)}{'PAT'.center(10)}\n"

        for _, row in group.iterrows():
            output_text += f"{str(row['TZ']).center(10)}{f'{row['VOL']:.2f}'.center(10)}{f'{row['%']}'.center(10)}{str(row['COD']).center(10)}{str(row['MAT']).center(15)}{str(row['PAT']).center(10)}\n"

        total_vol = group['VOL'].sum()
        output_text += f"{'Total'.center(10)}{f'{total_vol:.2f}'.center(10)}\n\n"

    return output_text

# Función para enviar el correo con el contenido del archivo .txt
def send_email_with_outlook(file_path, recipient_email, subject):
    # Inicializar la aplicación de Outlook
    outlook = win32.Dispatch('outlook.application')
    
    # Crear un nuevo mensaje
    mail = outlook.CreateItem(0)
    
    # Establecer el destinatario
    mail.To = recipient_email
    
    # Asunto del correo
    mail.Subject = subject
    
    # Leer el contenido del archivo .txt
    with open(file_path, 'r', encoding='utf-8') as f:
        file_content = f.read()
    
    # Establecer el cuerpo del mensaje con el contenido del archivo
    mail.Body = file_content
    
    # Enviar el correo directamente
    mail.Send()

# Inicializar la aplicación
if __name__ == '__main__':
    app.run(debug=True)
