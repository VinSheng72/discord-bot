from discord.ext import commands
import requests


class NSFW(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def pussy(self, ctx):
        payload = {"type": 'pussy'}
        r = requests.get('https://nekobot.xyz/api/image', params=payload)
        r_dist = r.json()
        await ctx.send(r_dist["message"])

    @commands.command()
    async def pgif(self, ctx):
        payload = {"type": 'pgif'}
        r = requests.get('https://nekobot.xyz/api/image', params=payload)
        r_dist = r.json()
        await ctx.send(r_dist["message"])

    @commands.command(name="4k")
    async def _4k(self, ctx):
        payload = {"type": '4k'}
        r = requests.get('https://nekobot.xyz/api/image', params=payload)
        r_dist = r.json()
        await ctx.send(r_dist["message"])

    @commands.command()
    async def anal(self, ctx):
        payload = {"type": 'anal'}
        r = requests.get('https://nekobot.xyz/api/image', params=payload)
        r_dist = r.json()
        await ctx.send(r_dist["message"])

    @commands.command()
    async def hentai(self, ctx):
        payload = {"type": 'hentai'}
        r = requests.get('https://nekobot.xyz/api/image', params=payload)
        r_dist = r.json()
        await ctx.send(r_dist["message"])

    @commands.command()
    async def gay(self, ctx):
        await ctx.send("Why are you gay?")


def setup(client):
    client.add_cog(NSFW(client))
