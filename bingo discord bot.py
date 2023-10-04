from discord.ext import commands
import random
from discord.utils import get
import discord
import requests




intents= discord.Intents.default()

intents.members=True

bot = commands.Bot(command_prefix = '!',intents=intents)
# This is an event:
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


@bot.command()
async def vbingo(ctx,x,y,free):
    outcomes = [] #Fill outcomes here
    x=int(x)
    y=int(y)
    free=int(free)
    total = x * y
    totalfull = total - free
    chosenoutcomes = []
    for i in range(0, totalfull):
        choice = random.choice(outcomes)
        outcomes.remove(choice)
        chosenoutcomes.append(choice)

    for i in range(0, free):
        chosenoutcomes.append("Free!")
    maindict = {}

    for i in range(0, y):
        maindict[i] = []

    for n in range(0, x):
        currentlen = 0
        for i in range(0, y):
            finalchoice = random.choice(chosenoutcomes)
            chosenoutcomes.remove(finalchoice)
            if len(finalchoice) > currentlen:
                currentlen = len(finalchoice)
            maindict[i].append(finalchoice)
        # for i in range(0, y):
        #     while len(maindict[i][n]) < currentlen:
        #         maindict[i][n] = f"{maindict[i][n]} "
    embedVar = discord.Embed(title="Victor Bingo", description="Made by tms#9649, fueled by tex#6666", color=0x00ff00)

    for i in range(0,y):
        totalstring=""
        for n in range(0,x):
            totalstring=f"{totalstring}|{maindict[i][n]}"

        embedVar.add_field(name=totalstring, value=".", inline=False)
    await ctx.send(embed=embedVar)

bot.run("ODAxMDU3NDI3NTAzODQxMzAx.YAbI3Q.AS0dWGg6MjHpEfKK0GxBc2RO2Jw")
