import discord
import asyncio
import pytz
from datetime import datetime
from discord.ext import commands
import os
from dotenv import load_dotenv
import random

load_dotenv()
import time
from tqdm import tqdm

intents = discord.Intents.all()
client = discord.Client(intents=discord.Intents.all())
client = commands.Bot(command_prefix=":", intents=intents)



@client.event
async def on_ready():
    for _ in tqdm(range(100),
                  desc="Loading...",
                  ascii=False, ncols=75):
        time.sleep(0.01)

    print('beep boop is it working?')
    #client.loop.create_task(my_background_task())
    client.loop.create_task(hourly_reminder())

@client.command()
async def poke(ctx, user: discord.Member):
    gifs = ["https://media.giphy.com/media/CK0Eg2ymtfzTO2yVJD/giphy.gif",
            "https://media.giphy.com/media/3o7bucYmhdKl9POfcs/giphy.gif",
            "https://media.giphy.com/media/1gQwMNJ9z1mqABgQd3/giphy.gif",
            "https://media.giphy.com/media/QVI2faNSfJlUQEIgzv/giphy.gif"]
    gif = random.choice(gifs)
    embed = discord.Embed(title="Poke!", description=f"{ctx.author.mention} pokes {user.mention}", color=0xC076C9)
    embed.set_image(url=gif)
    await ctx.send(embed=embed)



@client.event
async def on_message(message):
    rand = random.randint(1, 3)
    if message.author == client.user:
        return
    # fuck you
    if message.content.lower() in [
        "fuckyou", "fuck you", "fuck u",
        "fuckyoutoo", "fuck you too", "fuck u too",

        "fukyou", "fuk you", "fuk u",
        "fukyoutoo", "fuk you too", "fuk u too",

        "fuccyou", "fucc you", "fucc u",
        "fuccyoutoo", "fucc you too", "fucc u too",

        "faqyou", "faq you", "faq u",
        "faqyoutoo", "faq you too", "faq u too",
        "fokyou", "fok you", "fok u",
        "fokyoutoo", "fok you too", "fok u too"]:
        user = message.author
        await message.channel.send(f'fuck you too {user.mention}')
    elif message.content.lower() == 'fuck':
        user = message.author
        await message.channel.send(f'{user.mention} stop saying fuck')
    elif message.content.lower() in [
        "fucc", "fuc", "fok", "faq"
    ]:
        user = message.author
        await message.channel.send(f'{user.mention} stop saying fuck in a different spelling')
    #input randomizer here
    elif message.content.lower() == 'hi':
        if rand == 1:
            user = message.author
            # mention the user in the bot's response
            await message.channel.send(f'Hello, {user.mention}')
        elif rand == 2:
            user = message.author
            # mention the user in the bot's response
            await message.channel.send(f'wassup, {user.mention}')
        elif rand == 3:
            user = message.author
            # mention the user in the bot's response
            await message.channel.send(f'yo, {user.mention}')


    elif message.content.lower() == 'hello':
        if rand == 1:
            user = message.author
            # mention the user in the bot's response
            await message.channel.send(f'hi, {user.mention}')
        elif rand == 2:
            user = message.author
            # mention the user in the bot's response
            await message.channel.send(f'wassup, {user.mention}')
        elif rand == 3:
            user = message.author
            # mention the user in the bot's response
            await message.channel.send(f'yo, {user.mention}')


    elif "why" in message.content.lower():
        await message.reply("because fuck you")



    elif message.content.lower() in [
        "stfu bot", "shut up bot", "stupid bot", "stfu"]:
        user = message.author
        await message.channel.send(f'heh {user.mention}')


    elif "<:XDBIG:" in message.content:
        await message.reply("xD")
    elif "<:tsukided:" in message.content:
        await message.reply("ded")


    elif "frick" in message.content.lower():
        await message.reply("what is frick")

    elif "@everyone" in message.content:
        # do something when @everyone is mentioned
        await message.channel.send("why calling everyone?")


    if message.content.startswith('$time'):
        # Send a message asking the user to enter their country
        await message.channel.send("Please enter your country(use abbreviation e.g. Us, Ph, Jp):")

        # Wait for the user's response
        def check(msg):
            return msg.author == message.author and msg.channel == message.channel

        response = await client.wait_for('message', check=check)

        # Determine the time zone for the user's country
        try:
            country_tz = pytz.country_timezones[response.content.upper()][0]
            user_tz = pytz.timezone(country_tz)
        except KeyError:
            await message.channel.send("Invalid country. Please try again.")
            return

        # Get the current time in the user's time zone
        user_time = datetime.now(user_tz).strftime('%H:%M:%S %Z')

        # Send the user's time zone and current time as a message
        await message.channel.send(f"Your time zone is {user_tz.zone} and the current time is {user_time}")

    elif "what" in message.content.lower():
        await message.reply("deez nuts")

    elif "bye" in message.content.lower():
        await message.reply("goodbye")
#mention me the bot will respond
    if message.author != client.user:
        # Check if the specified user is mentioned
        if f"@{552811316927004683}" in message.content:
            # Send the response message
            await message.channel.send("Why?")
    await client.process_commands(message)



messages = ["wassap", "kamusta kaibigan?", "hello", "sup", "drink water"]
messages_hr =["hourly reminder to drink water!"]

#async def my_background_task():
    #await client.wait_until_ready()
#    channel = client.get_channel(1097132163775877160) # replace `channel_id` with the actual channel ID
 #   while not client.is_closed():
  #      message = random.choice(messages) # choose a random message from the list
   #     await channel.send(message)
    #    await asyncio.sleep(90) # wait for 10 minutes



async def hourly_reminder():
    await client.wait_until_ready()
    channel = client.get_channel(571277843129171970) # replace `channel_id` with the actual channel ID
    while not client.is_closed():
        message_hr = random.choice(messages_hr)
        await channel.send(message_hr)
        await asyncio.sleep(3600)


api_key = os.environ.get('API_KEY')
client.run(api_key)
