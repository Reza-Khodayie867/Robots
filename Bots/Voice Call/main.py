from pyrubi import Client
from pyrubi.types import Message
import requests, urllib


bot = Client("pyrubi")

Admims = []

Musics = []


@bot.on_message()
def music(app: Message):
	text = app.text
	guid = app.author_guid
	target = app.object_guid
	
	if app.text:
		try:
			if text.startswith("پخش"):
				if app.reply_message_id:
					reply_id = app.reply_message_id
					get = bot.get_messages_by_id(target, [reply_id])["messages"][0]
					if "file_inline" in get:
						file = get["file_inline"]
						msg_id = get["message_id"]
						mime = file["mime"]
						aa = app.reply("در حال دانلود...")["message_update"]["message_id"]
						bot.download(object_guid=target, file_inline=file, message_id=msg_id, save_as=f"music.{mime}")
						bot.play_voice(target, f"music.{mime}")
						app.reply("در حال پخش...")
				else:
					link = text.split()[1]
					aa = app.reply("در حال دانلود...")["message_update"]["message_id"]
					urllib.request.urlretrieve(link, "music.mp3")
					bot.play_voice(target, "music.mp3")
					app.reply("در حال پخش...")
			
		except Exception as e:
			app.reply(f"Error → {e}")


print("starting...")
bot.run()
