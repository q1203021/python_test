import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from telegram import Update
from telegram.constants import ChatAction
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

load_dotenv()
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

if not TELEGRAM_TOKEN or not GEMINI_API_KEY:
    raise ValueError("請確認 .env 檔案中已設定 TELEGRAM_BOT_TOKEN 與 GEMINI_API_KEY")

# 初始化 Gemini Client
client = genai.Client(api_key=GEMINI_API_KEY)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 你好！我是串接 Gemini 3.7 Flash 的 Telegram AI 助理，請隨時向我提問！")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return

    # 顯示「輸入中」狀態
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)

    try:
        # 使用非同步呼叫 Gemini 3.7 Flash
        response = await client.aio.models.generate_content(
            model="gemini-3.7-flash",
            contents=update.message.text,
            config=types.GenerateContentConfig(
                system_instruction="你是一個繁體中文的 Telegram 智慧助理，請用繁體中文給出清晰、條理分明的回答。"
            )
        )

        reply_content = response.text if response.text else "抱歉，目前無法生成回應。"
        await update.message.reply_text(reply_content)

    except Exception as e:
        print(f"呼叫 Gemini 3.7 Flash 發生錯誤: {e}")
        await update.message.reply_text("⚠️ 處理訊息時發生錯誤，請稍後再試。")

def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🚀 Gemini 3.7 Flash Telegram Bot 運行中...")
    app.run_polling()

if __name__ == "__main__":
    main()