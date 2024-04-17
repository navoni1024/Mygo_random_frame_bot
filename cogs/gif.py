import tempfile
import discord
import json
import os
from discord.ext import commands
from core.classes import Cog_Extension
from core.video_processing import random_file, random_gif

with open('setting.json','r',encoding='utf8') as jfile:
	jdata = json.load(jfile)

class gif(Cog_Extension):	
    @commands.command(aliases=['!!!!!', 'G', 'g'])
    async def gif(self, message, duration=3.0):
        if(duration <= 0):
            await message.channel.send("The requested GIF length is invalid")
            return
        if(duration > jdata['gif_duration_limit']):
            await message.channel.send("The requested GIF length is too long")
            return
        vid = random_file(jdata["video_path"])
        temp_file = tempfile.mkstemp(suffix=".gif")
        random_gif(vid, temp_file[1], duration)
        await message.channel.send(file=discord.File(temp_file[1]))
        os.close(temp_file[0])
        os.unlink(temp_file[1])
        
        
async def setup(bot):
	await bot.add_cog(gif(bot))


