#Imports:
#---------------
from operator import index
import asyncio
from re import I 
import discord 
from discord.ext import commands
from discord.ext.commands.flags import F
from discord.user import User
from InformationVariables import BasementUserIds
from InformationVariables import flame
import random
from InformationVariables import Hype

#Choyon Uddin
#Fresh bot
#Est. September 28th 2021


#Dev Head Guide:
#---------------
# Imports and project title
# Weekly log
# Random testing code
# Code Archive (Unorganized)
# Code Bank (TBM)
# Notes (TBD)



#Weekly Logs:
#---------------

#September 28th 2021
#This will be where I plan my ideas ig for my first bot, honestly looking forward to it

#October 4th, 2021 
#"Ok so this is going pretty Well. It's been almost been a week since I started working on the bot and its
# pretty fun and adicitive. There are some day where I just work on my bot instead of doing school work which is 
# not that good but it's whatever, I'll catch up... eventually. Right now I've got a function where Freshbot
# sends a message when im, imma, and i am i sent by any user, and in the same function which im trying to make into
# two seperate functions, an auto reply to whenever a specific user talks. Going well, I'm looking to move toward commands 
# next and possible even more trolling ig lmao. But yeah lets see how it goes. Oh also gotta do this weekly update log, That 
# might help. Ig also organizing it which I Might do now"



#Random Testing Code
# ---------------
print(BasementUserIds.keys("Fresh"))

#Archived code
#---------------

'''
Random code archive
=================================================
line = "i am good".lower()
linesplit = line.lower().split()
messagesplit = message.content.lower().split()
# do an else statement if it doesn't contain segments

if linesplit.__contains__("i") == False or linesplit.__contains__("am") == False:
    print(False)

elif (linesplit.index("i") - linesplit.index("am") == -1) and (len(linesplit)-1 > linesplit.index("am")):
    print("Hello,", linesplit[linesplit.index("am") + 1], "I am Freshbot")

#print(linesplit)

def func():
    Roasted = flame[random.randint(0,len(flame)-1)]
    print(Roasted)
func()

-----------------------------------------
Used Archived code:
messagesplit = message.content.lower().split()

-----------------------------------------
'''



#Code Bank Archive
#---------------
#if message.author.id == BasementUserIds.get('Ham'):
    #if message.content.lower() == "sigh".lower():
        #await message.reply("sigh")

#if message.content.lower().startswith("im "):
    #msg = message.content[2:]
    #await message.reply(f"Hello{msg}! I am Freshbot")
        


#Dev Notes
#---------------
#Figure out how to invite freshbot to servers more easily
#need to get a way to find out how large or fast my programs are using python
#goal for next time is the commands probs start with a simply one like !roast @user and !selfroast
#basically roasts using a line from a list of insults. Maybe even a 2d array or potentially a nested dictonary
#How to add to roast and hype properly 
#Get Better code for kdramatics command so that it doesn't always need a message parameter
#Get to work on help commands



#Questions to ask Nathan or anyone else
#Even if a function have 2 parameter args, is it possible to give 1 and still have it run Ex: if you 
    #where to do !hype instead of !hype @user, it would simply reply to you instead?

#If I have multiple imports from 1 file, can combined them in one from file line
#If I can have 2 of the same function ex: on_message
#If I can use emotes from another server even if the bot isn't in that server
#How I can have bot.run seperate from main and hid bot token