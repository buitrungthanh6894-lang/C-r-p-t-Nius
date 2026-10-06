from dotenv import load_dotenv
load_dotenv()

from rss import latest_news
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from config import BOT_TOKEN
from onchain import get_onchain
from rugpull import get_rugpull
from meme import get_meme
from newmeme import get_new_memes
from trending import get_trending
from market import get_market
from fear import get_fear

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🚀 Bot hoạt động!")

async def onchain(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(get_onchain())

async def rug(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(get_rugpull())

async def meme(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(get_meme())

async def newmeme(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(get_new_memes())

async def trending(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(get_trending())

async def market(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(get_market())

async def fear(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(get_fear())

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📚 Các lệnh:\n"
        "/start - Khởi động bot\n"
        "/help - Trợ giúp\n"
        "/news - Tin crypto mới nhất\n"
        "/onchain - Dữ liệu On-chain"
        "/rug - Hack & Rugpull\n"
        "/meme - Memecoin nổi bật\n"
        "/newmeme - New Memecoin\n"
        "/market - Tổng quan thị trường\n"
        "/fear - Fear & Greed"
    )


async def news(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        news = latest_news()

        if not news:
            await update.message.reply_text("📭 Hiện chưa có tin nổi bật.")
            return

        message = "🚨 HOT CRYPTO NEWS\n\n"

        for item in news:
            message += f"📰 {item['title']}\n"
            message += f"🔗 {item['link']}\n\n"

        await update.message.reply_text(message)

    except Exception as e:
        await update.message.reply_text(f"Lỗi: {e}")
        print(e)

async def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("news", news))
    app.add_handler(CommandHandler("onchain", onchain))
    app.add_handler(CommandHandler("rug", rug))
    app.add_handler(CommandHandler("meme", meme))
    app.add_handler(CommandHandler("newmeme", newmeme))
    app.add_handler(CommandHandler("trending", trending))
    app.add_handler(CommandHandler("market", market))
    app.add_handler(CommandHandler("fear", fear))
    print("✅ Bot is running...")

    async with app:
        await app.start()
        await app.updater.start_polling()

        while True:
            await asyncio.sleep(1)


if __name__ == "__main__":
    asyncio.run(main())