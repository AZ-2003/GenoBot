import discord
import logging
from os import environ
from discord.ext import commands
from dotenv import load_dotenv
from urllib.request import urlopen

# Importing helper file
from Geno0 import *


# Key Variable declarations

handler= logging.FileHandler(filename='discord.log', encoding = 'utf-8', mode = 'w')

'''
What are intents?
Intents allow the bot to subscribe to events
Here we are subscribing to all events for the bot
'''
intent = discord.Intents.default()
intent.message_content = True

# Creating a Client/Command Instance (*+Function Name)
Bot = commands.Bot(command_prefix='*', intents=intent)

# Obtaining the token from .env (private file)
load_dotenv() # Reading the .env file
token = environ["TOKEN"]


#Recall: async functions involves using "callback"
'''
Description: called when Geno is ready (? might need a better description)
Parameters:no parameters
Returns: no return value
'''
@Bot.event
async def on_ready():
    print(f"Geno logged in as {Bot.user}")
    #print("Geno logged in as {0.user}".format(client))

@Bot.command(name="Call", pass_context = True)
async def Call(ctx):
    await ctx.send("Function Call works!")


'''
Description: allows Geno to join a Voice Channel
Parametrs:
    (1)ctx: short for context
Returns: no return value
'''
#context:
@Bot.command(name="VoiceOn", pass_context = True)
async def VoiceOn(ctx):
    if(ctx.author.voice):
        channel = ctx.author.voice.channel
        await channel.connect()
        await ctx.send("Voice mode on")
    else:
        await ctx.send("Error: You are not in a Voice Channel")

'''
Description: allows Geno to leave a Voice Channel
Parametrs:
    (1)ctx: short for conetxt
Returns: no return value
'''
@Bot.command(name="VoiceOff",pass_context = True)
async def VoiceOff(ctx):
    if(ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("Voice mode off")
    else:
        await ctx.send("Error: I am not in a Voice Channel")

'''
Description: called when particular discord messages are seen
Parametrs:
    (1)message: the user input creating event
Returns: no return value
'''

@Bot.event
async def on_message(message):
    if message.author == Bot.user:
        return
    
    #Calling Geno
    if message.content.startswith("Geno"):
        await message.channel.send("At your service")

    #Asking about the temperature
    if message.content.startswith("Temp"):
        # Given no further text, temperature of select cities is provided
        if(message.content == "Temp"):
            daily_forecast = get_temperature_full()
            for i in cities:
                await message.channel.send(i+":"+daily_forecast[i])
        else:
            #print("Singular city case")
            daily_forecast = get_temperature(message.content.split("Temp ", 1)[1])
            await message.channel.send(message.content.split("Temp ", 1)[1]+":"+ daily_forecast)


    #Thanking Geno
    if message.content.startswith("Thank you"):
        await message.channel.send("An absolute pleasure")

    
    await Bot.process_commands(message)
    
    

#Thought: how many more functions can we add? what will they do ?  
#Thought: Eventually, we would have to break that file into modules 
#Thought: Need to make Geno only listen to *me*
'''
Proposed APIs to incorporate: 
    (1) Google Calender API
    (2) Spotify API 
''' 
# runs the bot 
Bot.run(token, log_handler=handler, log_level=logging.DEBUG)


