import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
import os
from quart import Quart

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)
slash = SlashCommand(bot, sync_commands=True)

app = Quart(__name__)

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

    if message.channel.id == 1117024608651063377:
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

@app.route('/')
async def home():
    return "I'm alive"

TOKEN = os.getenv("DISCORD_TOKEN")
PORT = os.environ.get('PORT')

@bot.event
async def on_ready():
    bot.loop.create_task(app.run_task('0.0.0.0', PORT))

@slash.slash(name="role", description="Displays the list of users with JLPT roles")
async def role(ctx: SlashContext):
    embed = discord.Embed(title="JLPT Role List", color=discord.Color.blue())
    for n in range(1, 6):
        role_name = f'JLPT N{n}'
        role = discord.utils.get(ctx.guild.roles, name=role_name)
        members = [member.display_name for member in role.members]
        members_str = ', '.join(members) if members else 'None'
        embed.add_field(name=role_name, value=members_str)
    await ctx.send(embed=embed)

bot.run(TOKEN)
