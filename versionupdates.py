"""#Main 0.0.1

#Discord Import
import asyncio 
import discord 
from discord.ext import commands

#bot (Fresh Bot)
bot = commands.Bot(command_prefix="!",case_insensitive=True)


#Event to know when the bot is live
@bot.event
async def on_ready():
    print("Bot is active")

#Function event to send a distinct message when someone says a certain phrase
@bot.event
async def on_message(message):
    # so the bot doesn't reply to its own message
    if message.author == bot.user:
        return

    if  message.content.lower() == "I AM".lower():
        await message.channel.send("banging myo's mom ;)")
   
#Run bot in the server
bot.run('ODkxOTMyMjQ2MzAxMzQ3ODUw.YVFiog.ZjFkUIXalxsyeU9JvTCv-lzGJLk')

if message.content.lower().startwith("i am"):
    msg = message.content[4:]
    await message.channel.send(f"Hello {msg}! I am Freshbot")
"""
#==============================================================================================================================
''' 0.0.2
#Discord Import
import asyncio 
import discord 
from discord.ext import commands
from discord.user import User

#Main



#bot (Fresh Bot)
bot = commands.Bot(command_prefix="!",case_insensitive=True)



@bot.event
#Event to know when the bot is live
async def on_ready():
    print("Bot is active")



@bot.event
#Function event to send a distinct message when someone says a certain phrase
async def on_message(message):
    # so the bot doesn't reply to its own message
    if message.author == bot.user:
        return
    if message.author.id == 317144947880886274:
        await message.reply("Go Study")
    if message.author.id == 349248018790481921:
        await message.reply("You're gay")


    else:
        messagesplit = message.content.lower().split()
        if message.content.lower() == "I AM".lower():
            await message.channel.send("Madly in love with you I'm just shy")

        elif message.content.lower().__contains__("imma"):
            await message.channel.send("how about you go get some bitches <:EZ:829421203247726592>")

        elif message.content.lower().startswith("i am"):
            msg = message.content[4:]
            await message.channel.send(f"Hello{msg}! I am Freshbot")
        
#@bot.event
# More to do with Pinging users, maybe when a certain user joins vc, it joins vc
# Could also get into the command prompts


#Run bot in the server
bot.run('ODkxOTMyMjQ2MzAxMzQ3ODUw.YVFiog.ZjFkUIXalxsyeU9JvTCv-lzGJLk')
'''
#==============================================================================================================================
''' Verison 0.0.3
#Imports
import asyncio 
import discord
from discord import member 
from discord.ext import commands
from discord.user import User
from InformationVariables import BasementUserIds 
from InformationVariables import flame
import random
from InformationVariables import Hype





#Bot command prefix (Fresh Bot)
bot = commands.Bot(command_prefix="!",case_insensitive=True)



@bot.event
#Event to know when the bot is live
async def on_ready():
    print("Bot is active")



@bot.event
#Function event to send a distinct message when a user sends a message
async def on_message(message):
    
    # so the bot doesn't reply to its own message
    if message.author == bot.user:
        return
    #Responses to certain phrases any user says
    #Notes: Make it that so long as message contains im, it works...maybe
    #See if i can make another function instead of having one big one for the above stuff too
    #or maybe just leave it idk 
    else:
        if message.content.lower().__contains__("imma"):
            await message.reply("how about you go get some bitches <:EZ:829421203247726592>")

        if message.content.lower().__contains__("ily ") or message.content.lower() == "ily".lower():
            await message.reply("ily babe <:kissing_heart:894543339460919347>")

        #if message.content.lower() == "no u".lower():
            #await message.reply("no u")

        
        return await bot.process_commands(message)


    #Because of on_message this has to be here to see if the message is actually a command
    #await bot.process_commands(message)







#Bot commands

#Roast Command to roast a specified user
@bot.command()
async def roast(ctx: commands.Context, user: discord.Member):
    if ctx.author == bot.user:
        return
    Roasted = flame[random.randint(0,len(flame)-1)]
    await ctx.send(f"{Roasted} {user.mention}")

#Hype Command to Hype a specified user
@bot.command()
async def hype(ctx : commands.Context, user:discord.Member):
    if ctx.author == bot.user:
        return
    Hyped = Hype[random.randint(0,len(Hype)-1)]
    await ctx.send(f"{Hyped} {user.mention}")
    

#Nobody asked command
@bot.command()
async def whoasked(ctx : commands.Context):
    if ctx.author == bot.user:
        return
    await ctx.send("https://youtu.be/suR7dIwARbY?t=0m26s")
    





#Runs bot
bot.run('ODkxOTMyMjQ2MzAxMzQ3ODUw.YVFiog.ZjFkUIXalxsyeU9JvTCv-lzGJLk')
#----------------------------------------------------------------------------------------

# Quick Access

# Basement User Ids:
"""
Fresh = 680164554952671234
Nathan = 485138947115057162
Ham = 222865938771345408
Ray = 317144947880886274
Fool = 349248018790481921
Myo = 302565282373697537
Suka = 281621038771732481
Leafy = 447534259708624906
Robert = 97175023155953664
Aaron = 155842684412624898
Noura = 616148871499874310
Momo = 697644327291191369
Cliff = 140329621307654144
Surprise = 248909528387551233
Gta = 741341438926651422
Aco = 723901906904154193
Tubs = 555085307431747584
Res = 466169694060281858
Planets = 726387978745806961
"""
# Dev Notes

    #October 3rd-4th, 2021
    # User ids need to be declared and initialized at the top before use otherwise it doesn't work
    # probably going to put them in a seperate file, have a hash map or dictionary for that file
    # import that hashmap or dicionary and then yeah
    # UPDATE
    # Did it with a dictionary which is literally basically a hashmap

    #October 4th-5th, 2021
    # Ok so we moved to commands! Right now I have roast command and whoasked command. Kinda funky at first
    # but then I asked Nathan for help and it's actually super simple also he told me that the easiest place
    # to get info for my bot is hamood github so I can checked that out if im stuck.
    # Good progress so far, I just gotta fix a couple bugs maybe even buff out a couple things and yeah
    # Honestly this was the goal for the end of the week and now maybe it's time to move on to my main goal:
    # Guess the quote 


# To be Toxic:

    #if message.author.id == 317144947880886274:
        #await message.reply("Ok Ray")

'''
#==============================================================================================================================
''' Version 0.0.4
#Imports
import asyncio 
import discord
from discord import member 
from discord.ext import commands
from discord.ext.commands.context import Context
from discord.ext.commands.core import Command
from discord.user import User
from InformationVariables import BasementUserIds 
from InformationVariables import flame
import random
from InformationVariables import Hype
from InformationVariables import freshsaddness




#Bot command prefix (Fresh Bot)
bot = commands.Bot(command_prefix="!",case_insensitive=True)


#Event to know when the bot is live
@bot.event
async def on_ready():
    print("Bot is active")



#Function event to send a distinct message when a user sends a message
@bot.event
async def on_message(message):
    # so the bot doesn't reply to its own message
    if message.author == bot.user:
        return
    #Responses to certain phrases any user says
    else:
        if message.content.lower().__contains__("imma"):
            await message.reply("how about you go get some bitches <:EZ:829421203247726592>")

        if message.content.lower().__contains__("ily ") or message.content.lower() == "ily".lower():
            await message.reply("ily babe <:kissing_heart:894543339460919347>")

        #Because of on_message this has to be here to see if the message is actually a command
        return await bot.process_commands(message)





#Bot commands
#-----------------------------------------------------------------------------------------------------------

#Roast Command to roast a specified user
@bot.command()
async def roast(ctx: commands.Context, user: discord.Member):
    if ctx.author == bot.user:
        return
    Roasted = flame[random.randint(0,len(flame)-1)]
    await ctx.send(f"{Roasted} {user.mention}")

#Hype Command to Hype a specified user
@bot.command()
async def hype(ctx : commands.Context, user:discord.Member):
    if ctx.author == bot.user:
        return
    Hyped = Hype[random.randint(0,len(Hype)-1)]
    await ctx.send(f"{Hyped} {user.mention}")

#Fresh sad command
@bot.command()
async def freshsad(ctx:commands.Context):
    bigsad = freshsaddness[random.randint(0,len(freshsaddness)-1)]
    if ctx.author == bot.user:
        return
    elif ctx.author.id != BasementUserIds.get('Fresh'):
        await ctx.send(f"<@680164554952671234> {bigsad}")
    await ctx.reply(f"{bigsad}")

#Nobody asked command
@bot.command()
async def whoasked(ctx : commands.Context):
    if ctx.author == bot.user:
        return
    await ctx.send("https://youtu.be/suR7dIwARbY?t=0m26s")

#Kanye jail command
@bot.command()
async def jail(ctx:commands.Context):
    if ctx.author == bot.user:
        return
    await ctx.send("https://i.redd.it/h20r5femjeh71.jpg")

#8bit command
@bot.command()
async def viiibit(ctx:commands.Context):
    if ctx.author == bot.user:
        return
    await ctx.send("https://i.imgur.com/R2FLyA3.png")

#Add Depressing quote to freshbot
#Need to get it to add permenantely 
@bot.command()
async def addfreshsad(ctx:commands.Context,*,addedsad:commands.clean_content):
    if ctx.author == bot.user:
       return
    freshsaddness.append(addedsad)
    await ctx.send("Saddness has been added")





#Runs bot and contains bot token, see what to do with this later
bot.run('ODkxOTMyMjQ2MzAxMzQ3ODUw.YVFiog.ZjFkUIXalxsyeU9JvTCv-lzGJLk')
#----------------------------------------------------------------------------------------

# Quick Access

# Basement User Ids:
    #*Check versionupdates or InformationVariables


# Dev Notes/log

    #October 3rd-4th, 2021
    # User ids need to be declared and initialized at the top before use otherwise it doesn't work
    # probably going to put them in a seperate file, have a hash map or dictionary for that file
    # import that hashmap or dicionary and then yeah
    # UPDATE
    # Did it with a dictionary which is literally basically a hashmap

    #October 4th-5th, 2021
    # Ok so we moved to commands! Right now I have roast command and whoasked command. Kinda funky at first
    # but then I asked Nathan for help and it's actually super simple also he told me that the easiest place
    # to get info for my bot is hamood github so I can checked that out if im stuck.
    # Good progress so far, I just gotta fix a couple bugs maybe even buff out a couple things and yeah
    # Honestly this was the goal for the end of the week and now maybe it's time to move on to my main goal:
    # Guess the quote 

    #October 5th-6th, 2021
    # Haven't done much today, just organized my code a bit, fixed a couple bugs and yeah. Also fixed some spelling errors,
    # Deleted some unnessary code, added some new roasts oh yeah I also added a hype command to gas up a selected user.
    # I was thinking about adding other commands like sus, flirt, personalroast, addpersonalroast, addroast,
    # reminders, 8bit or croc, and some other stuff. Commands are cool but I have to explore some other stuff to
    # To make the bot cooler, obi FreshBot will never be like hamood with the currency system, error handling, games and 
    # so much other stuff, but for now I kinda wanna keep him cool, simple and lowkey like !roast is fun and simple.
    # Gotta ask Nathan for some other cool ideas for commands or anything else 
    # But that's it for now, honestly wanted to add more to hype and roasts but it already 6:19am
    # So goodnight ig maybe 


# To be Toxic:

    #if message.author.id == 317144947880886274:
        #await message.reply("Ok Ray")
'''
#======================================================================================================================================
''' Verison 0.0.5
#Imports
import asyncio
from re import I 
import discord
from discord import member 
from discord.ext import commands
from discord.ext.commands import context
from discord.ext.commands.context import Context
from discord.ext.commands.core import Command, check
from discord.user import User
from InformationVariables import BasementUserIds 
from InformationVariables import flame
import random
from InformationVariables import Hype
from InformationVariables import freshsaddness




#Bot command prefix (Fresh Bot)
bot = commands.Bot(command_prefix="!",case_insensitive=True)


#Event to know when the bot is live
@bot.event
async def on_ready():
    print("Bot is active")



#Function event to send a distinct message when a user sends a message
@bot.event
async def on_message(message):
    # so the bot doesn't reply to its own message
    if message.author == bot.user:
        return
    #Responses to certain phrases any user says
    else:
        if message.content.lower().__contains__("imma"):
            await message.reply("how about you go get some bitches <:EZ:829421203247726592>")

        if message.content.lower().__contains__("ily ") or message.content.lower() == "ily".lower():
            await message.reply("ily babe <:kissing_heart:894543339460919347>")

        #Because of on_message this has to be here to see if the message is actually a command
        return await bot.process_commands(message)





#Bot commands
#-----------------------------------------------------------------------------------------------------------

#Roast Command to roast a specified user
@bot.command()
async def roast(ctx: commands.Context, user: discord.Member):
    Roasted = flame[random.randint(0,len(flame)-1)]
    await ctx.send(f"{Roasted} {user.mention}")

#Add to roasts to roast command
@bot.command()
async def addroast(ctx:commands.Context,*, addroast:commands.clean_content):
    flame.append(addroast)
    await ctx.reply(f"Your Roast '{addroast}' has been added")

#Hype Command to Hype a specified user
@bot.command()
async def hype(ctx : commands.Context, user:discord.Member):
    Hyped = Hype[random.randint(0,len(Hype)-1)]
    await ctx.send(f"{Hyped} {user.mention}")

#Add to roasts to roast command
@bot.command()
async def addhype(ctx:commands.Context,*, addhype:commands.clean_content):
    Hype.append(addhype)
    await ctx.reply(f"Your Hype '{addhype}' has been added")

#Fresh sad command
@bot.command()
async def freshsad(ctx:commands.Context):
    bigsad = freshsaddness[random.randint(0,len(freshsaddness)-1)]
    if ctx.author.id != BasementUserIds.get('Fresh'):
        await ctx.send(f"<@680164554952671234> {bigsad}")
    await ctx.reply(f"{bigsad}")

#Add Depressing quote to freshbot
#Need to get it to add permenantely 
@bot.command()
async def addfreshsad(ctx:commands.Context,*,addsad:commands.clean_content):
    freshsaddness.append(addsad)
    await ctx.reply("Saddness has been added")

#K-Drama command to ping anyone who wants to watch K-Dramas and get notified 
#Function could be better than what i got rn
#Also make it such that if no message is passed, it can ping all members
@bot.command()
async def kdramatics(ctx:commands.Context,*,message:commands.clean_content):
    #Hard coded Members of kdramatics usign basement id list while making the ids into string
    kdramawatchersid = [str(BasementUserIds.get('Fresh')),str(BasementUserIds.get('Momo')),
    str(BasementUserIds.get('Ham')),str(BasementUserIds.get('Myo'))]
    
    #for loop going through the list of members and adding the elements to make it a pingable string
    #for discord and then appending that to the pingable string that contains the pingable members
    kdramawatchersidping = ""
    for i in kdramawatchersid:
        i = "<@" + i + ">" + " "
        kdramawatchersidping += i
    await ctx.send(f"{kdramawatchersidping}{message}")







#practically for memes commands or comedical ease

#Nobody asked command
@bot.command()
async def whoasked(ctx : commands.Context):
    await ctx.send("https://youtu.be/suR7dIwARbY?t=0m26s")

#Kanye jail command
@bot.command()
async def jail(ctx:commands.Context):
    await ctx.send("https://i.redd.it/h20r5femjeh71.jpg")

#8bit command
@bot.command()
async def viiibit(ctx:commands.Context):
    await ctx.send("https://i.imgur.com/R2FLyA3.png")

#bahoo t-pose
@bot.command()
async def bahoo(ctx:commands.Context):
    await ctx.reply("https://cdn.discordapp.com/attachments/829072008733261834/895890602028322826/images.png")

#Astrology command
@bot.command()
async def astrology(ctx:commands.Context):
    await ctx.reply("Astrology is fake and if you don't agree then go read a book you talentless fiend. \n You actual goofy ball go find a meaningful fucking hobby better yet go fucking study something, go get a meaningful degree")



#Help commands soon



#Runs bot and contains bot token, see what to do with this later
bot.run('ODkxOTMyMjQ2MzAxMzQ3ODUw.YVFiog.ZjFkUIXalxsyeU9JvTCv-lzGJLk')
#----------------------------------------------------------------------------------------

# Quick Access

# Basement User Ids:
    #*Check versionupdates or InformationVariables


# Dev Notes/log

    #October 3rd-4th, 2021
    # User ids need to be declared and initialized at the top before use otherwise it doesn't work
    # probably going to put them in a seperate file, have a hash map or dictionary for that file
    # import that hashmap or dicionary and then yeah
    # UPDATE
    # Did it with a dictionary which is literally basically a hashmap

    #October 4th-5th, 2021
    # Ok so we moved to commands! Right now I have roast command and whoasked command. Kinda funky at first
    # but then I asked Nathan for help and it's actually super simple also he told me that the easiest place
    # to get info for my bot is hamood github so I can checked that out if im stuck.
    # Good progress so far, I just gotta fix a couple bugs maybe even buff out a couple things and yeah
    # Honestly this was the goal for the end of the week and now maybe it's time to move on to my main goal:
    # Guess the quote 

    #October 5th-6th, 2021
    # Haven't done much today, just organized my code a bit, fixed a couple bugs and yeah. Also fixed some spelling errors,
    # Deleted some unnessary code, added some new roasts oh yeah I also added a hype command to gas up a selected user.
    # I was thinking about adding other commands like sus, flirt, personalroast, addpersonalroast, addroast,
    # reminders, 8bit or croc, and some other stuff. Commands are cool but I have to explore some other stuff to
    # To make the bot cooler, obi FreshBot will never be like hamood with the currency system, error handling, games and 
    # so much other stuff, but for now I kinda wanna keep him cool, simple and lowkey like !roast is fun and simple.
    # Gotta ask Nathan for some other cool ideas for commands or anything else 
    # But that's it for now, honestly wanted to add more to hype and roasts but it already 6:19am
    # So goodnight ig maybe 

    #October 6th-9th
    #Ok so haven't been logging much, there are a couple new things I have done. Added new roasts and hypes,
    #added a freshsad command just went im sad ig to remind myself that Im used to being sad so it all good
    #also addfreshsaddness cause idk just in case im missing something and want to add it on the fly or if
    #someone else wants to add something. Also added an Addroast command and Addhype command although despite
    #that they get cleared after I re-run the bot so I got to make such that they hard code them in
    #also what I was working on today was making a kdrama command to ping members in the basement server who
    #watch kdrama and want to ping others to make plans since no one adding the role. Yeah ig thats all im doing
    #rn. It's another late night 5:23 rn so i should probably go to sleep soon. Oh also gotta work on the help
    #commands soon so people know what they do. But yeah that's it for now. GN ME!:)


# To be Toxic:

    #if message.author.id == 317144947880886274:
        #await message.reply("Ok Ray")
'''