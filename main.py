import discord
from discord.ext import commands
import os
from quart import Quart

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)
app = Quart(__name__)

async def give_reward_role_to_last_sent_msg_of_user(channel, role_name):
    if channel.last_message.content.startswith('k!quiz n') and channel.last_message.content[8] in '12345' and channel.last_message.content[10] in '123456789':
        return
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

@app.route('/')
async def home():
    return "I'm alive"

TOKEN = os.getenv("DISCORD_TOKEN")
PORT = os.environ.get('PORT')

@bot.event
async def on_ready():
    bot.loop.create_task(app.run_task('0.0.0.0', PORT))

bot.run(TOKEN)
