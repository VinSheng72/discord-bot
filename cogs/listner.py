import random
from discord.ext import commands
from globals import user_info


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

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if not message.author.bot:
            await message.channel.send(f"{message.author}, did something suspicious")


def setup(client):
    client.add_cog(Listener(client))


async def options(message):
    id = str(message.author.id)
    try:
        if user_info[id]["isAdmin"]:
            await message.add_reaction("😀")
        elif message.content.strip().lower() == 'is richie gay':
            await message.channel.send('Yes')
        else:
            if message.content.lower() in user_info[id]['respond']:
                await message.channel.send(random.choice(user_info[id]['reply']))
    except KeyError:
        # print("No User info")
        pass
