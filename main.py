import json
import os
import random
import discord
from discord.ext import commands
from config import settings
import asyncio
import re
import time

# /home/lokisor/BOT
# C:\Users\Vitaliy\Desktop\BOT
# /home/daniil/bot

path_dir = r'/home/daniil/bot'
bot = commands.Bot(command_prefix = "~")
os.chdir(path_dir)

bot_list = [
    234395307759108106,
    159985870458322944,
    264193410141913088,
    235088799074484224,
    727519290072498206
]

#channels_list_ids = [ 756924711673397358, # ID серверов(желательно сверху вниз как на сервере)
#                      758368327285342218,
#                      758368345845530674 ]

#@bot.event
#async def on_voice_state_update(member, before, after):
#    if after != None:
#        channel_from = bot.get_channel(756924711232995444) # Комната с которой перекидывает
#
#        try:
#
#            if after.channel.id == 756924711232995444: # Комната с которой перекидывает
#
#                all_count = {}
#
#                for id in channels_list_ids:
#                    count = 0
#                    list_of_members = bot.get_channel(id).members
#                    for i in list_of_members:
#                        count += 1
#
#                    all_count[id] = count
#
#               tuples = list(all_count.items())
#                tuples.sort(key=lambda i: i[1])
#
#                number = -1
#                for i in tuples:
#                    if tuples[number][-1] >= 3: # настройка лимитов (конкретно здесь убирают каналы с >№ участников)
#                        number = number - 1
#                        continue
#                    elif tuples[number][-1] >= 1: # второй уровень проверки, если первый не проходит
#                        channel = bot.get_channel(tuples[number][0])
#                        await member.move_to(channel)
#                    else:
#                        channel = bot.get_channel(tuples[0][0]) # Все остальные случае (конкретно если комната пустая)
#                        await member.move_to(channel)
#
#            await member.send('Ты перекинут в ' + str(channel.name))
#
#channels_list_ids = [ 756924711673397358, # ID серверов(желательно сверху вниз как на сервере)
#                      758368327285342218,
#                      758368345845530674 ]

#@bot.event
#async def on_voice_state_update(member, before, after):
#    if after != None:
#        channel_from = bot.get_channel(756924711232995444) # Комната с которой перекидывает
#
#        try:
#
#            if after.channel.id == 756924711232995444: # Комната с которой перекидывает
#
#                all_count = {}
#
#                for id in channels_list_ids:
#                    count = 0
#                    list_of_members = bot.get_channel(id).members
#                    for i in list_of_members:
#                        count += 1
#
#                    all_count[id] = count
#
#               tuples = list(all_count.items())
#                tuples.sort(key=lambda i: i[1])
#
#                number = -1
#                for i in tuples:
#                    if tuples[number][-1] >= 3: # настройка лимитов (конкретно здесь убирают каналы с >№ участников)
#                        number = number - 1
#                        continue
#                    elif tuples[number][-1] >= 1: # второй уровень проверки, если первый не проходит
#                        channel = bot.get_channel(tuples[number][0])
#                        await member.move_to(channel)
#                    else:
#                        channel = bot.get_channel(tuples[0][0]) # Все остальные случае (конкретно если комната пустая)
#                        await member.move_to(channel)
#
#            await member.send('Ты перекинут в ' + str(channel.name))
#
#        except AttributeError:
#            pass

@bot.event
async def on_raw_reaction_add(ctx):
    message_id = ctx.message_id
    if message_id == 733759588406657105:  # id  сообщения для комментирования
        guild_id = ctx.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, bot.guilds)  # хз как обьяснить что это, но оно надо
        if ctx.emoji.name == "✅":  # смайл
            role = discord.utils.get(guild.roles, name='User')
            member = discord.utils.find(lambda m: m.id == ctx.user_id,
                                        guild.members)  # хз как обьяснить что это, но оно надо
            if member:  # проверка на существование юзера
                await member.add_roles(role)  # добавление роли ботом
            else:
                print('Такого челика нет')
        else:
            print("Такой роли нет")

async def add_lvl(ctx, users, user):
    exp = users[user]['exp']
    lvl_start = users[user]['lvl']
    lvl_end = int(exp ** (1 / 4))
    if lvl_start < lvl_end:
        users[user]['lvl'] = lvl_end
        await ctx.channel.send(f'{ctx.author.mention} апнул {users[user]["lvl"]} уровень!')

        guilds = bot.guilds
        roles = guilds[0].roles

        if lvl_end >= 2 and lvl_end <= 5:
            for role in roles:
                pattern = r'\[1\-5\]'
                matched = re.match(pattern, role.name)
                if matched != None:
                    await ctx.author.add_roles(role)

        elif lvl_end >= 6 and lvl_end <= 10:
            for role in roles:
                pattern = r'\[5\-10\]'
                matched = re.match(pattern, role.name)
                if matched != None:
                    await ctx.author.add_roles(role)

        elif lvl_end >= 11 and lvl_end <= 15:
            for role in roles:
                pattern = r'\[10\-15\]'
                matched = re.match(pattern, role.name)
                if matched != None:
                    await ctx.author.add_roles(role)
        elif lvl_end >= 16 and lvl_end <= 20:
            for role in roles:
                pattern = r'\[15\-20\]'
                matched = re.match(pattern, role.name)
                if matched != None:
                    await ctx.author.add_roles(role)
        elif lvl_end >= 21 and lvl_end <= 25:
            for role in roles:
                pattern = r'\[20\-25\]'
                matched = re.match(pattern, role.name)
                if matched != None:
                    await ctx.author.add_roles(role)
        elif lvl_end >= 26 and lvl_end <= 30:
            for role in roles:
                pattern = r'\[25\-30\]'
                matched = re.match(pattern, role.name)
                if matched != None:
                    await ctx.author.add_roles(role)

