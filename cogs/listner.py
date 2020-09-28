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

        # current user
        user = str(message.author.id)
        if user == user_info['richie']['name'] and message.content.lower() in user_info['richie']['respond']:
            await message.channel.send(random.choice(user_info['richie']['reply']))
        elif user == user_info['beng']['name'] and message.content.lower() in user_info['beng']['respond']:
            await message.channel.send(user_info['beng']['reply'][0])
        elif user in admins:
            await message.add_reaction("😀")
        elif message.content.strip().lower() == 'is richie gay':
            await message.channel.send('Yes')

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if not message.author.bot:
            await message.channel.send(f"{message.author}, did something suspicious")


def setup(client):
    client.add_cog(Listener(client))
