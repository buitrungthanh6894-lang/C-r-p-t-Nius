import os
from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# 1. Lấy token trực tiếp từ Environment Variables của Render
BOT_TOKEN = os.environ.get("BOT_TOKEN")

# 2. Khởi tạo Flask App
flask_app = Flask(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🚀 Crypto News AI\n\nBot đã hoạt động thành công!")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Các lệnh hiện có:\n/start\n/help")

# Thêm handler cho bot
bot_app.add_handler(CommandHandler("start", start))
bot_app.add_handler(CommandHandler("help", help_command))

# 3. Tạo route Webhook cho Flask
@flask_app.route('/', methods=['POST', 'GET'])
async def webhook():
    if request.method == 'POST':
        # Xử lý tin nhắn đến từ Telegram
        update = Update.de_json(request.get_json(force=True), bot_app.bot)
        await bot_app.process_update(update)
        return "OK", 200
    return "Bot is running!", 200

if __name__ == "__main__":
    # 4. Chạy Flask server trên port Render yêu cầu (mặc định 10000)
    port = int(os.environ.get("PORT", 10000))
    flask_app.run(host="0.0.0.0", port=port)
