import discord
from discord.ext import commands, tasks
import os
import datetime
import pytz

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

async def give_reward_role_to_last_sent_msg_of_user(channel, role_name):
    role = discord.utils.get(channel.guild.roles, name=role_name)

    async for msg in channel.history(limit=10):
        if not msg.embeds:
            await msg.author.add_roles(role)
            return

@bot.event
async def on_message(message):
    if message.guild is None:
        return

    if message.channel.id == 1117024608651063377 or message.channel.id == 1118401512478097499:
        if message.embeds:
            embed = message.embeds[0]
            for n in range(1, 6):
                if embed.title and f'JLPT N{n} Reading Quiz Ended' in embed.title:
                    for field in embed.fields[::-1]:
                        if field.name.startswith('Unanswered Questions'):
                            unanswered_questions = eval(field.name.split(' ')[-1])
                            if unanswered_questions is None or unanswered_questions <= 3:
                                await give_reward_role_to_last_sent_msg_of_user(message.channel, f'JLPT N{n}')
                            return
                        elif field.name == 'Final Scores':
                            await give_reward_role_to_last_sent_msg_of_user(message.channel, f'JLPT N{n}')
                            return
    await bot.process_commands(message)


@bot.command(name='test')
async def test(ctx):
    embed = discord.Embed(title="JLPT N1~5ロールが付いている人の一覧")
    for n in range(1, 6):
        role = discord.utils.get(ctx.guild.roles, name=f'JLPT N{n}')
        members = [member.display_name for member in role.members]
        embed.add_field(name=f'JLPT N{n}', value='\n'.join(members), inline=False)
    await ctx.send(embed=embed)

TOKEN = os.getenv("DISCORD_TOKEN")

@tasks.loop(minutes=1)  # Update every 1 minute, you can adjust the interval as needed
async def update_time():
    us_time = datetime.datetime.now(pytz.timezone('US/Eastern')).strftime('%H:%M')
    eu_time = datetime.datetime.now(pytz.timezone('Europe/Paris')).strftime('%H:%M')
    jp_time = datetime.datetime.now(pytz.timezone('Asia/Tokyo')).strftime('%H:%M')
    status = f"US Time: {us_time} / Europe Time: {eu_time} / Japan Time: {jp_time}"
    await bot.change_presence(activity=discord.Game(name=status))

@update_time.before_loop
async def before_update_time():
    await bot.wait_until_ready()

@update_time.after_loop
async def after_update_time():
    if update_time.is_being_cancelled():
        print("The time update task has been cancelled.")

update_time.start()

bot.run(TOKEN)

