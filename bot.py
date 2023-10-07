import discord
import responses
import random

responses = [
    "what do yuw awANT!!!",
    "wussup",
    "your mom",
    "hola",
    "hey there",
    "hi",
    "i like trains",
    "my name is actually Bobothy",
]

async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

def run_discord_bot():
    TOKEN = 'MTE1Nzg0NTIwMDEzNjMyMzExMg.Gi_AwK.SQAt1qh8E8UE1mGJxEQK2QD1ykomrclX-bgiR4'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        await client.change_presence(activity = discord.Game('Maintnence'))
        print(f'{client.user} is now running')


    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        if 'jeff' in message.content.lower():
            response = random.choice(responses)
            await message.channel.send(response)
        if '.spam' in message.content.lower():
            for i in range(5):
                await message.channel.send('MUAHAHAHAHAHAHA')
        
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said: "{user_message}" ({channel})')

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)


    client.run(TOKEN)
