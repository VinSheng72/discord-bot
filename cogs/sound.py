import discord
from discord.ext import commands
from discord.utils import get
import requests
import os
import time
from discord import FFmpegPCMAudio
from youtube_dl import YoutubeDL
import asyncio


class Sound(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['j'])
    async def join(self, ctx):
        channel = ctx.author.voice.channel
        voice = get(self.client.voice_clients, guild=ctx.guild)
        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()
        return voice    
            
    @commands.command(aliases=['dc'])
    async def disconnect(self, ctx):
        voice = get(self.client.voice_clients, guild=ctx.guild)
        if voice.is_connected():
            await voice.disconnect()
        else:
            await ctx.send("Haiya!! Not in voice channel how to leave")


    @commands.command()
    async def ohaiyo(self, ctx):
        try:
            # callback
            voice = await ctx.invoke(self.join)

            # for HEROKU deploy
            voice.play(discord.FFmpegPCMAudio("song.mp3"), after=None)

            # for local debug
            # voice.play(discord.FFmpegPCMAudio(
            #     executable="C:/ProgramData/chocolatey/bin/ffmpeg.exe", source="song.mp3"), after=None)
            voice.volume = 100
            voice.is_playing()
            while voice.is_playing():
                time.sleep(1)
            else:
                await voice.disconnect()

        except AttributeError:
            await ctx.send("Haiya!! Join a voice channel first")

    _songQueue = asyncio.Queue()

    @commands.command(aliases=['p'])
    async def play(self, ctx, url:str):
        try:
            voice = await ctx.invoke(self.join)

            if voice.is_playing():
                await ctx.send("still playing music")
                return
            
            if self._songQueue.qsize > 1:
                # await ctx.invoke(self.queue)                
                self._songQueue.put(url)
            else:
                # do nothing
                url=url

            ydl_opts = {
                'format': 'bestaudio/best',
                # 'postprocessors' : [{
                #     'key' : 'FFmpegExtractAudio',
                #     'preferredcodec' : 'mp3',
                #     'preferredquality' : '192'
                # }]
            }

            with YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                path = info['formats'][0]['url']
                title = info.get('title', None)

            FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
            await voice.play(discord.FFmpegPCMAudio(path, **FFMPEG_OPTIONS), after=lambda x: ctx.send(f"Done"))

            await ctx.send(f"Now Playing **{title}**")

            voice.volume = 100
            
            while voice.is_playing():
                time.sleep(1)
                
        except AttributeError:
            await ctx.send("Haiya!! Join a voice channel first")
        except YoutubeDL.ExtractorError:
            await ctx.send("Cannot play this")


    # @commands.command()
    # def skip(self):
    #     asyncio.run_coroutine_threadsafe(play(self.client, nexturl), client.loop)

    @commands.command(aliases=['s'])
    async def stop(self, ctx):
        voice = get(self.client.voice_clients, guild=ctx.guild)
        if voice.is_playing():
            voice.stop()
            await ctx.send(f"Stopped, No song played")        
        else:
            await ctx.send(f"No song")

    @commands.command()
    async def pause(self, ctx):
        voice = get(self.client.voice_clients, guild=ctx.guild)
        if voice.is_playing():
            voice.pause()
            await ctx.send(f"Paused")
        else:
            await ctx.send(f"No song")

    @commands.command()
    async def resume(self, ctx):
        voice = get(self.client.voice_clients, guild=ctx.guild)
        if voice.is_playing():
            voice.resume()
            await ctx.send(f"Resumed")
        else:
            await ctx.send(f"No song")

    # @commands.command()
    # async def queue(self, ctx, url:str):
    #     voice = get(self.client.voice_clients, guild=ctx.guild)
    #     self._songQueue.put(url)


def setup(client):
    client.add_cog(Sound(client))
