import discord
from discord.ext import commands
from config import settings
import asyncio
import os

bot = commands.Bot(command_prefix = "HERE") # prefix
os.chdir(r'HERE') # dir with bot

channels_list_ids = [ 754836145103175841, # ID of all using channels
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

            if after.channel.id == 756924711232995444: # id main channel

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
                n = 10 # setting limit of user in one channel(10)
                for i in tuples:
                    if tuples[number][-1] >= n: 
                        number = number - 1
                        continue
                    elif tuples[number][-1] >= n/2:
                        channel = bot.get_channel(tuples[number][0])
                        await member.move_to(channel)
                    else:
                        channel = bot.get_channel(tuples[0][0]) #
                        await member.move_to(channel)

            await member.send('Ты перекинут в ' + str(channel.name))

        except AttributeError:
            pass

bot.run('ТОКЕН')
