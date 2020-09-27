import discord
import requests
import random
from discord.ext import commands
from globals import *

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
        
        # current user
        user = str(message.author.id)

        if user == '258442650259161088' and message.content.lower() in richie_stuff['respond'] : #Richie
            await message.channel.send(random.choice(richie_stuff['reply']))        
        elif user == '258420153912393728' and message.content.lower() in ('i', 'haha', 'hahaha', 'lol', 'xd', 'fuck', 'diu', 'niama', 'fk'):
            await message.channel.send('HAHAHAHAHA LOL 👏😂')
        elif user in admins:                     
            await message.author.react('759647085862584380') 
        elif message.content.strip().lower() == 'is richie gay':
            await message.channel.send('Yes')

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if not message.author.bot:
            await message.channel.send(f"{message.author}, did something suspicious")


def setup(client):
    client.add_cog(Listener(client))

