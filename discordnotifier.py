from telebot import TeleBot
from json import loads
from loguru import logger
from sys import stderr
from msvcrt import getch
from ctypes import windll
from os import system
from dotenv import dotenv_values
from requests import get

system("cls")
print('Telegram Channel - https://t.me/n4z4v0d\n')

config = dotenv_values(".env")
tgbot_key = str(config['tgbotkey'])
tg_userid = int(config['tguserid'])
ds_token = str(config['dstoken'])
ds_chatid = int(config['dschatid'])
bot = TeleBot(tgbot_key)

logger.remove()
logger.add(stderr, format="<white>{time:HH:mm:ss}</white> | <level>{level: <8}</level> | <cyan>{line}</cyan> - <white>{message}</white>")

def check_posts(old_msg_id):
	logger.success('The bot has been successfully launched, waiting for new posts')
	while True:
		try:
			r = get(f'https://discord.com/api/v9/channels/{ds_chatid}/messages?limit=1', headers={'authorization': ds_token})
			new_msg_id = loads(r.text)[0]['id']
			if old_msg_id == None or int(old_msg_id) != int(new_msg_id):
				msg_text = loads(r.text)[0]['content']
				if old_msg_id != None:
					if len(msg_text) > 0:
						bot.send_message(int(tg_userid), 'New post:\n'+str(msg_text))
					else:
						bot.send_message(int(tg_userid), 'New post: empty')
					logger.success('A new post. The information was successfully sent to Telegram')
				old_msg_id = new_msg_id
		except:
			pass

check_posts(None)