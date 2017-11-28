#Client for connecting to discord

import discord
import asyncio

class RpgClient:
    
    #constructor
    def __init__(self):
        self.client = discord.Client()
        