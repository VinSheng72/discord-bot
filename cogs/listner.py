import random
from discord.ext import commands
from globals import user_info, version
from utils import write_txt, roll
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
        if not message.author.bot and not user_info[id]['isAdmin'] and roll() < user_info[id]['luck']:
            await message.channel.send(f"{message.author}, did something suspicious")

    @commands.command()
    async def version(self, ctx):
        await ctx.send(f"Current version is {version}")

    @commands.command()
    async def flip(self, ctx):
        await ctx.send(f"Flipped {random.choice(['Head', 'Tail'])}")

    @commands.command()
    async def snipe(self, ctx, name: str):
        for (k, v) in user_info.items():
            if f"<@!{k}>" == name:
                await ctx.send(v['lastmsg'])
                break

    @commands.command()
    async def laugh(self, ctx, name: str):      
        if len({k:v for (k, v) in user_info.items() if f"<@!{k}>" == name}) > 0:
            await ctx.send(f"HAHAHAHAHA :point_right {name}")
        else:
            await ctx.send('?')


    # @commands.command()
    # async def stop(self, ctx, service=''):
    #     id = str(ctx.author.id)
    #     if(user_info[id]["isAdmin"]):
    #         if(service.lower() == 'options'):

    #     else:
    #         await ctx.send("No")


def setup(client):
    client.add_cog(Listener(client))




async def options(message):
    id = str(message.author.id)
    try:
        if len(user_info[id]['reaction']) > 0 and roll() < user_info[id]['luck']:
            await message.add_reaction(random.choice(user_info[id]['reaction']))
        if message.content.strip().lower() == 'is richie gay':
            await message.channel.send('Yes')
        else:
            if message.content.lower() in user_info[id]['respond']:
                await message.channel.send(random.choice(user_info[id]['reply']))

        print(user_info[id]['lastmsg'] )
        user_info[id]['lastmsg'] = message.content
        print(user_info[id]['lastmsg'] )

    except KeyError:
        # print("No User info")
        pass

async def writelog(message):
    id = str(message.author.id)

    if not user_info[id]['isAdmin']:
        msg = f"({str(message.channel)}) {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} {user_info[id]['username']} : {message.content.strip().lower()}"
        write_txt('test_collect.txt', msg)