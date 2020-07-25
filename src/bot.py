import discord
from discord.ext import commands
import subprocess
#import ffmpeg
#from voice_generator import creat_WAV
client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    # 「おはよう」で始まるか調べる
    if message.content.startswith("おはよう"):
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:
            # メッセージを書きます
            m = "おはようございます" + message.author.name + "さん！"
            # メッセージが送られてきたチャンネルへメッセージを送ります
            await message.channel.send(m)
        else :
            m="おはよう"
            await message.channel.send(m)

client.run("NzM2NjE2Mzk4NTk1NTU1Mzg2.XxxZew.TRTU4YfKA1f-XMvFkqUBuEDBP-Q")