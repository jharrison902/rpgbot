#Base RPG Session Class
from datetime import datetime

class RpgSession:
    
    def __init__(self, session_name: str, channel_name: str, server_name: str):
        self.session_name = session_name
        self.channel_name = channel_name
        self.server_name = server_name
        self.datetime = datetime.now()
    
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
    