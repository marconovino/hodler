import shrimpy
import plotly.graph_objects as go
import discord
import asyncio
import os
import psutil
from discord.ext import commands

#  VARIABLES  #
bot = commands.Bot(command_prefix = '$', activity=discord.Game(name="Hodling coinz"))
TOKEN = os.getenv('DISCORD_TOKEN')
DATABASE_URL = os.environ['DATABASE_URL']
public_key = os.getenv('SHRIMPY_PUB')
secret_key = os.getenv('SHRIMPY_PRIV')
client = shrimpy.ShrimpyApiClient(public_key, secret_key)
dates = []
open_data = []
high_data = []
low_data = []
close_data = []

@bot.event
async def on_ready():
    print("-------------------")
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('-------------------')

@bot.command()
async def graph(ctx,coin,interval = '15m'):
    embed = discord.Embed(title="Loading graph", description="Sit tight! Our highly trained team of shiba inus are retrieving the data", color=0x0c0f27)
    message = await ctx.send(embed=embed)
    candles = client.get_candles('binance',coin,'BUSD',interval)
    for candle in candles:
        dates.append(candle['time'])
        open_data.append(candle['open'])
        high_data.append(candle['high'])
        low_data.append(candle['low'])
        close_data.append(candle['close'])
    fig = go.Figure(data=[go.Candlestick(x=dates,
                       open=open_data, high=high_data,
                       low=low_data, close=close_data)])
    fig.write_image("figure.png", engine="kaleido")
    embed = discord.Embed(title="Here is your graph!", description=f"{coin}/USD", color=0x0c0f27)
    file=discord.File('figure.png')
    embed.set_image(url="attachment://figure.png")
    await message.edit(file=file,embed = embed)

bot.run(TOKEN)
#hi taric