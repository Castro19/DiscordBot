import discord # Recieve the libraries from Discord
import random # Imports randmized Numbers?
import asyncio
from discord.ext import commands
from asyncio import sleep as s

# Specialized Token for this Discord Bot
TOKEN = 'MTAwMDA5NTUzMzI5NTIxODg1OA.GGrfWD.MRwRPxd_OY-nnTZLVfAWlOObfX49NfrOw7NEVA'

# Create a Client
client = discord.Client()

# Create a Client Event
@client.event

# Define event as an Asyc Function ()
async def on_ready(): #on_ready means this function will be called immediately when the Bot starts
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message): #on_message means that we take a message as a parameter
    username = str(message.author).split('#')[0] # Only saving the Name of User & not their ID #4532
    user_message = str(message.content) # The user message
    channel = str(message.channel.name) # The Channel message was sent on
    print(f'{username}: {user_message} ({channel})')

    # IMPORTANT 
    if message.author == client.user: # SO we dont get trapped in a never ending Loop
        return
    
    # Just TESTING
    if message.channel.name == 'testing': # If the message was sent in the channel: Testing
        if user_message.lower() == 'hello': 
            # This format just sends a regular message
            await message.channel.send(f'Hello {username}!')
            return
        elif user_message.lower() == 'bye':
            await message.channel.send(f'See you later {username}!')
            return
        elif user_message.lower() == '!random':
            response = f'This is your random number: {random.randrange(1000000)}'
            await message.channel.send(response)
            return
    
    # Need More Ideas on what Commands Financial Aid should have
    if message.channel.name == 'financial-aid':
        if user_message.lower() == '!commands':
            embed = discord.Embed() # makes the message an embed (Looks a lot cleaner)
            embed.description = '**TYPE:**\n**“`!fafsa`“** --> *To view basic information about the FAFSA\n\n**“`!howToFafsa`"** --> *To view a step by step guide on how to submit the FAFSA!*\n\n**"`!scholarships`"** --> *To view a list of available scholarships*\n\n**“`!contact`“** --> *To view the contact information of the Financial Aid Office\n\n**“`!info`“** --> *To view basic information on how financial aid can cover your tuition costs and send cash grants to help pay for books, supplies, and etc.'
            await message.channel.send(embed=embed)     
            return 
        # The above 4 lines are needed to send a message in an embed format 
        elif user_message.lower() == '!scholarships':
            # FIX & ADD CCC Scholarship link and a file w other scholarships (make embed too)
            await message.channel.send(f'Hello {username}, here are the available scholarships: !')
            return
        elif user_message.lower() == '!fafsa':
            # Give basic info on FAFSA 
            embed = discord.Embed() 
            embed.description = 'The **[FAFSA](https://studentaid.gov/)** 2022 - 2023 is open!\nPlease submit the FAFSA form to see if you qualify for a fee-waiver or cash grants! This form needs to be completed once a year.'
            await message.channel.send(embed=embed)  
            return
        elif user_message.lower() == '!contact':
            embed = discord.Embed() 
            embed.description = 'The **[Financial Aid Office](https://www.cloviscollege.edu/admissions-and-aid/financial-aid/index.html)** is here to provide assitance to all students who need help or have questions regarding their financial aid status\n\n**Contact Informaion:**\n*Email:* clovis.financialaid@cloviscollege.edu\n*Phone Number:* (559)325-5239\n\n*Location:* AC2-141\n*Hours:* Monday - Friday (8:00AM - 5:00PM)'
            await message.channel.send(embed=embed)  
            return
        elif user_message.lower() == '!info':
            embed = discord.Embed() 
            embed.description = 'To receive Financial Aid, you must complete the the 2022 - 2023 FAFSA form! This is the only form you need to complete to see if you might qualify for a fee-waiver, Pell Grant, or Cal Grant. This form needs to be renewed every school year, and NOT each semester. '
            await message.channel.send(embed=embed)  
            return

   # Commands for Clubs is done & Template is made. We just need more clubs!
    if message.channel.name == 'clubs':
        # Important lines of code that shows what the commands are for each channel
        if user_message.lower() == '!commands':
            embed = discord.Embed() # makes the message an embed (Looks a lot cleaner)
            embed.description = '**TYPE:**\n**"!Clubs"** --> *To view a list of all available clubs!*\n\n**"!MakeClub"** --> *To view a step by step guide on how to make a club*\n\n**"!ClubEvents"** --> *To view upcoming club events, rushes, and etc.*'
            await message.channel.send(embed=embed)     
            return 
        elif user_message.lower() == '!clubs':
            embed = discord.Embed()
            # CHange font Color of (!)
            embed.description = '*List of Available Clubs:*\n**(!amc)** *Active Minds Club:* Particpates in mental health awareness... \n\n**(!asg)** *Associated Student Government:* Represents the voice of the students & is involved with other student organizations \n\n**(!econ)** *Crush Economics:* Attend networking events, Host speaking events with intership recruiters, and participate in a variety of activities.'
            await message.channel.send(embed=embed)
            return

        # List the Steps to make a club!

        # List upcoming Club Evemts!

        # ALL OF OUR CLUBS:
        elif user_message.lower() == '!amc':
            embed = discord.Embed()
            embed.description = 'The **[Active Minds Club](https://www.cloviscollege.edu/campus-life/clubs-organizations/active-minds.html)** is the... \n\n**Contact Informaion:**\n*Advisor Email:* naomi.forey@cloviscollege.edu\n*Email:* @gmail.com\n*Location:* On Zoom\n\nTo *Join the Active Minds Club* please send an Email to ...'
            await message.channel.send(embed=embed)
            return
        elif user_message.lower() == '!asg':
            embed = discord.Embed()
            embed.description = "*The Associated Student Government* **[ASG](https://www.cloviscollege.edu/campus-life/clubs-organizations/associated-student-government.html)** is the... \n\n**Contact Informaion:**\n*Phone:* (559)325-5235\n*Email:* cccasg@cloviscollege.edu\n*Location:* Student Center, *AC1-160*\n\nTo *Join ASG,* please send an Email to ..."
            await message.channel.send(embed=embed)
            return
        elif user_message.lower() == '!econ':
            embed = discord.Embed()
            embed.description = 'The **[Crush Economics Club](https://www.cloviscollege.edu/campus-life/clubs-organizations/economic-club.html)** is...\n\n**Contact Informaion:**\n*Advisor Email:* sandy.brown@cloviscollege.edu\n*Email:* crusheconccc@gmail.com\n*Location:* On Zoom\n\nTo *Join Econ Crush,* please send an Email to ...\nHere is a Flyer:'
            # ??? How to add this file into our embeded message file = discord.File('crush_econ.heic')) ???
            await message.channel.send(embed=embed)
            return
        ''' CLUB TEMPLATE: 
        elif user_message.lower() == '!CLUB CODENAME':
            embed = discord.Embed()
            embed.description = "The **[CLUB NAME](CLUB URL)** is the... \n\n**Contact Informaion:**\n*Phone:* (559)123-4567\n*Email:* ccc@cloviscollege.edu\n*Location:* Student Center, *AC1-160*\n\nTo *Join CLUB NAME,* please send an Email to ..."
            await message.channel.send(embed=embed)
            return
        '''
         
    # Need More Ideas on what Commands Resources should have:
    if message.channel.name == 'resources':
        if user_message.lower() == '!commands':
            embed = discord.Embed()
            embed.description = '**TYPE:**\n**"!career"** --> *To receive information from our Career Counselors on the skills necessary to find a job!*\n\n**"!counseling"** --> *To recieve information on how to contact a counselor*\n\n**"!tech"** --> *To receive information on how to checkout a laptop, calculator, etc.*'
            await message.channel.send(embed=embed)
            return
        elif user_message.lower() == '!career':
            embed = discord.Embed()
            embed.description = 'The **[Career Center](https://www.cloviscollege.edu/student-services/career-services/index.html)** is here to help you with the career and major exploration process as well as gaining all the skills necessary to find a job in your chosen pathway.\n\n**Contact Informaion:**\n*Email:* careercenter@cloviscollege.edu\n*Phone Number:* (559)325-5398\n\n*Location:* AC2-174\n*Hours:* Monday - Thursday (9:00AM - 6:00PM) & Friday (9:00AM - 5:00PM)'
            await message.channel.send(embed=embed)
            return
        elif user_message.lower() == '!counseling':
            embed = discord.Embed()
            embed.description = 'The **[Counseling Center](https://www.cloviscollege.edu/student-services/academic-counseling/index.html)** provide comprehensive counseling services to assist students toward a successful college experience\n\n**Contact Informaion:**\n*Email:* cccounseling@cloviscollege.edu\n*Phone Number:* (559)325-5230\n\n*Location:* AC2-133\n*Hours:* Monday - Thursday (8:00AM - 6:00PM) & Friday (8:00AM - 5:00PM)'
            await message.channel.send(embed=embed)
            return
        elif user_message.lower() == '!tech':
            embed = discord.Embed()
            embed.description = 'The **[Technology Checkout Program](https://www.cloviscollege.edu/student-services/library/technology-loan-program.html)** Students who are enrolled in CCC classes can check out laptops, webcams, personal hotspots, calculators, headphones, and etc from the Librart\n\n**Contact Informaion:**\n*Email:* library@cloviscollege.edu\n*Phone Number:* (559)325-5215\n\n*Location:* AC2-148'
            await message.channel.send(embed=embed)
            return
        
    # FIX: User should be PM'd a MAP if they type a command in ANY channel
    if user_message.lower() == '!map':
        await message.channel.send('Here is a map of the campus', file = discord.File('map.pdf'))
        return

client.run(TOKEN)



''' FIX the Reminder Bot or create a new one
@client.command()
async def reminder(ctx, time: int, *, msg):
    while True:
        await s(60*time) # Makes this for every minute instead of every hour
        await ctx.send(f'{msg}, {ctx.author.mention}')
'''     

