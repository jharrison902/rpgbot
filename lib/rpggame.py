import json
from rpgsession import RpgSession
from rpgplayer import RpgPlayer
from datetime import datetime

#Game class for representing a game
class RpgGame:
    
    def __init__(self, *initial_data, **kwargs):
        for dictionary in initial_data:
            for key in dictionary:
                setattr(self, key, dictionary[key])
        for key in kwargs:
            setattr(self, key, kwargs[key])
    
    def __init__(self, game_name: str, server_name: str, channel_name: str, sessions=[], notes=[], players=[]):
        self.game_name = game_name
        self.server_name = server_name
        self.channel_name = channel_name
        self.players = players
        self.sessions = sessions
        self.notes = notes
    
    def add_session(self, session : RpgSession):
        self.sessions.append(session)
        
    def remove_session(self, session=None, date_str=None, date=None, date_format="%Y-%m-%d", session_id=None):
        fdate = date
        if date_str:
            fdate = datetime.strptime(date_str, date_format)
        for x in range(0,len(self.sessions)):
            tmp = self.sessions[x]
            if fdate:
                if tmp.datetime==fdate:
                    del self.sessions[x]
                    break
            elif session_id:
                if tmp.session_id==session_id:
                    del self.sessions[x]
                    break
            elif session:
                if tmp == session:
                    del self.sessions[x]
                    break
            
    
    def add_player(self, player : RpgPlayer):
        self.sessions.append(player)
        
    def remove_player(self, player=None, player_name=None):
        for x in range(0,len(self.players)):
            tmp = self.players[x]
            if player:
                if player == tmp:
                    del self.players[x]
                    break
            elif player_name:
                if player.player_name == tmp.player_name:
                    del self.players[x]
                    break
        
    
    #general methods
    
    def add_feature(self, feature_name:str, feature=None):
        if getattr(self, feature_name):
            setattr(self, feature_name, feature)
        else:
            self.setattr(self, feature_name, feature)
    
    def remove_feature(self, feature_name:str):
        if getattr(self, feature_name):
            delattr(self, feature_name)
    
    def insert_into_feature(self, feature_name:str, data=None):
        attr = getattr(self, feature_name)
        if attr and type(attr)==list:
            attr.append(data)
    
    def remove_from_feature(self, feature_name:str, data_property:str, property_value=None):
        attr = getattr(self, feature_name)
        if attr and type(attr)==list:
            for x in range(0,len(attr)):
                tmp = attr[x]
                xattr = getattr(tmp, data_property)
                if xattr and xattr==property_value:
                    del attr[x]
                    break
    
        
            
            
        