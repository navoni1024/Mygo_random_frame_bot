import tempfile
import discord
import json
from discord.ext import commands
from core.classes import Cog_Extension
from core.video_processing import random_file, select_random_frame

with open('setting.json','r',encoding='utf8') as jfile:
	jdata = json.load(jfile)

class mygo(Cog_Extension):	
    @commands.command(aliases=['!!!!!'])
    async def mygo(self, message):
        vid = random_file(jfile['video_path'])
        temp_file = tempfile.mkstemp(suffix=".jpg")
        select_random_frame(vid, temp_file[1])
        await message.channel.send(file=discord.File(temp_file[1]))
        
        
async def setup(bot):
	await bot.add_cog(mygo(bot))


