import discord
import responsevs
import datetime

bugün = datetime.datetime.today()



async def send_message(message, user_message, is_private):
    try:
        response = responsevs.get_respones(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        a = 1+1


def run_discord_bot():
    TOKEN = 'YOUR BOT TOKEN'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        await client.change_presence(activity=discord.CustomActivity(name='7563616b206765726920646f6e6475'))
        print(f'{client.user} is now running!')
        with open('log.txt', 'a', encoding='utf-8') as f:
            f.write('BOT is now running!\n'+str(bugün))

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} : {user_message} ({channel})')
        with open('log.txt', 'a', encoding='utf-8') as f:
            f.write(f'{username} : {user_message} ({channel})'+'\n')

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    client.run(TOKEN)


