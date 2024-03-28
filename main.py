import discord
import logging
import json
import os
from discord.ext import commands

with open('setting.json','r',encoding='utf8') as jfile:
	jdata = json.load(jfile)

bot = commands.Bot(command_prefix=commands.when_mentioned_or(jdata['prefix']))

for filename in os.listdir('./cogs'):
	if filename.endswith('.py'):
		bot.load_extension(f'cogs.{filename[:-3]}')

@bot.event
async def on_ready():
	print('Nande Haruhikage yadaso')

if __name__ == "__main__":
	bot.run(jdata['token'])
