#Class for holding the rpg info in database
#This is a singleton class

from tinydb import TinyDB, Query

class RpgDB:
    class __RpgDB:
        def __init__(self, database_str):
            self.db = TinyDB(database_str)
            
    instance = None
    def __init__(self, database_str):
        if not RpgDB.instance:
            RpgDB.instance = __RpgDB(database_str)
        else:
            RpgDB.instance.database_str = database_str
    def __getattr(self, name):
        return getattr(self.instance,name)