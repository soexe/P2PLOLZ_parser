import os
import sys
import time
import asyncio
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'core')))
import configuration
from core import forum
from core import parser
from core import tg

def calculator(seconds):
    minutes = 0
    if seconds < 60:
        minutes = 1
    elif seconds >= 60 and seconds <= 120:
        minutes = 2
    elif seconds >= 121 and seconds <= 180:
        minutes = 3
    elif seconds >= 181 and seconds <= 240:
        minutes = 4
    elif seconds >= 241 and seconds <= 300:
        minutes = 5
    else:
        minutes = 5
    return minutes

ids = []

async def main_loop():
    while True:
        mylist = forum.get_threads(url='https://api.zelenka.guru/threads?forum_id=1001', token=configuration.lzt_token)
        response = parser.job(mylist, time.time(), processed_ids=ids)
        if response is not None:
            print('Найдена новая тема, обработка...')
            thread_id = response['thread_id']
            ids.append(thread_id)
            message = "❗Доступен новый P2P обмен\n"
            message += f'Направление: {response["navigation"]}\n'
            message += f'Создано: {str(calculator(int(response["created"])))} минуты назад\n'
            message += f'Создал: [{response["username"]}]({response["user_url"]})'

            await tg.send_message_to_channel(
                message,
                response['url'],
                response['user_url'],
                response['transfer_url']
            )
        else:
            print('Новых тем в разделе не найдено, sleep {} secs'.format(configuration.wait))

        await asyncio.sleep(configuration.wait)
if __name__ == "__main__":
    asyncio.run(main_loop())
