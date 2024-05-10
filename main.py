import discord
import logging
import json
import os
import asyncio
from discord.ext import commands

class MyHelpCommand(commands.MinimalHelpCommand):
	async def send_pages(self):
		destination = self.get_destination()
		pic = discord.File("SOYO.jpg")
		embed=discord.Embed(title="買夠的指令:", url="")
		embed.add_field(name="@買夠", value="輸出一張圖", inline=False)
		embed.add_field(name="@買夠 g [num]", value="產生num秒的gif圖片，預設5秒。最高十秒", inline=True)
		embed.add_field(name="", value="[源碼](https://github.com/navoni1024/Mygo_random_frame_bot)", inline=False)
		embed.set_footer(text="*GIF太大的話，在discord中有可能不會動。")
		embed.set_image(url="attachment://SOYO.jpg")
		await destination.send(file=pic, embed=embed)

async def load_extensions():
	for filename in os.listdir('./cogs'):
		if filename.endswith('.py'):
			await bot.load_extension(f'cogs.{filename[:-3]}')

with open('setting.json','r',encoding='utf8') as jfile:
	jdata = json.load(jfile)

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix=commands.when_mentioned_or(jdata['prefix']), intents=intents)
bot.help_command = MyHelpCommand()

asyncio.run(load_extensions())

@bot.event
async def on_ready():
	print('なんで春日影やったの！？')

if __name__ == "__main__":
	bot.run(jdata['token'])
