import discord
import random
from discord.ext import commands
import os
from quart import Quart

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)
app = Quart(__name__)

fun_facts = [
    "Japan is known as the Land of the Rising Sun.",
    "Japan has the third longest life expectancy in the world.",
    "Japan consists of over 6,800 islands.",
    "Home to 33 million people, the Tokyo-Yokohama metropolitan area is the largest populated metropolitan region in the world.",
    "Japan has more than 3,000 McDonald’s restaurants, the largest number in any country outside the U.S.",
    "Japanese director Akira Kurosawa’s film The Hidden Fortress was the basis for George Lucas’ famous film Star Wars.",
    "Each spring, Japan has a festival that celebrates both the penis and female fertility called Kanamara Matsuri, or 'Festival of the Steel Phallus.'",
    "Japan is one of the few countries in the world where the elderly outnumber the young.",
    "The Japanese eat more fish than any other people in the world, about 17 million tons per year.",
    "Over two billion manga, Japanese comic books or graphic novels, are sold in Japan each year.",
    "More than 5 billion servings of instant ramen noodles are consumed in Japan each year.",
    "Sushi has been around since about the second century A.D. It started as a way to preserve fish in China and eventually made its way to Japan. The method of eating raw fish and rice began in the early 17th century. Sushi does not mean raw fish in Japanese. It actually means rice seasoned with vinegar, sugar, and salt. Raw fish sliced and served alone without rice is called sashimi.",
    "Japanese Kobe beef is famous worldwide for its succulence and taste. The Japanese cows this beef comes from receive daily massages and, in summer, are fed a diet of saké and beer mash. True Kobe beef comes from only 262 farms in the Tajima region, of which Kobe is the capital, and each of which raises an average of 5 of the animals at a time. In the United States, Kobe beef is called Wagyu beef.",
    "Japan has around 5.5 million vending machines with one on almost every street corner. There are vending machines that sell beer, hot and cold canned coffee, cigarettes, wine, condoms, comic books, hot dogs, light bulbs, bags of rice, toilet paper, umbrellas, fish bait, fresh eggs, porn magazines, and even used women’s underwear.",
    "Japan has the second lowest homicide rate in the world, but it also home to the spooky 'suicide forest' Aokigahara at the base of Mt. Fuji. It is the second most popular place in the world for suicides after San Francisco’s Golden Gate Bridge.",
    "The Japanese have such a low birth rate that there are more adult diapers sold than baby diapers.",
    "Cherry blossoms (sakura) are Japan's national flower.",
    "Japanese ganguro ('black face') fashion was started in the 1990s and has young women tanning their skin as dark as possible, bleaching their hair, and using extremely colorful makeup in contrast to the traditional Japanese pale-skinned, dark-haired standard of beauty.",
    "The world’s shortest escalator is in the basement of More’s department store in Kawasaki, Japan; it has only 5 steps and is 32.8 inches (83.3 cm) high.",
    "Yaeba, or crooked teeth, are considered attractive in Japan—so much so that girls go to the dentist to have their teeth purposefully unstraightened.",
    "Haiku poetry, which was invented in Japan, consists of only three lines and is the world’s shortest poetic form.",
    "Women in ancient Japan blackened their teeth with dye as white teeth were considered ugly. This practice, called ohaguro, continued until the late 1800s.",
    "Shinjuku station, Tokyo’s main train station, is the busiest in the world with over 2 million people passing through it every day.",
    "Anime, or animated Japanese films and television shows, account for 60% of the world’s animation-based entertainment. Animation is so successful in Japan that there are almost 130 voice-acting schools in the country.",
    "Ninety percent of all mobile phones sold in Japan are waterproof because youth like to use them even while showering.",
    "Ninety-eight percent of adoptions that take place in Japan are of male adults, so family businesses can stay within those families.",
    "The sole Japanese man who survived the wreck of the RMS Titanic in 1914, Masabumi Hosono, was called a coward in his country for not dying with the other passengers.",
    "In Japan, it is acceptable to take a nap, called inemuri, on the job—it is viewed as evidence of exhaustion from working very hard.",
    "When bowing, keep enough distance to avoid bumping heads. When Japanese people meet, they traditionally bow instead of shake hands, and the lowest bow shows the deepest respect.",
    "During World War II, Japan bombed China with fleas infested with Bubonic plague.",
    "Japan and Russia still haven’t signed a peace treaty to end World War II due to a dispute over the Kuril Islands.",
    "In Japan, Kit Kat candy bars come in flavors like grilled corn, Camembert cheese, Earl Gray tea, grape, and wasabi. The Japanese pronounce Kit Kat like 'Kitto Katsu,' which sounds like 'You are sure to pass' in Japanese, and so they make a popular gift to students during entrance exam season.",
    "The world’s largest Pokémon memorabilia collection belongs to Lisa Courtney of the United Kingdom. She has 14,410 items as of October 14, 2010, collected over 14 years. Items from her collection come from Japan, the UK, the U.S., and France.",
    "Around 25 billion pairs of waribashi (disposable chopsticks) are used in Japan each year. This is equivalent to the timber needed to build 17,000 homes.",
    "In Japan, black cats are considered good luck charms or omens of good luck.",
    "In Japan, Kentucky Fried Chicken is a typical Christmas Eve feast.",
    "Many hot springs and onsen (public bathhouses) in Japan ban customers with tattoos from entering because the tattoos remind the public of the yakuza, or Japanese mafia, whose members sport full-body tattooing.",
    "Cartooning in Japan began in the 12th century, and today more paper is used for comics than for toilet paper in that country.",
    "In Japan, there is an island full of rabbits called Ōkunoshima. They were brought there during World War II to test the effects of poison gas.",
    "The biggest Japanese community outside of Japan is in Brazil.",
    "Raw horse meat is considered a delicacy in Japan. It is called basashi and is sliced thinly and eaten raw.",
    "Sumo wrestling in Japan can be traced back 1,500 years. Wrestlers weigh 300 pounds or more and train in a heya (room, stable) operated by former sumo champions. Younger sumo wrestlers are traditionally required to clean and bathe the veteran wrestlers, including all the hard-to-reach places.",
    "Hello Kitty was born in Japan in 1974 as a plastic coin purse. More than 20,000 Hello Kitty products are on the market today, including toasters, instant noodles, credit cards, and toilet paper. To her Japanese fans, she is known as Kitty Chan.",
    "Japanese 'love hotels' are short-stay hotels mainly designed for amorous couples and are identified by the presence of heart symbols. They have different room rates: a 'rest' rate as well as an overnight rate. An estimated 2% of Japan’s population visits one each day.",
    "Japanese macaques, or snow monkeys, are the fabled animals that 'see no evil, hear no evil, and speak no evil.' The macaques in northern Honshu live farther north than any other monkey in the world.",
    "It is appropriate to slurp noodles, especially soba (buckwheat), when eating in Japan. Slurping indicates the dish is delicious. It also cools down the hot noodles.",
    "Japan is the largest automobile producer in the world, and the Japanese company Toyota is the third largest automaker in the world. It was founded by Kiichiro Toyoda who changed the 'da' for 'ta' because it sounds clearer. Also, written in Katakana script, 'Toyota' uses 8 brush strokes, a number considered to be lucky in Japan.",
    "Mt. Fuji, or Fujisan or Fujiyama, is the tallest mountain in Japan at 12,388 feet (3,776 m). It is considered a sacred mountain to many Japanese. More than one million people climb Mt. Fuji every year during the official climbing season of July and August.",
    "Tsukiji market in Tokyo is the world’s largest fish market, handling over 2,000 tons of marine products daily.",
    "Hadaka Matsuri, or Naked Festival, is a kind of festival where thousands of Japanese men remove their clothing in public due to the belief that a naked man has a greater ability to absorb evil spirits. Only the most intimate parts of the body are covered with a cloth called a fundoshi.",
    "The word Japanese karaoke means 'empty orchestra.' Cabaret singer Daisuke Inoue made a coin-operated machine that played his songs on tape so his fans could sing along in the 1970s, but he failed to patent his creation and therefore never cashed in on his invention.",
    "Widespread inbreeding of dogs in Japan has resulted in one of the highest rates of genetic defects for canines in the world.",
    "The green traffic light in Japan is called ao shingō, or 'blue.'",
    "In Japan, it is considered rude to tear the wrapping paper off of a gift.",
    "The Japanese have more pets than children.",
    "Baseball is the most popular sport in Japan. Known as yakyū, it was introduced to Japan by an American teacher named Horace Wilson. The first game was played in Japan in 1873 at Tokyo University. Japan has two professional baseball leagues, the Pacific and Central. The game is so popular that even high school games are broadcast on national TV.",
    "The Japanese invented shibari, or sexual bondage play, which may have begun as the martial art of restraint known as hojōjutsu, in which a samurai practices capturing or detaining his enemy with ropes in the least amount of time possible.",
    "The first geishas were actually men, called taikomochi, and they had a role similar to court jesters. Geisha in Japanese means 'person of the arts,' and the first geishas were actually men called taikomochi and they had a role similar to Western court jesters.",
    "Noh drama is the oldest surviving theatrical form in the world, dating back to the 14th century. In this drama, all female characters wear elaborate masks while the male characters do not.",
    "Karate is perhaps the best known martial arts form to have come out of Japan. It originated in China but was refined in Okinawa. It literally means 'empty hands' and uses trained movements of the hands, arms, and legs for self-defense. An estimated 50 million people worldwide practice karate.",
    "The first man born outside of Japan to compete as a sumo wrestler was a second-generation Japanese American who went by the sumo ring name Sendagawa. He made his debut in October 1915.",
    "The term harakiri may be familiar to Westerners as a gruesome Japanese method of suicide which literally means 'cutting the belly.' The proper term for suicide performed by cutting one’s abdomen open with a knife is seppuku. According to Bushidō, the code of the warrior, a samurai facing defeat was supposed to save his honor by committing seppuku rather than surrendering to his enemy.",
    "The Japanese word for a dog’s barking sound is wan-wan instead of 'bow-wow.' Japan’s Akita breed was developed in the 1600s and was once called the royal dog because the emperors kept Akitas as pets. The most famous of all Akitas was Hachikō. Legend has it he waited 10 years at the Shibuya train station in Tokyo for his master who had died while at work. A statue of Hachikō now stands outside the station as a tribute to his loyalty.",
    "The imperial family of Japan descends from an unbroken lineage of nearly 2,000 years. No other royal family in history has held its position for so long. The first Japanese emperor, Jimmu Tennō, ruled about the time of Christ.",
    "In 1993, Japanese author Yume-Hotaru wrote the world’s first novel written entirely on a cell phone: Maho No I-rando (Magic Island).",
    "To this day, Japan is the only country to ever have a nuclear bomb detonated on its soil. Kumamoto was the original target of the atomic bomb dropped by the U.S. Air Force on Hiroshima. On the day of the flight in April 1945, Kumamoto was covered in clouds, and the bomber passed it by, dropping the bomb on Hiroshima instead.",
    "Godzilla, a huge monster resembling a dinosaur, made his film debut in 1954. In Japan, he is known as Gojira, where he rose from the sea, after being awakened by atomic bomb testing, and attacked Tokyo.",
    "The Japanese religion of Shinto is one of the few religions in the world with a female solar deity.",
    "Many Japanese babies are born with a Mongolian spot (mokohan) on their backs. This harmless birthmark usually fades by the age of 5. It is common in several Asian populations and in Native Americans.",
    "Today, fewer than 200 people in Japan can claim both parents with exclusively Ainu, perhaps the original human inhabitants of Japan, descent. The Ainu do not possess the Y chromosome typically found in the rest of the Japanese population.",
]

