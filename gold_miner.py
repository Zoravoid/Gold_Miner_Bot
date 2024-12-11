import os
import discord

exec
(
    compile
    (
        open
        (
            #include external file names here
            'reader.py'
        )
        .read()
    )
)


#importaint fonctionality
#1. read from xml 
#2. implement a 2/3 week timer for the payment period
#4. member notification if they havent payed
#5. notify gear about missing payment of members
#6. Auto nickname server members with their real names
#7. change member roles 

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord')

client.run(TOKEN)