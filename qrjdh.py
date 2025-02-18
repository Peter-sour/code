import qrcode
import base64
from PIL import Image

# Membuka file gambar dan mengonversi ke base64
file_path = "prooject1/foto3.png"
with open(file_path, "rb") as file:
    encoded_image = base64.b64encode(file.read()).decode("utf-8")

# Membuat QR Code dengan data base64 gambar
qr = qrcode.QRCode(
    version=5,  # Versi lebih tinggi untuk data lebih besar
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(encoded_image)
qr.make(fit=True)

# Membuat gambar QR Code
img = qr.make_image(fill_color="black", back_color="white")

# Menampilkan QR Code
img.show()

# Menyimpan QR Code
img.save("qr_code_base64.png")
