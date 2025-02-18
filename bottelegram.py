from telegram import Update
from telegram.ext import Application, MessageHandler, CommandHandler, CallbackContext, filters
from telegram.ext.filters import Regex
from fuzzywuzzy import fuzz
import string
import pywhatkit
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import re
import pywhatkit as kit

# Daftar kata valid untuk typo detection
valid_words = ["halo", "hai", "selamat", "pagi", "siang", "malam", "start", "selesai", "terima kasih"]

# Fungsi untuk mendeteksi typo dan memberikan saran
async def handle_message(update: Update, context: CallbackContext) -> None:
    text = update.message.text.lower().translate(str.maketrans('', '', string.punctuation))

    best_match = None
    highest_score = 0
    for word in valid_words:
        score = fuzz.ratio(text, word)
        if score > highest_score:
            highest_score = score
            best_match = word

    if best_match and highest_score > 70:
        await update.message.reply_text(f"Apakah yang Anda maksud '{best_match}'?")

# Fungsi untuk perintah /start
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Halo! Selamat datang di coffe_bot, ketik <b>lanjut</b> untuk melanjutkan",parse_mode='HTML')

# Fungsi untuk perintah /pesan
async def pesan(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(
        "Silahkan kirim pesan dengan format dibawah\nSalin semua isi format dibawah ini dengan menyertakan '/format' kemudian isi dengan sesuai"
    )
    await update.message.reply_text(
        "/format\n nama : abcdefgij\n nomor wa : 08123456789\n pesanan : Milk Coffe dan Coffe with Strawberry"
    )

# Fungsi untuk perintah /format
DEFAULT_CONTACT = "+6285230070232"  # Nomor WhatsApp default
async def send_message(update: Update, context: CallbackContext) -> None:
    args = context.args
    contact = DEFAULT_CONTACT
    message = " ".join(args) if args else "Pesan default dari bot."

    try:
        pywhatkit.sendwhatmsg_instantly(contact, message, wait_time=10)
        user_name = update.message.from_user.username
        await update.message.reply_text(f"kirim kembali format tersebut tanpa menyertakan '/format'\nTerimakasih @{user_name} untuk pesanan anda\nkami akan segera menghubungi anda jika pesanan siap \U0001F604\nTerimakasih telah menghubungi <b>coffe_bot</b>\U0001F609",parse_mode='HTML')
        await update.message.reply_text("kirim <b>home</b> untuk kembali ke menu awal", parse_mode='HTML')
    except Exception as e:
        await update.message.reply_text(f"Gagal mengirim pesan: {e}")

# Fungsi untuk menangani menu "lanjut"
async def handle_lanjut(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(
        "Silahkan pilih menu berikut:\n1. Tampilkan gambar menu\n2. Pesan menu\nKirim angka <b>1</b> atau <b>2</b> untuk melanjutkan.",
        parse_mode='HTML'
    )
    await update.message.reply_text("kirim <b>home</b> jika ingin kembali ke menu awal", parse_mode='HTML')

# Fungsi untuk menu 1
async def handle_menu1(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(
        "Menu:\nA. Milk Coffee Picture\nB. Coffee with Strawberry Flavored Picture\nkirim <b>a</b> atau <b>b</b> untuk melanjutkan",
        parse_mode='HTML'
    )
    await update.message.reply_text("kirim <b>home</b> jika ingin kembali ke menu awal", parse_mode='HTML')

# Fungsi untuk menu 2
async def handle_menu2(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Silahkan pilih pesanan berikut:\n1. Milk Coffee Rp.5000\n2. Coffee with Strawberry Flavored Rp.6500\ntekan /pesan untuk memesan")
    await update.message.reply_text("kirim <b>home</b> jika ingin kembali ke menu awal", parse_mode='HTML')

# Fungsi untuk menampilkan gambar menu
async def handle_foto1(update: Update, context: CallbackContext) -> None:
    text = update.message.text.lower()
    if text == "a":
        try:
            with open("prooject1/foto1.png", "rb") as image_file:
                await update.message.reply_photo(photo=image_file, caption="Milk Coffee.")
                await update.message.reply_text("kirim <b>home</b> jika ingin kembali ke menu awal", parse_mode='HTML')
        except Exception as e:
            await update.message.reply_text(f"Gagal mengirim gambar: {e}")
            await update.message.reply_text("kirim <b>home</b> untuk kembali ke menu awal", parse_mode='HTML')
    elif text == "b":
        try:
            with open("prooject1/foto2.png", "rb") as image_file:
                await update.message.reply_photo(photo=image_file, caption="Coffee with Strawberry Flavored.")
                await update.message.reply_text("kirim <b>home</b> jika ingin kembali ke menu awal", parse_mode='HTML')
        except Exception as e:
            await update.message.reply_text(f"Gagal mengirim gambar: {e}")
            await update.message.reply_text("kirim <b>home</b> untuk kembali ke menu awal", parse_mode='HTML')

# Fungsi untuk kembali ke menu awal
async def handle_menu(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(
        "Silahkan pilih menu berikut:\n1. Tampilkan gambar menu\n2. Pesan menu\nKirim angka <b>1</b> atau <b>2</b> untuk melanjutkan.",
        parse_mode='HTML'
    )
# Fungsi untuk mendeteksi nomor telepon dalam pesan
async def handle_message(update: Update, context: CallbackContext) -> None:
    text = update.message.text
    name, order = extract_info(text) #ekstrak informasi
    # Regex untuk mendeteksi nomor telepon
    phone_match = re.search(r'(\+62|62|0)[0-9]{9,13}', text)
    if phone_match:
        phone_number = phone_match.group()
        message = f"Terimakasih {name}\ndengan pesanan {order}\nMohon menunggu, pesanan anda sedang diproses!!\U0001F604"
        # await update.message.reply_text(f"Nomor terdeteksi: {phone_number}. ")
        await update.message.reply_text("Terimakasih untuk pesanan anda \U0001F604\nMohon tunggu sebentar ya")
        
        # Kirim pesan WhatsApp
        try:
            # send_whatsapp_message(phone_number, message)
            pywhatkit.sendwhatmsg_instantly(phone_number, message, wait_time=10)
            await update.message.reply_text(f"Pesan berhasil dikirim ke {phone_number}.")
            await update.message.reply_text("kirim <b>home</b> untuk kembali ke menu awal", parse_mode='HTML')
        except Exception as e:
            await update.message.reply_text(f"Gagal mengirim pesan: {e}")
    else:
        await update.message.reply_text("Tidak ada nomor telepon yang valid dalam pesan.")

def send_whatsapp_message(phone_number, message):
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Jalankan di background
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    
    driver = webdriver.Chrome(options=chrome_options)
    
    try:
        # Kirim pesan WhatsApp
        kit.sendwhatmsg_instantly(phone_number, message, wait_time=10)
        time.sleep(5)  # Tunggu beberapa detik agar proses selesai
    finally:
        driver.quit()
# Fungsi untuk mengirim pesan menggunakan Selenium dan pywhatkit
def send_whatsapp_message(phone_number, message):
    # Setup Selenium untuk headless
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Headless mode
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")

    # Jalankan driver dengan opsi headless
    driver = webdriver.Chrome(options=chrome_options)

    # Kirim pesan WhatsApp menggunakan pywhatkit (browser tetap berjalan di background)
    pywhatkit.sendwhatmsg_instantly("+6285230070232", "Pesan default", wait_time=10)

    # Jangan lupa untuk menutup driver setelah selesai
    time.sleep(5)  # Tunggu beberapa detik sebelum menutup
    driver.quit()

def extract_info(text):
    # Pola regex untuk nama, nomor WhatsApp, dan pesanan
    name_pattern = r"nama\s*:\s*(.+)"
    order_pattern = r"pesanan\s*:\s*(.+)"
    
    # Ekstraksi nama
    name_match = re.search(name_pattern, text, re.IGNORECASE)
    name = name_match.group(1).strip() if name_match else "Nama tidak ditemukan"
    
    # Ekstraksi pesanan
    order_match = re.search(order_pattern, text, re.IGNORECASE)
    order = order_match.group(1).strip() if order_match else "Pesanan tidak ditemukan"
    
    return name, order


# Fungsi utama
def main():
    token = "7555000051:AAEWgXB-E9vFzEB_GqwqT7HrzmhBK_ZPo2A"
    application = Application.builder().token(token).build()

    # Tambahkan handler
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("pesan", pesan))
    application.add_handler(CommandHandler("format", send_message))
    application.add_handler(MessageHandler(Regex("^(1)$"), handle_menu1))
    application.add_handler(MessageHandler(Regex("^(2)$"), handle_menu2))
    application.add_handler(MessageHandler(Regex("^(lanjut|Lanjut)$"), handle_lanjut))
    application.add_handler(MessageHandler(Regex("^(a|b|A|B)$"), handle_foto1))
    application.add_handler(MessageHandler(Regex("^(home|Home)$"), handle_menu))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Jalankan bot
    application.run_polling()

if __name__ == "__main__":
    main()
