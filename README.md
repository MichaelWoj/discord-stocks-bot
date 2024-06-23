# discord-stocks-bot

## Hello

This is a quick guide on what the bot does and how to use it.

## What does the bot do?

It gets K-line data for SOL/USDT pair from Bybit, calculates RSI for it based on closing price and sends a message to Discord channel of your choice and if the calculated RSI value is over 70 or below 30.

## How to use it 

First you need to go https://discord.com/developers/applications and get your bot token, open config.ini and REPLACE "[YOUR TOKEN]" with it. You do this my clicking "New Application" then once the bot is made you go Bot -> Reset Token and copy the token that appears after reseting it.

Then get the ID of the Discord channel you want the bot to post to and replace "[CHANNEL ID]" with it. You do this by right clicking on a channel and selecting "Copy Channel ID". If you don't see the option you need to turn on "Developer Mode" (Settings -> Advanced -> Developer Mode).

Once that's done all you have to do is double click " main.py " to turn it on. Make sure to have all of the files in 1 location and that you have Python3 installed on your PC.
