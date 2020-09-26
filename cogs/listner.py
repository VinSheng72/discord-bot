import discord
from discord.ext import commands
import requests

# 694379147065163806


class Listener(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        trigger = ['nigger', 'nigga', 'nig', 'niga', "n*gger", "black"]
        format = message.content.replace(" ", "").lower()
        if any(x in format for x in trigger):
            await message.channel.send("https://www.streamscheme.com/wp-content/uploads/2020/04/Cmonbruh.png.webp")
        
        if message.author.id === '258442650259161088': #Richie
            msgReply = ('hue', 'pro', 'woW', 'noice', ':3', 'xd', 'uwu', 'im gay', ':poorU: :RichieNgaw:', 'geng')
            await message.channel.send(random.message.choice(msgReply))            
        elif message.author.id === '258420153912393728' and message.content.lower() in ('i', 'haha', 'hahaha', 'lol', 'xd', 'fuck', 'diu', 'niama', 'fk'):
            await message.channel.send('HAHAHAHAHA LOL 👏😂')
        elif message.author.id === '262222726209470464':
            await message.channel.send(':ok_hand:')

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if not message.author.bot:
            await message.channel.send(f"{message.author}, did something suspicious")


def setup(client):
    client.add_cog(Listener(client))
