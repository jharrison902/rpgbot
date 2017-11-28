#Client for connecting to discord

import discord
from discord.ext import commands
import asyncio
import rpgdb

class RpgClient:
    
    #constructor
    def __init__(self, notice_tag="!rpg", description="RPG Bot", db : RpgDB):
        self.notice_tag=notice_tag
        self.description = description
        self.db = db
        self.bot = commands.Bot(command_prefix=notice_tag, description=description)
        
        @self.bot.event
        @asyncio.coroutine
        def on_ready():
            print("RPG BOT READY")
            print("RPG BOT TAG: {}".format(self.notice_tag))
            print("RPG BOT USER: {}".format(self.bot.user.name))
            print("RPG BOT ID: {}".format(self.bot.user.id))
            
        #create a game
        @self.bot.command
        @asyncio.coroutine
        def create_game(game_name : str):
            #TODO: create game in db
            #TODO: only create game if one doesn't exist with that name
            #TODO: track game creater user
            print("CREATING GAME {}".format(game_name))
            
        #delete game
        @self.bot.command
        @asyncio.coroutine
        def delete_game(game_name : str):
            #TODO: delete game in db
            #TODO: should maybe check so only user who made game can delete
            print("DELETING GAME {}".format(game_name))
        
        #join game
        @self.bot.command(pass_context=True)
        @asyncio.coroutine
        def delete_game(ctx, game_name : str):
            #TODO: add user to game
            print("ADDING USER {} TO GAME {}".format(ctx.message.author, game_name))
        
        #TODO: add more commands
            
    
        
        