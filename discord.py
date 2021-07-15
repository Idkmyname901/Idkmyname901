import discord
from discord.ext import commands
import random
import keep_alive
import requests, base64
import time

bot = commands.Bot(command_prefix='+')
bot.remove_command("help")

@bot.event
async def on_ready():
    print("Bot online")

@bot.command()
async def help(ctx):
    await ctx.send ("""
+ping=查bot ping
+ddd=嗲leemaleeblyatlee
+online=讓bot online
+wdnmd=wdnmd
+ruit= 肉 m
""")

@bot.command()
async def ping(ctx):
    await ctx.send (f"{round(bot.latency*1000)} (ms)")


@bot.command()
async def ddd(ctx):
    await ctx.send ("嗲leemaleeblyatlee")

@bot.command()
async def wdnmd(ctx):
    await ctx.send ("wdnmd")

@bot.command()
async def online(ctx):
    await ctx.send ("我日你媽的bot都online了你還想online???")

@bot.command()
async def ruit(ctx):
    await ctx.send ("肉便器")

keep_alive.keep_alive()
bot.run("")
