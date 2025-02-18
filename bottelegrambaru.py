from telegram import Update
from telegram.ext import Application, MessageHandler, CommandHandler, filters, CallbackContext
from telegram.ext.filters import Regex
from fuzzywuzzy import fuzz
import string
import pywhatkit

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

#fungsi untuk memesan
async def pesan(update: Update, context: CallbackContext) ->None:
    await update.message.reply_text(
        "silahkan kirim pesan dengan format dibawah\nSalin semua isi format dibawah ini termasuk '/format' kemudian isi dengan sesuai"
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
        await update.message.reply_text(f"Terimakasih @{user_name} untuk pesanan anda\nkami akan segera menghubungi anda jika pesanan siap \U0001F604\nTerimakasih telah menghubungi <b>coffe_bot</b>\U0001F609",parse_mode='HTML')
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
    # await update.message.reply_text(
    #     "jika anda ingin memesan menu diatas\n silahkan kirim pesan dengan format dibawah\nSalin format dibawah ini lalu isi dengan sesuai"
    # )
    # await update.mesage.reply_text(
    #     "/format\n nama : abcdefgij\n nomor wa : 08123456789\n pesanan : Milk Coffe dan Coffe with Strawberry"
    # )
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
