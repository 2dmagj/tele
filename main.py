import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, ContextTypes, filters
import yt_dlp
from flask import Flask, request

BOT_TOKEN = os.environ.get("TOKEN")
APP_URL = os.environ.get("APP_URL")  # رابط Railway الكامل

app = Flask(__name__)
user_data = {}

def get_video_formats(url):
    ydl_opts = {'quiet': True, 'no_warnings': True}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
    formats = info.get('formats', [])
    filtered_formats = [
        f for f in formats
        if f.get('ext') in ('mp4', 'webm') and f.get('acodec') != 'none' and f.get('vcodec') != 'none'
    ]
    filtered_formats.sort(key=lambda x: x.get('height', 0), reverse=True)
    return filtered_formats

def download_video(url, format_id):
    ydl_opts = {
        'format': format_id,
        'outtmpl': 'downloads/%(title)s.%(ext)s',
        'quiet': True,
        'no_warnings': True,
        'noplaylist': True
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)
    return filename

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 مرحباً! أرسل رابط فيديو، واختر الجودة.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text
    await update.message.reply_text("🔍 جاري جلب خيارات الجودة...")
    try:
        formats = get_video_formats(url)
        if not formats:
            await update.message.reply_text("❌ لا توجد جودات مناسبة (mp4 أو webm).")
            return
        buttons = []
        for f in formats[:8]:
            label = f"{f.get('height', '?')}p - {f.get('ext')}"
            buttons.append([InlineKeyboardButton(label, callback_data=f['format_id'])])
        markup = InlineKeyboardMarkup(buttons)
        user_data[update.message.from_user.id] = url
        await update.message.reply_text("✅ اختر الجودة:", reply_markup=markup)
    except Exception as e:
        await update.message.reply_text(f"❗ حدث خطأ: {e}")

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    format_id = query.data
    url = user_data.get(user_id)

    if not url:
        await query.edit_message_text("❗ أرسل رابط أولاً.")
        return

    await query.edit_message_text("📥 جاري تحميل الفيديو...")
    try:
        filename = download_video(url, format_id)
        with open(filename, 'rb') as video:
            await query.message.reply_video(video)
        os.remove(filename)
        user_data.pop(user_id, None)
    except Exception as e:
        await query.message.reply_text(f"⚠️ خطأ أثناء التحميل: {e}")

# Flask endpoint for Webhook
@app.route(f'/{BOT_TOKEN}', methods=['POST'])
def telegram_webhook():
    from telegram import Update
    from telegram.ext import Application

    update = Update.de_json(request.get_json(force=True), bot.application.bot)
    bot.application.update_queue.put(update)
    return 'ok'

# Start bot via Webhook
async def start_bot():
    app_obj = Application.builder().token(BOT_TOKEN).build()
    app_obj.add_handler(CommandHandler("start", start))
    app_obj.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app_obj.add_handler(CallbackQueryHandler(button_callback))
    global bot
    bot = app_obj
    await app_obj.bot.set_webhook(url=f"{APP_URL}/{BOT_TOKEN}")
    await app_obj.start()

if __name__ == "__main__":
    import asyncio
    asyncio.run(start_bot())
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))