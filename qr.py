import qrcode
import base64
from PIL import Image

# Data yang ingin dimasukkan ke dalam QR Code
data = "https://malak.it.student.pens.ac.id"

# Membuat objek QR Code
qr = qrcode.QRCode(
    version=1,  # Menentukan ukuran QR Code
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Tingkat koreksi kesalahan
    box_size=10,  # Ukuran setiap kotak dalam QR Code
    border=4,  # Lebar border
)

# Menambahkan data ke dalam QR Code
qr.add_data(data)
qr.make(fit=True)

# Membuat gambar dari QR Code
img = qr.make_image(fill='black', back_color='white')

# Menyimpan gambar QR Code ke file
img.save("qrcode.png")

print("kode QR berhasil dibuat")
