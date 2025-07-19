import discord
import logging

intents = discord.Intents.default()

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"✅ Connecté en tant que {client.user} (ID: {client.user.id})")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "!ping":
        await message.channel.send("🏓 Pong !")

if __name__ == "__main__":
    import os
    logging.basicConfig(level=logging.INFO)
    TOKEN = os.getenv("DISCORD_TOKEN")
    if not TOKEN:
        raise ValueError("Le token Discord n'est pas défini dans les variables d'environnement.")
    client.run(TOKEN)
