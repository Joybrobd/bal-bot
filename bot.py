import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Replace these with your own Bot Token and Movider credentials
BOT_TOKEN = '7783866404:AAFXWzKeCFXxd20quEa191cz1cxm3pYH0wU'
API_KEY = '2gDVUCVlFBq2HCP5xuBs1eLBbTB'
API_SECRET = 'UNDn7dpkI8ugAhRyYK7DioDUW3kyhqdVLT38IKyk'
FROM = 'MOVIDER'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome! Use /sms <number> <message> to send an SMS.")

async def send_sms(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) < 2:
        await update.message.reply_text("Usage: /sms <number> <message>")
        return

    number = context.args[0]
    message = ' '.join(context.args[1:])

    # Sending SMS via Movider API
    response = requests.post("https://api.movider.co/v1/sms", data={
        'to': number,
        'text': message,
        'api_key': API_KEY,
        'api_secret': API_SECRET,
        'from': FROM
    })

    if response.status_code == 200:
        await update.message.reply_text(f"SMS sent to {number}!")
    else:
        await update.message.reply_text("Failed to send SMS. Check logs.")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("sms", send_sms))
    app.run_polling()

if __name__ == "__main__":
    main()
