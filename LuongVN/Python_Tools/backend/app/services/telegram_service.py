import telebot 
from app.config.settings import settings

bot = telebot.TeleBot(settings.TELEGRAM_BOT_TOKEN)

def send_telegram_message(message: str): 
    try: 
        bot.send_message(
            chat_id=settings.TELEGRAM_CHAT_ID, 
            text=message   
        )

        return True
    except Exception as e: 
        print("Faild to send tele message: {e}")
        return False
