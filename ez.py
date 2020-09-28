import discord
from discord.ext import commands
from config import settings
import asyncio
import os

bot = commands.Bot(command_prefix = "ЗДЕСЬ") # префикс
os.chdir(r'ЗДЕСЬ') # директория с ботом

channels_list_ids = [ 754836145103175841, # ID серверов(желательно сверху вниз как на сервере)
                      754836180989902879,
                      754836202066149416,
                      754836202066149416,
                      754836262979895316,
                      756568649120088218,
                      756568681026420940,
                      756568724445855824,
                      756568785720311829,
                      756568860420866238,
                      758017566546591835,
                      758017606576767087,
                      758017634544517210 ]

@bot.event
async def on_voice_state_update(member, before, after):
    if after != None:
        try:

            if after.channel.id == 756924711232995444: # Комната с которой перекидывает

                all_count = {}

                for id in channels_list_ids:
                    count = 0
                    list_of_members = bot.get_channel(id).members
                    for i in list_of_members:
                        count += 1

                    all_count[id] = count

                tuples = list(all_count.items())
                tuples.sort(key=lambda i: i[1])

                number = -1
                for i in tuples:
                    if tuples[number][-1] >= 10: # настройка лимитов (конкретно здесь убирают каналы с >№ участников)
                        number = number - 1
                        continue
                    elif tuples[number][-1] >= 5: # второй уровень проверки, если первый не проходит
                        channel = bot.get_channel(tuples[number][0])
                        await member.move_to(channel)
                    else:
                        channel = bot.get_channel(tuples[0][0]) # Все остальные случае (конкретно если комната пустая)
                        await member.move_to(channel)

            await member.send('Ты перекинут в ' + str(channel.name))

        except AttributeError:
            pass

bot.run('ТОКЕН')