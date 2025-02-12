import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv
import os

# Lade die Umgebungsvariablen aus der .env-Datei
load_dotenv()

# Hole den Token aus den Umgebungsvariablen
TOKEN = os.getenv("TOKEN")
if TOKEN is None:  # Überprüfung, ob der Token geladen wurde
    raise ValueError(
        "Die Umgebungsvariable 'TOKEN' ist nicht gesetzt. Stellen Sie sicher, dass die Datei '.env' den Discord-Bot-Token enthält.")

# Erstelle die Bot-Instanz
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)
tree = bot.tree


@bot.event
async def on_ready():
    print(f"Eingeloggt als {bot.user}")
    try:
        # Lösche alte Befehle und synchronisiere neu für ALLE Server
        await tree.sync()
        print("Globale Befehle wurden synchronisiert!")
    except Exception as e:
        print(f"Fehler beim Synchronisieren der Befehle: {e}")


@tree.command(name="ping", description="Antwortet mit Pong!")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("Pong!")


# Starte den Bot
bot.run(TOKEN)
