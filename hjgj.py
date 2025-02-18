from telegram import Update
from telegram.ext import Application, MessageHandler, CommandHandler, filters, CallbackContext
from fuzzywuzzy import fuzz
import string
import pywhatkit

# Daftar kata valid untuk typo detection
valid_words = ["halo", "hai", "selamat", "pagi", "siang", "malam", "start", "selesai", "terima kasih"]

# Fungsi untuk menangani pesan dan mendeteksi typo
async def handle_message(update: Update, context: CallbackContext) -> None:
    if update.message:
        text = update.message.text.lower()
        text = text.translate(str.maketrans('', '', string.punctuation))

        best_match = None
        highest_score = 0
        for word in valid_words:
            score = fuzz.ratio(text, word)
            if score > highest_score:
                highest_score = score
                best_match = word

        if best_match and highest_score > 70:
            await update.message.reply_text(f"Apakah yang Anda maksud '{best_match}'?")

# Fungsi untuk menangani pesan "start"
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Halo! Selamat datang. Ketik /send untuk mengirim pesan ke WhatsApp.")

# Fungsi untuk mengirim pesan ke WhatsApp
DEFAULT_CONTACT = "+6285230070232"  # Nomor WhatsApp yang akan dihubungi
async def send_message(update: Update, context: CallbackContext) -> None:
    args = context.args
    contact = DEFAULT_CONTACT  # Gunakan nomor default
    message = " ".join(args) if args else "Pesan default dari bot."

    try:
        pywhatkit.sendwhatmsg_instantly(contact, message, wait_time=10)
        await update.message.reply_text("Terima kasih atas pesanan anda, Kami akan menghubungi anda sesaat lagi")
    except Exception as e:
        await update.message.reply_text(f"Terjadi kesalahan saat mengirim pesan: {e}")

# Fungsi untuk menangani pesan "lanjut"
async def handle_lanjut(update: Update, context: CallbackContext) -> None:
    if update.message and update.message.text.lower() == "lanjut":
        await update.message.reply_text("Silahkan pilih menu berikut \n 1. Tampilkan gambar menu \n 2. pesan menu \n silahkan kirim contoh <b>1</b> untuk lanjut ", parse_mode='HTML')

# Fungsi menampilkan menu 1
async def handle_menu1(update: Update, context: CallbackContext) -> None:
    if update.message:
        text = update.message.text.lower().strip()
        user_name = update.message.from_user.username
        user_phone = update.message.contact.phone_number if update.message.contact else "No phone number provided"
        
        print(f"- Pesan diterima dari User: {user_name} \n- Nomor Telepon Pengguna: {user_phone} \n- Menu yang dipilih: '{text}' \n")

        if text == "1":
            await update.message.reply_text("Menu:\n a. Milk Coffe Picture \n b. Coffe With Strawberry Flavored Picture\n")
            await update.message.reply_text("kirim <b>home</b> jika ingin kembali ke menu awal", parse_mode='HTML')

# Fungsi menampilkan menu
async def handle_menu(update: Update, context: CallbackContext) -> None:
    if update.message:
        text = update.message.text.lower().strip()
        user_name = update.message.from_user.username
        user_phone = update.message.contact.phone_number if update.message.contact else "No phone number provided"
        
        print(f"- Pesan diterima dari User: {user_name} \n- Nomor Telepon Pengguna: {user_phone} \n- Menu yang dipilih: '{text}' \n")

        if text == "home":
            await update.message.reply_text("Silahkan pilih menu berikut \n 1. Tampilkan gambar menu \n 2. pesan menu \n", parse_mode='HTML')

# Fungsi menampilkan menu 2
async def handle_menu2(update: Update, context: CallbackContext) -> None:
    if update.message and update.message.text.lower() == "2":
        await update.message.reply_text("Silahkan Pilih Menu Dibawah :\n 1. Milk Coffe\n 2. Coffe With Strawberry Flavored\n")

# Fungsi menampilkan gambar
async def handle_foto1(update: Update, context: CallbackContext) -> None:
    if update.message:
        text = update.message.text.lower().strip()
        print(f"Teks yang diterima: '{text}'")  # Log untuk debugging

        if text == "a":
 try:
                with open("prooject1/foto1.png", "rb") as image_file:
                    await update.message.reply_photo(photo=image_file, caption="ini adalah gambar kopi susu")
            except Exception as e:
                print(f"Error: {e}")  # Log error
                await update.message.reply_text(f"Gagal mengirim gambar: {e}")
        elif text == "b":
            try:
                with open("prooject1/foto2.png", "rb") as image_file:
                    await update.message.reply_photo(photo=image_file, caption="ini adalah gambar kopi susu campuran strawberi")
            except Exception as e:
                print(f"Error: {e}")  # Log error
                await update.message.reply_text(f"Gagal mengirim gambar: {e}")

# Fungsi untuk menangani pesan "hai"
async def handle_hai(update: Update, context: CallbackContext) -> None:
    if update.message and update.message.text.lower() == "hai":
        await update.message.reply_text("Apa kabar?")

# Fungsi utama untuk menjalankan bot
def main():
    token = "7555000051:AAEWgXB-E9vFzEB_GqwqT7HrzmhBK_ZPo2A"  # Ganti dengan token bot Anda
    application = Application.builder().token(token).build()

    # Tambahkan handler
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("send", send_message))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    application.add_handler(MessageHandler(filters.TEXT & filters.Regex('^(a|b)$'), handle_foto1))
    application.add_handler(MessageHandler(filters.TEXT & filters.Regex('^home$'), handle_menu))
    application.add_handler(MessageHandler(filters.TEXT & filters.Regex('^hai$'), handle_hai))
    application.add_handler(MessageHandler(filters.TEXT & filters.Regex('^1$'), handle_menu1))
    application.add_handler(MessageHandler(filters.TEXT & filters.Regex('^2$'), handle_menu2))
    application.add_handler(MessageHandler(filters.TEXT & filters.Regex('^lanjut$'), handle_lanjut))

    # Jalankan bot
    application.run_polling()

if __name__ == "__main__":
    main()