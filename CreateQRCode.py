import qrcode

def generate_qr_code(data, output_file):
    # Crear una instancia de QRCode
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    # Agregar los datos al QRCode
    qr.add_data(data)
    qr.make(fit=True)

    # Crear la imagen del QRCode
    img = qr.make_image(fill_color="black", back_color="white")

    # Guardar la imagen
    img.save(output_file)
    print(f"Código QR guardado como {output_file}")

# Ejemplo de uso
data = "https://www.example.com"  # Cambia esto por los datos que quieras codificar
output_file = "codigo_qr.png"  # Cambia esto por la ruta donde quieras guardar el QR
generate_qr_code(data, output_file)
