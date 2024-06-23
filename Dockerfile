FROM python:3.8

WORKDIR /usr/src/app

RUN git clone https://github.com/MichaelWoj/discord-stocks-bot.git && cd discord-stocks-bot

RUN pip install --no-cache-dir -r requirements.txt

ENV TOKEN=YOUR_TOKEN
ENV CHANNEL=YOUR_CHANNEL_ID

CMD ["python", "bot.py"]