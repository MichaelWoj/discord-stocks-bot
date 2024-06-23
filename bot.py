import ccxt
import pandas as pd
import discord
import functions
from configparser import ConfigParser
from discord.ext import tasks
import os

exchange = ccxt.bybit()
config = ConfigParser()
config.read("config.ini")
CHANNEL_ID = int(os.environ['CHANNEL'])

class MyBot(discord.Client):
    def __init__(self, **options):
        super().__init__(**options)
        self.channel = None 

    async def on_ready(self):
        print(f'{self.user} is now running')
        self.channel = self.get_channel(CHANNEL_ID)
        self.monitor_rsi.start()

    @tasks.loop(seconds=5)
    async def monitor_rsi(self):
        df = functions.fetch_klines('SOL/USDT', '1h')
        df = functions.calculate_rsi(df, 14)

        rsi = df['rsi'].iloc[-1]
        message = None

        if rsi > 70:
            message = f'RSI is over 70: {rsi:.2f}.'
        elif rsi < 30:
            message = f'RSI is below 30: {rsi:.2f}.'
        else:
            message = f'its working  {rsi:.2f}'

        if message:
            await self.channel.send(message)

    @monitor_rsi.before_loop
    async def before_monitor(self):
        # Waits for the bot to be fully connected and ready to start the loop.
        await self.wait_until_ready()

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True  

# Run the bot
bot = MyBot(intents=intents)
bot.run(str(os.environ['TOKEN']))
