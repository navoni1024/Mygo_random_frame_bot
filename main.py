import discord
import logging
import json
import os
import asyncio
from discord.ext import commands

async def load_extensions():
	for filename in os.listdir('./cogs'):
		if filename.endswith('.py'):
			await bot.load_extension(f'cogs.{filename[:-3]}')

with open('setting.json','r',encoding='utf8') as jfile:
	jdata = json.load(jfile)

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix=commands.when_mentioned_or(jdata['prefix']), intents=intents)

asyncio.run(load_extensions())

@bot.event
async def on_ready():
	print('なんで春日影やったの！？')

if __name__ == "__main__":
	bot.run(jdata['token'])
