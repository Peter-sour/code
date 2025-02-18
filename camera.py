import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # Buka kamera
if not cap.isOpened():
    print("Gagal membuka kamera.")
    exit()

ret, frame = cap.read()  # Ambil frame
if not ret:
    print("Gagal membaca frame.")
    cap.release()
    exit()

# Simpan gambar hanya jika frame tidak kosong
cv2.imwrite("foto.png", frame)  # Simpan gambar sebagai foto.png
cap.release()  # Tutup kamera