async def lvl(ctx, users): #+
    user = str(ctx.author.id)
    await ctx.channel.send(f'{ctx.author.mention}, у тебя {int(users[user]["lvl"])} LVL!')


async def roll(ctx): #+
    roll = str(random.randint(1, 100))
    await ctx.channel.send("[1-100]: " + roll)


async def ping(ctx): #+
    await ctx.channel.send('pong')


async def add_exp(ctx, users, user, exp): #+
    if ctx.author.id == 727519290072498206:
        return
    else:
        users[user]['exp'] += exp


async def update_data(users, user): #+
    if not user in users:
        users[user] = {}
        users[user]['exp'] = 0


        users[user]['lvl'] = 1


async def clear(ctx):
    count = ctx.content.split()
    count_int = int(count[1])
    await ctx.channel.purge(limit=int(count_int) + 1)
    await ctx.channel.send('Удалено сообщений: ' + str(count_int))


async def find_member(m):
    for guild in bot.guilds:
        for i in guild.members:
            id = i.id
            if int(id) == int(m):
                return i
            else:
                continue


async def bibametr(ctx):
    biba = str(random.randint(1, 40))
    author = ctx.author
    await ctx.channel.send(f'{author.mention}, у тебя {biba} см!')


async def find_role(m):
    for guild in bot.guilds:
        for i in guild.roles:
            if str(i) == 'Muted':
                return i


async def mute(ctx):
    m = ctx.content.split()[1]
    m = str(m).replace('!', '').replace('@', '').replace('>', '').replace('<', '')

    m_ready = await find_member(m)
    r_ready = await find_role(m)
    server = bot.get_guild(393828800133333022)
    role_user = server.get_role(692144762039435284)

    if m_ready != None and r_ready != None:
        await ctx.channel.send(f'{m_ready.mention} получает мут!')
        await m_ready.add_roles(r_ready)
        await m_ready.remove_roles(role_user)
    else:
        await ctx.channel.send(f'{m_ready.mention} уже в муте!')


async def unmute(ctx):
    m = ctx.content.split()[1]
    m = str(m).replace('!', '').replace('@', '').replace('>', '').replace('<', '')
    m_ready = await find_member(m)

    server = bot.get_guild(393828800133333022)
    role_muted = server.get_role(619253182081794048)
    role_user = server.get_role(692144762039435284)

    if m_ready in role_muted.members:
        await m_ready.remove_roles(role_muted)
        await ctx.channel.send(f'{m_ready.mention} больше не в муте!')
        await m_ready.add_roles(role_user)
    else:
        await ctx.channel.send(f'{m_ready.mention} Пользователь не в муте!')


@bot.event
async def on_message(ctx):
    with open(path_dir + '/users.json', 'r') as f:  # lvl system
        users = json.load(f)
    if ctx.author.id in bot_list:
        print('ПИЗДЕЦ')
    else:
        await update_data(users, str(ctx.author.id))
        await add_lvl(ctx, users, str(ctx.author.id))
        await add_exp(ctx, users, str(ctx.author.id), 5)
        with open(path_dir + '/users.json', 'w') as f:
            json.dump(users, f, indent=2, ensure_ascii=False)

    if ctx.content.startswith('~lvl'):
        await lvl(ctx, users)

    if ctx.content.startswith('~ping'):
        await ping(ctx)

    if ctx.content.startswith('~bibametr'):
        await bibametr(ctx)

    if ctx.content.startswith('~roll'):
        await roll(ctx)
    if ctx.content.startswith('~clear'):
        if discord.utils.get(ctx.author.roles, name= 'Staff Senior') is None or discord.utils.get(ctx.author.roles, name= 'Bot Dev') is None:
            await ctx.channel.send('У вас недостаточно прав!')
            return False
        else:
            await clear(ctx)
    #mute
    if ctx.content.startswith('~mute'):
        if discord.utils.get(ctx.author.roles, name='Staff'):
            await mute(ctx)
        else:
            ctx.channel.send('У вас недостаточно прав!')

    if ctx.content.startswith('~unmute'):
        if discord.utils.get(ctx.author.roles, name='Staff'):
            await unmute(ctx)
        else:
            ctx.channel.send('У вас недостаточно прав!')

    if ctx.content.startswith('~join'):
        channel1 = ctx.author.voice.channel
        await channel1.connect()

    await bot.process_commands(ctx) # что бы работал @bot.command


# Счёт участников
@bot.event
async def on_member_join(member: discord.Member):
    CountChannel = bot.get_channel(727656124911714316)
    await CountChannel.edit(name="Участников: {}".format(len(member.guild.members)))


@bot.event
async def on_member_remove(member: discord.Member):
    CountChannel = bot.get_channel(727656124911714316)
    await CountChannel.edit(name="Участников: {}".format(len(member.guild.members)))


# Статус у бота
@bot.event
async def on_ready():
    print('Bot is ready!')
    await bot.change_presence(activity=discord.Game(name="~"))

bot.run(settings['token'])