import discord
import csv
import codecs

TOKEN = 'NjgyMTYyMjYyNzE0NDgyNjg4.Xlcn6A.p_aTn8rgHKwgu_IuAcR7sE0Il24'

client = discord.Client()

with open('buki.csv', 'r',encoding='utf-8') as f:
    bukilist = list(csv.reader(f))
    f.close()

@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「!buki」と発言したらランダムに生成したブキ名が返る処理
    if message.content == '!buki':
        channel = VoiceChannel.menbers
        for num in bukilist:
            await message.channel.send({channel[len(num)]} + 'の使うブキは' + {*random.choice(bukilist)} + 'です')

client.run(TOKEN)
