import os
import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
DISCORD_BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

print(f"DISCORD_BOT_TOKEN: {DISCORD_BOT_TOKEN}")
print(f"OPENAI_API_KEY: {OPENAI_API_KEY}")

client = OpenAI(api_key=OPENAI_API_KEY)

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
tree = bot.tree

user_histories = {}

@bot.event
async def on_ready():
    await tree.sync()
    print(f'Logged in as {bot.user}')

@tree.command(name='discgpt', description='Ask GPT-3 a question')
@app_commands.describe(prompt='Your question for GPT-3')
async def discgpt(interaction: discord.Interaction, prompt: str):
    await interaction.response.defer()
    try:
        response = client.chat.completions.create(
            messages=[
                {"role": "user", "content": prompt}
            ],
            model="gpt-3.5-turbo",
        )
        answer = response.choices[0].message.content.strip()
        
        if interaction.user.id not in user_histories:
            user_histories[interaction.user.id] = []
        user_histories[interaction.user.id].append(prompt)
        if len(user_histories[interaction.user.id]) > 5:
            user_histories[interaction.user.id].pop(0)

        embed = discord.Embed(title="DisGPT Response", description=answer, color=discord.Color.blue())
        await interaction.followup.send(embed=embed)
    except Exception as e:
        await interaction.followup.send(f"An error occurred: {e}")

@tree.command(name='preprompt', description='Choose a pre-defined prompt for GPT-3')
@app_commands.describe(option='Select a predefined prompt')
async def preprompt(interaction: discord.Interaction, option: str):
    predefined_prompts = {
        "joke": "Tell me a joke.",
        "advice": "Give me some life advice.",
        "quote": "Give me a motivational quote."
    }

    if option in predefined_prompts:
        prompt = predefined_prompts[option]
        await discgpt(interaction, prompt)
    else:
        await interaction.response.send_message("Invalid option. Choose from 'joke', 'advice', 'quote'.", ephemeral=True)

@tree.command(name='history', description='Show your prompt history')
async def history(interaction: discord.Interaction):
    if interaction.user.id in user_histories and user_histories[interaction.user.id]:
        history = "\n".join(user_histories[interaction.user.id])
        embed = discord.Embed(title="Your Prompt History", description=history, color=discord.Color.green())
    else:
        embed = discord.Embed(title="Your Prompt History", description="No history available.", color=discord.Color.green())
    await interaction.response.send_message(embed=embed)

@tree.command(name='clearhistory', description='Clear your prompt history')
async def clearhistory(interaction: discord.Interaction):
    if interaction.user.id in user_histories:
        user_histories[interaction.user.id] = []
    await interaction.response.send_message("Your prompt history has been cleared.", ephemeral=True)

@tree.command(name='helpdiscgpt', description='Get help with the DiscGPT bot commands')
async def help_discgpt(interaction: discord.Interaction):
    embed = discord.Embed(title="DiscGPT Bot Help", description="Here are the available commands for the DiscGPT bot:", color=discord.Color.purple())
    embed.add_field(name="/discgpt <prompt>", value="Ask GPT-3 a question.", inline=False)
    embed.add_field(name="/preprompt <option>", value="Choose a pre-defined prompt (options: 'joke', 'advice', 'quote').", inline=False)
    embed.add_field(name="/history", value="Show your prompt history.", inline=False)
    embed.add_field(name="/clearhistory", value="Clear your prompt history.", inline=False)
    embed.add_field(name="/helpdiscgpt", value="Get help with the DiscGPT bot commands.", inline=False)
    await interaction.response.send_message(embed=embed)

bot.run(DISCORD_BOT_TOKEN)
