from rubpy import Client, exceptions
from rubpy.types import Updates
import requests


bot = Client("myself")


@bot.on_message_updates()
async def main(client: Updates):
	text:str = client.text
	if text.startswith("دلار"):
		result = requests.get("https://v3.api-free.ir/arz/?limit=30").json()["result"]
		matn = ''
		for data in result:
			name = data["name"]
			price = data["price"]
			matn += f'• **{name}** —> {price}\n'
		await client.reply(matn)
	elif text.startswith("ارز"):
		result = requests.get("http://v3.api-free.ir/crypto").json()["result"]
		matn = ''
		for data in result:
			name = data["name"]
			name_locale = data["name_locale"]
			price = data["price"]
			daily_change = data["daily_change_percent"]
			matn += f'• **{name}**({name_locale}) —> {price}\n'
		await client.reply(matn)
	elif text.startswith("طلا"):
		result = requests.get("http://v3.api-free.ir/gold").json()["result"]
		matn = ''
		for data in result:
			name = data["name"]
			price = data["price"]
			matn += f'• **{name}** —> {price}\n'
		await client.reply(matn)
	
	
bot.run()