@bot.event
async def on_message(message):
    if message.guild is None:
        return

    if message.content.startswith('k!quiz n'):
        _, level, score = message.content.split()
        if int(level[1]) in range(1, 6) and int(score) in range(1, 5):
            return

    if message.channel.id == 1117024608651063377 or message.channel.id == 1118401512478097499 or message.channel.id == 1124293569260310621:

        if message.embeds:
            embed = message.embeds[0]
            or_var = True
            if embed.title and 'Quiz Starting in 5 seconds' in embed.title:
                for field in embed.fields:
                    if field.name == 'Score limit' and field.value in '123456789':
                        or_var = False
                        break
            for n in range(1, 6):
                if embed.title and f'JLPT N{n} Reading Quiz Ended' in embed.title:
                    for field in embed.fields[::-1]:
                        if field.name.startswith('Unanswered Questions'):
                            unanswered_questions = eval(field.name.split(' ')[-1])
                            if unanswered_questions is None or unanswered_questions <= 3:
                                await give_reward_role_to_last_sent_msg_of_user(message.channel, f'JLPT N{n}', or_var)
                            return
                        elif field.name == 'Final Scores':
                            await give_reward_role_to_last_sent_msg_of_user(message.channel, f'JLPT N{n}', or_var)
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

@bot.command()
async def ping(ctx):
    latency = bot.latency * 1000
    await ctx.send(f'Pong!! 現在のPing値は{latency:.2f}msです.')

@bot.command()
async def mamechisiki(ctx):
    random_fact = random.choice(fun_facts)
    await ctx.send(random_fact)

@app.route('/')
async def home():
    return "I'm alive"

TOKEN = os.getenv("DISCORD_TOKEN")
PORT = os.environ.get('PORT')

@bot.event
async def on_ready():
    bot.loop.create_task(app.run_task('0.0.0.0', PORT))

bot.run(TOKEN)
