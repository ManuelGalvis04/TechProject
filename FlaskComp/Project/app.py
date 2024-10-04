from flask import Flask, request, render_template, send_file
import pandas as pd
import os

app = Flask(__name__)

# Ruta de la página principal donde se sube el archivo
@app.route('/')
def upload_file():
    return render_template('upload.html')

# Ruta para procesar el archivo subido
@app.route('/uploader', methods=['POST'])
def uploader():
    if 'file' not in request.files:
        return "No file part"
    
    file = request.files['file']

    if file.filename == '':
        return "No selected file"
    
    if file:
        # Guardamos el archivo temporalmente
        file_path = os.path.join('uploads', file.filename)
        file.save(file_path)
        
        # Cargar el archivo CSV o Excel
        if file.filename.endswith('.csv'):
            df = pd.read_csv(file_path, delimiter=';', encoding='latin1')
        else:
            df = pd.read_excel(file_path)
        
        # Procesar los datos (el mismo código que antes para limpiar y agrupar)
        df['VOL'] = df['VOL'].str.replace('.', '', regex=False).str.replace(',', '.').astype(float)
        df['%'] = df['%'].str.replace('.', '', regex=False).str.replace(',', '.').astype(float)
        grouped = df.groupby(['MAT', 'COD'])
        
        # Crear el texto de salida
        output_text = ""
        for (mat, cod), group in grouped:
            output_text += f"COMPUESTA {cod}-{mat} AZ\n\n"
            output_text += "TZ\tVOL\t%\tCOD\t\tMAT\t\tPAT\n"
            for _, row in group.iterrows():
                output_text += f"{(row['TZ'])}\t{row['VOL']:.2f}\t{row['%']}\t{row['COD']}\t{row['MAT']}\t{row['PAT']}\n"
            total_vol = group['VOL'].sum()
            output_text += f"\t{total_vol:.2f}\n\n"

        # Guardar el archivo de texto
        output_file_path = os.path.join('outputs', 'tabla_material_cod.txt')
        print(output_file_path, '******')
        with open(output_file_path, 'w', encoding='utf-8') as f:
            f.write(output_text)
        
        with open(output_file_path, 'r', encoding='utf-8') as f:
            processed_content = f.read()
        # Eliminar el archivo subido para no almacenar archivos innecesarios
        os.remove(file_path)
        
        # Devolver el archivo de texto generado
        # return send_file(output_file_path, as_attachment=True)
        # return "El archivo fue subido y procesado correctamente."
        return render_template('display_file.html', content=processed_content)


if __name__ == '__main__':
    # Crear las carpetas de uploads y outputs si no existen
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    if not os.path.exists('outputs'):
        os.makedirs('outputs')
    
    app.run(debug=True)
