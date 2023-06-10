import discord
from discord.ext import commands
import os
from keep_alive import keep_alive

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

    if message.channel.id == 769733434834157588:
        if message.embeds:
            embed = message.embeds[0]
            if embed.title and 'JLPT N4 Reading Quiz Ended' in embed.title:
                for field in embed.fields[::-1]:
                    if field.name.startswith('Unanswered Questions'):
                        unanswered_questions = eval(field.name.split(' ')[-1])
                        if unanswered_questions is None or unanswered_questions <= 3:
                            await give_reward_role_to_last_sent_msg_of_user(message.channel, 'JLPT N4')
                        return
                    elif field.name == 'Final Scores':
                        await give_reward_role_to_last_sent_msg_of_user(message.channel, 'JLPT N4')
                        return

TOKEN = os.getenv("DISCORD_TOKEN")
keep_alive()
bot.run(TOKEN)
