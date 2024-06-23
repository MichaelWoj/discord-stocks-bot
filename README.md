# discord-stocks-bot

## Hello

This is a quick guide on what the bot does and how to use it.

## What does the bot do?

It gets K-line data for SOL/USDT pair from Bybit, calculates RSI for it based on closing price and sends a message to Discord channel of your choice and if the calculated RSI value is over 70 or below 30.

## How to use it 

First, change ENV CHANNEL and ENV TOKEN in the dockerfile to your corresopnding keys. Here is how to obtain them:

CHANNEL_ID: To get the ID of the Discord channel you wish the bot to post you right click on a channel and selecting "Copy Channel ID". If you don't see the option you need to turn on "Developer Mode" (Settings -> Advanced -> Developer Mode).

BOT_TOKEN: First you need to go https://discord.com/developers/applications, click "New Application" then once the bot is made you go Bot -> Reset Token and copy the token that appears after reseting it.

Once both of the keys are replaced you create a docker image using the dockerfile. The command is: **docker build -t your-image-name .**

When the image is done all you have to do is run the container with the command: **docker container run your-image-name**
