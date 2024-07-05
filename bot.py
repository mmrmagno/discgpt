import os
import discord
from discord.ext import commands
import openai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the tokens from environment variables
openai_api_key = os.getenv('OPENAI_API_KEY')
discord_bot_token = os.getenv('DISCORD_BOT_TOKEN')

# Initialize OpenAI
openai.api_key = openai_api_key

# Initialize Discord Bot
intents = discord.Intents.default()
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.slash_command(name='chatgpt', description='Get an answer from ChatGPT')
async def chatgpt(ctx, *, prompt: str):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150
        )
        await ctx.respond(response.choices[0].text.strip())
    except Exception as e:
        await ctx.respond(f"Error: {str(e)}")

bot.run(discord_bot_token)
