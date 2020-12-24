import random
from discord.ext import commands
from globals import user_info, version
from utils import write_txt, write_json
from datetime import datetime
from events import Events

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
        if not message.author.bot and not user_info[id]['isAdmin'] and random.uniform(0, 1) < user_info[id]['luck']:
            await message.channel.send(f"{message.author}, did something suspicious")            
            user_info[id]['lastmsg'] = message.content
            write_json('users.json', user_info)

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
                await ctx.send(f"{name} : {v['lastmsg']}")
                break

    @commands.command()
    async def laugh(self, ctx, name: str):      
        if len({k:v for (k, v) in user_info.items() if f"<@!{k}>" == name}) > 0:
            await ctx.send(f"HAHAHAHAHA <:MEGALUL:690548433169285141> :point_right: {name}")
        else:
            await ctx.send('?')

    @commands.command()
    async def greet(self, ctx, name: str):
        if len({k:v for (k, v) in user_info.items() if f"<@!{k}>" == name}) > 0:
            await ctx.send(f":wave: <:Okayge:690548078662385675> {random.choice(['你好', 'salam','hello'])} {name}")
        else:
            await ctx.send('greet who?')

    @commands.command()
    async def food(self, ctx, *args):
        await ctx.send(f"Go eat {random.choice(args).replace(',','')}")


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
        if len(user_info[id]['reaction']) > 0 and random.uniform(0, 1) < user_info[id]['luck']:
            await message.add_reaction(random.choice(user_info[id]['reaction']))
        # if message.content.strip().lower() == 'is richie gay':
        #     await message.channel.send('Yes')
        else:
            if any(x in message.content.lower().split() for x in user_info[id]['respond']):
                await message.channel.send(random.choice(user_info[id]['reply']))

    except KeyError:
        # print("No User info")
        pass

async def writelog(message):
    id = str(message.author.id)

    if not user_info[id]['isAdmin']:
        msg = f"({str(message.channel)}) {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} {user_info[id]['username']} : {message.content.strip().lower()}"
        write_txt('test_collect.txt', msg)