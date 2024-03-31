import discord
import json
import tempfile
import os
from discord.ext import commands
from core.classes import Cog_Extension
from core.video_processing import random_file, random_frame

with open('setting.json','r',encoding='utf8') as jfile:
	jdata = json.load(jfile)

class listen(Cog_Extension):	
    @commands.Cog.listener()
    async def on_message(self, message):
        if(message.author.bot): return
        if('<@'+str(self.bot.user.id)+'>' == message.content):			
            vid = random_file('./video')
            temp_file = tempfile.mkstemp(suffix=".png")
            random_frame(vid, temp_file[1])
            await message.channel.send(file=discord.File(temp_file[1]))
            os.close(temp_file[0])
            os.unlink(temp_file[1])

async def setup(bot):
	await bot.add_cog(listen(bot))