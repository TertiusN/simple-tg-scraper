import argparse
import os
from dotenv import load_dotenv
from telethon import TelegramClient, events
import pygame

# Load environment variables from .env file
load_dotenv()

# Get environment variables
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
phone_number = os.getenv('PHONE_NUMBER')
alert_sound = "./uwu.mp3"  

# Argument parser for the phrase to search
parser = argparse.ArgumentParser(description="Telegram scraper to search for a phrase.")
parser.add_argument('--PHRASE', required=True, help="Phrase to search for in messages.")
args = parser.parse_args()

search_phrase = args.PHRASE.lower()

# Initialize Pygame mixer
pygame.mixer.init()

# Create a Telegram client
client = TelegramClient('session_name', api_id, api_hash)

@client.on(events.NewMessage)
async def handler(event):
    if search_phrase in event.message.message.lower():
        print(f"Found phrase in message: {event.message.message}")
        pygame.mixer.music.load(alert_sound)
        pygame.mixer.music.play()

async def main():
    await client.start(phone=phone_number)
    await client.run_until_disconnected()

with client:
    client.loop.run_until_complete(main())
