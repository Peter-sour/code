from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, MessageHandler, CommandHandler, filters, CallbackContext
from fuzzywuzzy import fuzz
import string
import pywhatkit

# Daftar kata valid untuk typo detection
valid_words = ["halo", "hai", "selamat", "pagi", "siang", "malam", "start", "selesai", "terima kasih"]

# Fungsi untuk menangani pesan dan mendeteksi typo
async def handle_message(update: Update, context: CallbackContext) -> None:
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
DEFAULT_CONTACT = "+6285230070232"
async def send_message(update: Update, context: CallbackContext) -> None:
    args = context.args
    contact = "DEFAULT_CONTACT"
    message = "".join(args) if args else "Pesan default dari bot. "
    try:
        pywhatkit.sendwhatmsg_instantly(contact, message)
        await update.message.reply_text(f"Pesan ke {contact} berhasil dikirim.")
    except Exception as e:
        await update.message.reply_text(f"Terjadi kesalahan saat mengirim pesan: {e}")
        
# Fungsi utama untuk menjalankan bot
def main():
    token = "7555000051:AAEWgXB-E9vFzEB_GqwqT7HrzmhBK_ZPo2A"  # Ganti dengan token bot Anda
    application = Application.builder().token(token).build()

    # Tambahkan handler
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("send", send_message))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Jalankan bot
    application.run_polling()

if __name__ == "__main__":
    main()
