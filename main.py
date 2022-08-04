# from pkg_resources import require
# require('dotenv').config()
# ^^^ NEEDED to hide API Token
import discord # receive the libraries from Discord
import random # Imports randmized Numbers?
from dotenv import load_dotenv
import os

load_dotenv()
# environment variables: comp knows w/out initializing variables

# Specialized Token for this Discord Bot
token = os.getenv('bot_token')
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

    # IMPORTANT 0
    if message.author == client.user: # SO we dont get trapped in a never ending Loop
        return

    # Just TESTING
    if message.channel.name == 'testing': # If the message was sent in the channel: Testing
        if user_message.lower() == '!commands':
            embed = discord.Embed() # makes the message an embed (Looks a lot cleaner)
            embed.description = '***TYPE:***\n**`!hello`** \n\n**`!bye`** \n\n`**!random**` --> *To receive a random automated number!*'
            await message.channel.send(embed=embed)     
            return 
        if user_message.lower() == '!hello': 
            # This format just sends a regular message
            await message.channel.send(f'Hello {username}!')
            return
        elif user_message.lower() == '!bye':
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
            embed.description = '***TYPE:***\n**`!fafsa`** --> *To view basic information about the FAFSA*\n\n**`!howToFafsa`** --> *To view a step by step guide on how to submit the FAFSA!*\n\n**`!scholarships`** --> *To view a list of available scholarships*\n\n**`!help`** --> *Please contact the Financial Aid Office if you have any questions regarding your financial aid status!*\n\n**`!info`** --> *To view basic information on how financial aid can cover your tuition costs and send cash grants to help pay for books, supplies, etc.*\n\n**`!requirements`** --> *To view the requirements needed to qualify for Financial Aid*'
            await message.channel.send(embed=embed)     
            return 
        elif user_message.lower() == '!help':
            embed = discord.Embed() 
            embed.description = 'The **[Financial Aid Office](https://www.cloviscollege.edu/admissions-and-aid/financial-aid/index.html)** is here to provide assitance to all students who need help or have questions regarding their financial aid status\n\n**__Contact Information:__**\n***E-mail:*** clovis.financialaid@cloviscollege.edu\n***Phone:***(559)325-5239\n\n***Location:*** AC2-141\n**__Hours:__** Monday - Friday (8:00AM - 5:00PM)'
            await message.channel.send(embed=embed)  
            return
        # The above 4 lines are needed to send a message in an embed format 
        elif user_message.lower() == '!fafsa':
            # Give basic info on FAFSA 
            embed = discord.Embed() 
            embed.description = 'The **[FAFSA](https://studentaid.gov/)** 2022 - 2023 is open!\nPlease submit the FAFSA form to see if you qualify for a fee-waiver or cash grants!'
            await message.channel.send(embed=embed)  
            return
        elif user_message.lower() == '!info':
            embed = discord.Embed() 
            embed.description = 'To receive Financial Aid, you must complete the the 2022 - 2023 FAFSA form! This is the only form you need to complete to see if you might qualify for a fee-waiver, Pell Grant, or Cal Grant. This form needs to be renewed every school year, and NOT each semester. '
            await message.channel.send(embed=embed)  
            return
        elif user_message.lower() == '!scholarships':
            # FIX & ADD CCC Scholarship link and a file w other scholarships (make embed too)
            await message.channel.send(f'Hello {username}, here are the available scholarships: !')
            return
        elif user_message.lower() == '!requirements':
            # Give basic info on FAFSA 
            embed = discord.Embed() 
            embed.description = '**__The requirements to qualify for Financial Aid__**\n\n**Academic requirements (SAP):**\n1.) Maintain at least a cumulative GPA of 2.0\n2.) Complete at least 67% for all total units attempted\n Have attempted less than 150% of the max units required for completion of their degree.\n\nFor any questions, use the command `!help` to view how to contact the Financial Aid Office or visit their [website](https://www.cloviscollege.edu/admissions-and-aid/financial-aid/satisfactory-academic-progress.html) for more details on the requirements'
            await message.channel.send(embed=embed)  
            return

    # Detail a description of each Grant and how it works!
    if message.channel.name == 'grants':
        if user_message.lower() == '!commands':
            embed = discord.Embed() # makes the message an embed (Looks a lot cleaner)
            embed.description = '***TYPE:***\n**`!info`** --> *To view information about what Grants are & how they work!*\n\n**`!dates`** --> *To view the upcoming disbursement dates where we send out the grants!*\n\n**__GRANTS__**\n**`!pell`** --> *To view information about the PELL Grant and how to qualify!*\n\n**`!cal`** --> *To view information about the CalGrant and how to qualify!*\n\n**`!success`** --> *To view information about the Student Success Completion Grant and how to qualify!*\n\n**__FEE-WAIVERS__**\n**`!AB19`** --> *To view information about the AB19 Fee-Waiver and how to qualify!*\n\n**`!promise`** --> *To view information about the the Promise Grant Fee-Waiver and how to qualify!*'
            await message.channel.send(embed=embed)     
            return 
        elif user_message.lower() == '!info':
            embed = discord.Embed() 
            embed.description = 'Grants are sources of financial aid that do **NOT** have to be repaid! Grants are directly sent out in a check form to a student via direct deposit or mail.\n\n**How to Apply for a Grant?**\n\nA student needs to submit the [FAFSA 2022 - 2023](https://studentaid.gov/h/apply-for-aid/fafsa) to be eligible for the CalGrant & Pell Grant. The FAFSA is the only application you need to complete to be eligible for these grants! Once the FAFSA is submitted, the system will determine what grants you will be awarded based on the household income.'
            await message.channel.send(embed=embed)     
            return
        elif user_message.lower() == '!pell':
            embed = discord.Embed() 
            embed.description = 'The [Pell Grant](https://studentaid.gov/understand-aid/types/grants/pell#how-much-money-can-i-get) is a federal grant awarded based on financial need & can be awarded for up to 6 years!\n\n**How much is the Pell Grant?**\nThe maximum amount for the school year 2022-2023 is $6,895, however, the amount you receive will vary depending on if you are a full-time student and your Expected Family Contribution (EFC)\n\n**More Info:**\n - *Full-time (At least 12 units)* --> 100% of the Pell Grant you are eligible for\n - *Three-Quarter-time (9 - 11.5 units)* --> 75% of the Pell Grant you are eligible for\n - *Half-time (6 - 8.5)* --> 50% of the Pell Grant you are eligible for\n - *Less than Half-time (3 - 5.5)* --> 25% of the Pell Grant you are eligible for'
            await message.channel.send(embed=embed)     
            return 
        elif user_message.lower() == '!cal':
            embed = discord.Embed()
            embed.description = 'The [Cal Grant](https://www.cloviscollege.edu/admissions-and-aid/financial-aid/cal-grant.html) is a grant that is funded by the state of California & this grant can be awarded for up to 4 years.\n\n**How much is the Cal Grant?**\nThe maximum amount for the school year 2022-2023 is $1,624, however the amount will vary depending on if you are a full-time student\n\n**More Info:**\nThe CalGrant A, CalGrant B, CalGrant C...'
            await message.channel.send(embed=embed)     
            return 
        elif user_message.lower() == '!success':
            embed = discord.Embed() 
            embed.description = 'The [Student Success Completion Grant](https://www.cloviscollege.edu/admissions-and-aid/financial-aid/cal-grant.html) pays Cal Grant recipients who are *Full-Time Students*!\n\nStudents enrolled in at least 12 but fewer than 15 semester units: **$649 per semester ($1,298 annually)**\n\nCal Grant recipients enrolled in 15 or more semester units: **$2,000 per semester ($4,000 annually)**'
            await message.channel.send(embed=embed)     
            return 
        elif user_message.lower() == '!dates':
            embed = discord.Embed() 
            embed.description = 'The [Disbursement Date Calendar](https://www.cloviscollege.edu/admissions-and-aid/financial-aid/financial-aid-disbursement-dates.html) details when you should be receiving your financial aid check.\n\nThe Pell Grant is split up and sent to students in two different checks. The first check is sent out before the semester begins, to help pay for books/school supplies. The second check is sent out in the middle of the semester during October for Fall 2022!\n\nThe CalGrant and Student Success Completion Grant are paid together in September.'
            await message.channel.send(embed=embed)     
            return 
        elif user_message.lower() == '!ab19':
            embed = discord.Embed() 
            embed.description = 'The [AB19 Fee-Waiver](https://www.cloviscollege.edu/admissions-and-aid/financial-aid/financial-aid-disbursement-dates.html) allows first-time college students who are California residents to pursue two years of college for FREE! Regardless of the Income in the household, any new student can qualify!\n\n**Requirements**\n1.) The student must have the FAFSA submitted\n2.) The student needs a first-time college student & full-time (at least 12 units)\n3.) California Resident or Non-Resident Exempt'
            await message.channel.send(embed=embed)     
            return 
        elif user_message.lower() == '!promise':
            embed = discord.Embed() 
            embed.description = 'Unlike the AB19 fee-waiver, the Promise Grant Fee-Waiver does depend on Financial Need based on the income in the household.\n\nStudents that qualify for the Promise Grant have their tuiton fees paid automatically!'
            await message.channel.send(embed=embed)     
            return 
   # Commands for Clubs is done & Template is made. We just need more clubs!
    if message.channel.name == 'clubs':
        # Important lines of code that shows what the commands are for each channel
        if user_message.lower() == '!commands':
            embed = discord.Embed() # makes the message an embed (Looks a lot cleaner)
            embed.description = '***TYPE:***\n**`!clubs`** --> *To view a list of all available clubs!*'
            # \n\n**`!make`** --> *To view a step by step guide on how to make a club*\n\n**`!events`** --> *To view upcoming club events, rushes, etc.*'
            await message.channel.send(embed=embed)     
            return 
        elif user_message.lower() == '!clubs':
            embed = discord.Embed()
            embed.description = '*List of Available Clubs:*\n**`!amc`** *Active Minds Club:* Particpates in mental health awareness... \n\n**`!asg`** *Associated Student Government:* represents the voice of the students through active representation on campus committees\n\n**`!econ`** *Crush Economics:* Attend networking events, Host speaking events with internship recruiters, and participate in a variety of activities.'
            await message.channel.send(embed=embed)
            return
        # List the Steps to make a club!

        # List upcoming Club Evemts!

        # ALL OF OUR CLUBS:
        elif user_message.lower() == '!amc':
            embed = discord.Embed()
            embed.description = 'The **[Active Minds Club](https://www.cloviscollege.edu/campus-life/clubs-organizations/active-minds.html)** is the... \n\n**__Contact Information:__**\n***Advisor E-mail:*** naomi.forey@cloviscollege.edu\n***E-mail:*** @gmail.com\n***Location:*** On Zoom\n\nTo *Join the Active Minds Club* please send an E-mail to ...'
            await message.channel.send(embed=embed)
            embed.description = "The next meeting for the Active Minds Club is..."
            # file = 
            # I get a terminal error message bc of the DM. But it doesn't break the bot, so probably fine to ignore
            await message.author.send(embed=embed)
            return
        elif user_message.lower() == '!asg':
            embed = discord.Embed()
            embed.description = "*The Associated Student Government* **[ASG](https://www.cloviscollege.edu/campus-life/clubs-organizations/associated-student-government.html)** is the... \n\n**__Contact Information:__**\n***Phone:*** (559)325-5235\n***E-mail:*** cccasg@cloviscollege.edu\n***Location:*** Student Center, *AC1-160*\n\nTo *Join ASG,* please send an E-mail to ..."
            await message.channel.send(embed=embed)
            embed.description = "The next meeting for the Associated Student Government is..."
            file = discord.File("crush.png")
            await message.author.send(embed=embed, file = file)
            return
        elif user_message.lower() == '!econ':
            embed = discord.Embed()
            embed.description = 'The **[Crush Economics Club](https://www.cloviscollege.edu/campus-life/clubs-organizations/economic-club.html)** is...\n\n**__Contact Information:__**\n***Advisor E-mail:*** sandy.brown@cloviscollege.edu\n***E-mail:*** crusheconccc@gmail.com\n***Location:*** On Zoom\n\nTo *Join Econ Crush,* please send an E-mail to ...\nHere is a Flyer:'
            # ??? How to add this file into our embeded message file = discord.File('crush_econ.heic')) ???
            await message.channel.send(embed=embed)
            embed.description = "The next meeting for the Crush Economics Club is..."
            await message.author.send(embed=embed)
            return
        ''' CLUB TEMPLATE: 
        elif user_message.lower() == '!CLUB CODENAME':
            embed = discord.Embed()
            embed.description = "The **[CLUB NAME](CLUB URL)** is the... \n\n**__Contact Information:__**\n***Phone:***(559)123-4567\n***E-mail:*** ccc@cloviscollege.edu\n***Location:*** Student Center, *AC1-160*\n\nTo *Join CLUB NAME,* please send an E-mail to ..."
            await message.channel.send(embed=embed)
    
# This is the DM sent out to the user which informs them of the NEXT MEETING:
            embed.description = "The next meeting for the Crush Economics Club is..."
            await message.author.send(embed=embed)
            return
        '''
    
    # Need More Ideas on what Commands Resources should have:
    if message.channel.name == 'resources':
        if user_message.lower() == '!commands':
            embed = discord.Embed()
            embed.description = '***TYPE:***\n**`!career`** --> *To receive information from our Career Counselors on the skills necessary to find a job!*\n\n**`!counseling`** --> *To receive information on how to contact a counselor*\n\n**`!tech`** --> *To receive information on how to check out a laptop, calculator, etc.*\n\n**`!tutorial`** --> *To receive information on how to access our tutorial center where we provide free tutoring!*\n\n**`!activities`** --> *To view details on our student center and how to participate in extracurricular activities.*\n\n**`!health`** --> *Provides students with resources to help their mental/physical health*\n\n**`!pantry`** --> To view the details of our free food programs for all students!' 
            await message.channel.send(embed=embed)
            return
        elif user_message.lower() == '!career':
            embed = discord.Embed()
            embed.description = 'The **[Career Center](https://www.cloviscollege.edu/student-services/career-services/index.html)** is here to help you with the career and major exploration process. Our career counselors will help you gain all the skills necessary to find a job in your chosen pathway.\n\n**__Contact Information:__**\n***E-mail:*** careercenter@cloviscollege.edu\n***Phone:*** (559)325-5398\n***Location:*** AC2-174\n\n**__Hours:__**\nMonday - Thursday (9:00AM - 6:00PM)\nFriday (9:00AM - 5:00PM)'
            await message.channel.send(embed=embed)
            return
        elif user_message.lower() == '!counseling':
            embed = discord.Embed()
            embed.description = 'The **[Counseling Center](https://www.cloviscollege.edu/student-services/academic-counseling/index.html)** provides comprehensive counseling services to assist students toward a successful college experience\n\n**__Contact Information:__**\n***E-mail:*** cccounseling@cloviscollege.edu\n***Phone:*** (559)325-5230\n***Location:*** AC2-133\n\n**__Hours:__**\nMonday - Thursday (8:00AM - 6:00PM)\nFriday (8:00AM - 5:00PM)'
            await message.channel.send(embed=embed)
            return
        elif user_message.lower() == '!tech':
            embed = discord.Embed()
            embed.description = 'The **[Technology Checkout Program](https://www.cloviscollege.edu/student-services/library/technology-loan-program.html)** allows students who are enrolled in CCC classes to check out laptops, webcams, personal hotspots, calculators, headphones, etc from the Library\n\n**__Contact Information:__**\n***E-mail:*** library@cloviscollege.edu\n***Phone:***(559)325-5215\n***Location:*** AC2-148'
            await message.channel.send(embed=embed)
            return 
        elif user_message.lower() == '!tutorial':
            embed = discord.Embed()
            embed.description = 'The **[Tutorial Center](https://www.cloviscollege.edu/student-services/tutorial-center/index.html)** provides peer tutoring in a welcoming, supportive, and challenging learning environment. You can access the tutorial center on campus or online via Zoom!\n\n**__Contact Information:__**\n***Phone:*** 559-325-5248\n***Location:*** AC1-137\n\n**__In-Person Hours:__**\nMonday (9:00AM - 6:00PM)\nTuesday - Thursday (9:00AM - 9:00PM)\nFriday (9:00AM - 4:00PM)\n\n**__Virtual Hours (Zoom):__**\nSunday (2:00PM - 8:00PM)\nMonday (10:00AM - 6:00PM)\nTuesday - Thursday (10:00AM - 9:00PM)\nFriday (10:00AM - 4:00PM)'
            await message.channel.send(embed=embed)
            return 
        elif user_message.lower() == '!activities':
            embed = discord.Embed()
            embed.description = '**[Student Activities](https://www.cloviscollege.edu/campus-life/student-center.html)** gives students opportunities to expand their horizons through social and extracurricular activities.\n\n**__Contact Information:__**\n***E-mail:***cccstudentcenter@cloviscollege.edu\n***Phone:*** 559-325-5235\n***Location:*** AC1-160\n\n**__Hours:__**\nMonday - Thursday (8:00AM - 5:00PM)\nFriday (9:00AM - 4:00PM)'
            await message.channel.send(embed=embed)
            return    
        elif user_message.lower() == '!health':
            embed = discord.Embed()
            embed.description = 'The **[Health Services](https://www.cloviscollege.edu/student-services/health-services/index.html)** provides students with clinical health services such as blood pressure checks, height, weight, body fat, BMI measures, etc.\n **Location:**\nAC1-2??\n\nThe **[Psychological Services](https://www.cloviscollege.edu/student-services/health-services/psychological-services-for-students.html)** is offering free individual therapy to SCCCD students via phone or Zoom meetings.\n**__Contact Information:__**\n***E-mail:*** PsychServices@SCCCD.edu\n***Phone:***559-325-5377\n\n**__Hours:__**\nMonday - Friday (8:00AM - 5:00PM)'
            await message.channel.send(embed=embed)
            return
        elif user_message.lower() == '!honors':
            embed = discord.Embed()
            embed.description = 'The **[Leon S. Peters Honors Program](https://www.cloviscollege.edu/student-services/student-support-programs/honors-program.html)** '
            await message.channel.send(embed=embed)
            return
        elif user_message.lower() == '!pantry':
            embed = discord.Embed()
            embed.description = '**[Crush Pantry](https://www.cloviscollege.edu/campus-life/crush-pantry.html)** is a free food assistance program located at the Herndon Campus available for all students!\n\n**__Contact Information:__**\n***E-mail:***crushpantry@cloviscollege.edu\n***Phone:*** 559-324-6498\n***Location:*** __Herndon Campus__ | Building A - Student Lounge\n\n**__Hours:__**\nTuesday & Thursday (10:00AM - 3:00PM)\nWednesday (11:00AM - 4:00PM)\n\n**[Crush Cupboard](https://www.cloviscollege.edu/campus-life/crush-pantry.html)** offers free food items for students On-Campus!\n\n**__Contact Information:__**\n***E-mail:*** crushpantry@cloviscollege.edu\n***Phone:***559-325-5235\n***Location:*** Student Center AC1-160\n\n**__Hours:__**\nMonday - Thursday (8:00AM - 5:00PM)\nFriday (8:00AM - 2:00PM)'
            await message.channel.send(embed=embed)
            return

    # Users are DM'd a MAP if they type this command in ANY channel
    if user_message.lower() == '!map':
        embed = discord.Embed()
        embed.description = "Here is a map of Clovis Community College!"
        file = discord.File("map.pdf")
        await message.author.send(embed=embed, file = file)

client.run(token)
 
