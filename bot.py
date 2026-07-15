from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = "8713102553:AAHxj2VJpJzna9UpoC6A0Y_YCcISxWxEquw" 

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Pocket Signal AI is online!\n\nUse /signal to receive a trading signal."
    )

async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📈 Demo Signal\n\nPair: EUR/USD\nDirection: BUY\nTimeframe: 5 Minutes"
    )

app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("signal", signal))

print("Pocket Signal AI is running...")
app.run_polling()
