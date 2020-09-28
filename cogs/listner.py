import random
from discord.ext import commands
from globals import user_info, admins


class Listener(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        trigger = ['nigger', 'nigga', 'nig', 'niga', "n*gger", "black"]
        format = message.content.replace(" ", "").lower()
        if any(x in format for x in trigger):
            await message.channel.send("https://www.streamscheme.com/wp-content/uploads/2020/04/Cmonbruh.png.webp")
        
        await options(message)

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if not message.author.bot:
            await message.channel.send(f"{message.author}, did something suspicious")


def setup(client):
    client.add_cog(Listener(client))

async def options(message):
    if str(message.author.id) in admins:     
        await message.add_reaction("😀")
    elif message.content.strip().lower() == 'is richie gay':
        await message.channel.send('Yes')
    else:
        #TODO checks if user id is in here, else skips to save performance
        for user in user_info:
            if str(message.author.id) == user_info[user]['id'] and message.content.lower() in user_info[user]['respond']:
                await message.channel.send(random.choice(user_info[user]['reply']))
