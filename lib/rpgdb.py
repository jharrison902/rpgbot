#Class for holding the rpg info in database
#This is a singleton class

from tinydb import TinyDB, Query
from rpggame import RpgGame

class RpgDB:
    class __RpgDB:
        def __init__(self, database_str):
            self.db = TinyDB(database_str)
            self.master_dict = {}
            
        #create a game document
        def create_game(self, game_name, server_name, channel_name):
            game = RpgGame(game_name, server_name, channel_name)
            self.db.insert(vars(game))
        
        def get_game(self, game_name, server_name, channel_name):
            gameQ = Query()
            results = self.db.search(gameQ.game_name==game_name and gameQ.server_name==server_name and gameQ.channel_name==channel_name)
            games = list(map(lambda r: RpgGame(**r), results))
            return games
            
            
    instance = None
    def __init__(self, database_str):
        if not RpgDB.instance:
            RpgDB.instance = RpgDB.__RpgDB(database_str)
        else:
            RpgDB.instance.database_str = database_str
    def __getattr__(self, name):
        return getattr(self.instance,name)