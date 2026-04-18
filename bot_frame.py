import discord
from discord.ext import commands
import random
from ciekawostki import ciekawostka

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='>', intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

@bot.command()
async def ciekawostka_discord(ctx, how_much:int):
    await ctx.send(ciekawostka(how_much))

bot.run("token")
