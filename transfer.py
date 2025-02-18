import qrcode

nomor_va = "5801610024934"

url_transfer = f"https://www.btn.co.id/transfer?rek={nomor_va}"

qr = qrcode.QRCode(
    version=1,  # Menentukan ukuran QR Code
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Tingkat koreksi kesalahan
    box_size=10,  # Ukuran setiap kotak dalam QR Code
    border=4,  # Lebar border
)

qr.add_data(url_transfer)
qr.make(fit=True)

# Membuat gambar dari QR Code
img = qr.make_image(fill='black', back_color='white')

# Menyimpan gambar QR Code ke file
img.save("qrcode.png")

print(" QR Code pembayaran BTN berhasil dibuat!")
