FROM python:3.8

WORKDIR /usr/src/app

RUN git clone https://github.com/MichaelWoj/discord-stocks-bot.git

WORKDIR /usr/src/app/discord-stocks-bot

RUN pip install --no-cache-dir -r requirements.txt

ENV CHANNEL=YOUR_CHANNEL_ID
ENV TOKEN=YOUR_TOKEN

CMD ["python", "bot.py", CHANNEL, TOKEN]