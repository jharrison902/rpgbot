#Player base class

class RpgPlayer:
    
    def __init__(self, player_name:str, player_roles=None):
        self.player_name = player_name
        self.player_roles = player_roles
        self.characters = []
    
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
    