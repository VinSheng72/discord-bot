import random
from discord.ext import commands
from globals import user_info, version
from utils import write_txt
from datetime import datetime


class Listener(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return None
        trigger = ['nigger', 'nigga', 'nig', 'niga', "n*gger", "black"]
        format = message.content.replace(" ", "").lower()
        if any(x in format for x in trigger):
            await message.channel.send("https://www.streamscheme.com/wp-content/uploads/2020/04/Cmonbruh.png.webp")

        await options(message)
        await writelog(message)

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        id = str(message.author.id)
        if not message.author.bot and not user_info[id]["isAdmin"]:
            await message.channel.send(f"{message.author}, did something suspicious")

    @commands.command()
    async def version(self, ctx):
        await ctx.send("Current version is " + version)

    @commands.command()
    async def flip(self, ctx):
        await ctx.send("Flipped " + random.choice(["Head", "Tail"]))

def setup(client):
    client.add_cog(Listener(client))


async def options(message):
    id = str(message.author.id)
    try:
        if user_info[id]["isAdmin"]:
            await message.add_reaction("😀")
        if message.content.strip().lower() == 'is richie gay':
            await message.channel.send('Yes')
        else:
            if message.content.lower() in user_info[id]['respond']:
                await message.channel.send(random.choice(user_info[id]['reply']))

        if( message.content.strip().lower() == 'laugh at him' and user_info[id]["isAdmin"]):
            await message.channel.send('HAHAHAHAHAHA :point_right:' + user_info[id]["username"])

    except KeyError:
        # print("No User info")
        pass

async def writelog(message):
    id = str(message.author.id)

    if user_info[id]['isAdmin'] :
        msg = datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ' ' + user_info[id]['username'] + ' : ' + message.content.strip().lower() + '\t\t' + str(message.channel)
        write_txt('test_collect.txt', msg)