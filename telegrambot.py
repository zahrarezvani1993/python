import requests
import telebot
TOKEN ="6711795406:AAF3kpvciCn5zJekB6YFsTSpzaHFF2UyBXo"
bot = telebot.TeleBot(TOKEN)

# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
# 	bot.reply_to(message, "salam... usdt ra vaared konid!!!")

# @bot.message_handler(func=lambda message: True)
# def show_usdt(message):
# 	headers = {'Accept': 'application/json'}
# 	r = requests.get('https://api.tetherland.com/currencies', headers=headers)
# 	data=r.json()
# 	USDT=data['data']['currencies']['USDT']['price']
# 	if message.text.upper()=="USDT":
# 		if r.status_code==200:
# 			bot.reply_to(message,USDT)
# 			print(USDT)
# 		else:
# 			bot.reply_to(message,"ertebat ba server ghat ast.")
# 			print("ertebat ba server ghat ast.")
# 	else:
# 		bot.reply_to(message,"vorodi na motabar")
# 		print("vorodi na motabar")
	
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "salam... arz dijital ra vared konid!!!")

@bot.message_handler(func=lambda message: True)
def showPrice(message):
	symbol=message.text.upper()
	response=requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}")
	if response.status_code==200:
		data=response.json()
		bot.reply_to(message,f"{data["symbol"]} price is {data["price"]}")
	else:
		bot.reply_to(message,"vorodi eshtebah ast.")
bot.infinity_polling()


