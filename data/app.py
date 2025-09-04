# install dulu library ini (di terminal atau di replit):
# pip install python-telegram-bot

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Ganti dengan token dari @BotFather
TOKEN = "MASUKKAN_TOKEN_BOT_KAMU_DI_SINI"

# Fungsi yang akan dijalankan ketika user ketik /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Halo! Bot ini sudah aktif. 🚀")

# Jalankan bot
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("Bot berjalan...")
app.run_polling()

