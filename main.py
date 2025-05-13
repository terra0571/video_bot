from pyrogram import Client, filters
from downloader import download_youtube_video
import os

# Telegram API ma'lumotlari (Siz taqdim etgan)
API_ID = 27941617
API_HASH = "732e799ff25d34b1b41842216a8aa5cf"
BOT_TOKEN = "7496406827:AAFBf0dXknanmHizdIHgDE_hiJIEapzKmzw"

# Botni yaratamiz
app = Client("video_downloader_bot",
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN)

# /start buyrug'i uchun handler
@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text("👋 Salom! YouTube havolasini yuboring, men sizga videoni yuklab beraman.")

# YouTube havola qabul qilish va video jo‘natish
@app.on_message(filters.text & ~filters.command("start"))
async def handle_url(client, message):
    url = message.text.strip()
    await message.reply_text("⏳ Yuklab olinmoqda...")

    try:
        video_path, title = download_youtube_video(url)
        await message.reply_video(video_path, caption=f"✅ Yuklandi: {title}")
        os.remove(video_path)
    except Exception as e:
        await message.reply_text(f"❌ Xatolik: {e}")

# Botni ishga tushiramiz
app.run()
