import discord
from discord.ext import commands
import os

print(f"[DEBUG] Version Pycord: {discord.__version__}")
print(f"[DEBUG] app_commands dispo ? {'app_commands' in dir(discord)}")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Connecté en tant que {bot.user}")

tree = bot.tree

@tree.command(name="ping", description="Répond avec pong !")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("Pong !")

TOKEN = os.getenv("DISCORD_TOKEN")
if not TOKEN:
    raise ValueError("⚠️ Le token Discord est manquant dans les variables d'environnement !")

bot.run(TOKEN)
