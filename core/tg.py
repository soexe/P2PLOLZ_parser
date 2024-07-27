import configuration
from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup
import asyncio

async def send_message_to_channel(message, thread_url, user_url, transfer_url):
    bot = Bot(token=configuration.bot_token)

    keyboard = [
        [InlineKeyboardButton("Тема", url=thread_url)],
        [InlineKeyboardButton("Отправить деньги", url=transfer_url)],
        [InlineKeyboardButton("Профиль", url=user_url)],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await bot.send_message(
        chat_id=configuration.channel_id,
        text=message,
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )
