import discord
import time

TOKEN = 'NTYwNTg3NzA1MTI2MzU0OTU1.D32JKQ.dW3uyAtPsByqpggTsFdQnpfum5o'

client = discord.Client()
prefixes = ["!qt",";;","!","!b"]

@client.event
async def on_ready():
    print("The bot is ready!")

def test_prefixes(message_content):
    if len(message_content) <= 2:
        return False
    if len(message_content) >= 3:
        if message_content[:1] == "!":
            return True
    if len(message_content) >= 4:
        if message_content[:2] == ";;" or message_content[:2] == "!b" or message_content[:2] == "y! ":
            return True
    if len(message_content) >= 5:
        if message_content[:3] == "!qt" or message_content[:3] == "pls":
            return True 

@client.event
async def on_message(message):
    if(message.author != client.user):
        #Function that answers Hello to the author
        #if(message.content == 'Hello'):
            #await client.send_message(message.channel, 'Hello '+message.author.mention)

        #Tests the message head for a PoppyQTPi command
        if(len(message.content) > 4):
            if(message.content[:3] == "!qt"):
                print(len(message.content))
                print(message.content[4:8])
                #Tests the length of a message otherwise array might be accessing private memory
                if(len(message.content) >= 8):
                    if(message.content[4:8] == "help"):
                        await client.send_message(message.author,"After using the prefix *!qt* insert one of these commands:\n\t_-help_\n\t_-ping_")
                    if(message.content[4:8] == "ping"):
                        await client.send_message(message.channel,"pong")

        #Function that eliminates unecessary commands from server
        if(test_prefixes(message.content)):
            time.sleep(1)
            await client.delete_message(message)
            
def read_token(path):
    file = open(path,"r")
    return file.read()
        



client.run(read_token("Token.txt"))
