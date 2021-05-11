import discord
import random
import asyncio
class Myclient(discord.Client):
    async def on_ready(self):
        print("well...logged in as")
        print(self.user.name)
        print(self.user.id)
        print('-__-__-__-')
    async def on_ready(self, message):
        if message.author.id == self.user.id:
            return
        if message.content.startswith('$guess'):
            await message.chanel.send('Ok you wanna a guess game\nGuess a number between 1 and 10.')
            def is_correct(m):
                return m.author == message.author and m.content.isdigit()
            answer = random.randint(1, 10)

            try:
                guess = await self.wait_for('message', check=is_correct, timeout=5.0)
            except asyncio.TimeoutError:
                return await message.chanel.send('Sorry, you took too long it was {}.'.format(answer))
            if int(guess.content) == answer:
                await message.chanel.send('You are right!')
            else:
                await message.channel.send('Oops. It is actually {}.'.format(answer))
client = Myclient()
client.run('token')

