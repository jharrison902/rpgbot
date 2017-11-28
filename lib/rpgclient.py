#Client for connecting to discord

import discord
import asyncio
import sys
from rpgdb import RpgDB

class RpgClient:
    
    #constructor
    def __init__(self, db : RpgDB, notice_tag="!rpg", description="RPG Bot"):
        self.notice_tag=notice_tag
        self.description = description
        self.db = db
        self.bot = discord.Client(cache_auth=False)
        
        @self.bot.event
        @asyncio.coroutine
        def on_ready():
            print("RPG BOT READY")
            print("RPG BOT TAG: {}".format(self.notice_tag))
            print("RPG BOT USER: {}".format(self.bot.user.name))
            print("RPG BOT ID: {}".format(self.bot.user.id))
            
        @self.bot.event
        @asyncio.coroutine
        def on_message(message):
            print("GOT MESSAGE: {}: {}".format(message.author, message.content))
            
            content = message.content
            if content.startswith(self.notice_tag+" "):
                print("Valid message! Passing to processor")
                yield from self.process_msg(message)
                
    #processor
    @asyncio.coroutine
    def process_msg(self, message):
        print("PROCESSING MESSAGE")
        
        #strip tag and excess spaces
        command_txt = message.content[len(self.notice_tag+" "):].strip()
        print("COMMAND TEXT: {}".format(command_txt))
        try:
            command_arr = command_txt.split(" ")
            command_func_name = command_arr[0]
            command_args = None
            if len(command_arr) > 1:
                command_args = command_arr[1:]
            else:
                command_args = []
            command_args.insert(0, message)
            print("FINDING COMMAND {}".format(command_func_name))
            command_func = getattr(self, command_func_name)
            
            yield from command_func(*command_args)
        except:
            e = sys.exc_info[0]
            print(str(e))
            print("INVALID COMMAND: {}".format(command_txt))
            yield from self.bot.send_message(message.channel, "INVALID COMMAND {}".format(command_txt))
        print("MESSAGE PROCESSED")
            
    #create a game
    @asyncio.coroutine
    def create_game(self, message, game_name : str):
        #TODO: create game in db
        #TODO: only create game if one doesn't exist with that name
        #TODO: track game creater user
        print("CREATING GAME {}".format(game_name))
        yield from self.bot.send_message("CREATING GAME {}".format(game_name))
        
    #delete game
    
    @asyncio.coroutine
    def delete_game(self, game_name : str):
        #TODO: delete game in db
        #TODO: should maybe check so only user who made game can delete
        print("DELETING GAME {}".format(game_name))
        yield from self.bot.say("DELETING GAME {}".format(game_name))
    
    #join game
    @asyncio.coroutine
    def join_game(self, ctx, game_name : str):
        #TODO: add user to game
        print("ADDING USER {} TO GAME {}".format(ctx.message.author, game_name))
        yield from self.bot.say("ADDING USER {} TO GAME {}".format(ctx.message.author, game_name))
    
    #TODO: add more commands
    #Destroy method
    def __del__(self):
        if self.bot:
            self.bot.close()
          
    #start bot
    def startup(self, token):
        loop = asyncio.get_event_loop()
        try:
            loop.run_until_complete(self.bot.start(token))
        except KeyboardInterrupt:
             loop.run_until_complete(self.logout())
        # cancel all tasks lingering
        finally:
            loop.close()
           
    @asyncio.coroutine
    def logout(self):
        self.bot.logout()
        
    
        
        