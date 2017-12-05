"""Tiny Entity Base Class"""

class TinyEntity:

    ID = str

    def __init__(self, **kwargs):
        """Initialize the abstract class"""
        self.uid = TinyEntity.ID() #Suggest the id moving forward to be a string
        self.te_converters = {}
        for key in kwargs:
            setattr(self,key, kwargs[key])
        if self.te_converters:
            self.restore()
    def serialize(self) -> dict:
        """handle converting any submethods before calling vars()"""
        if self.te_converters and type(self.te_converters)==dict:
            # have converters run
            for key in self.te_converters:
                tmp = getattr(self, key)
                delattr(self, key) # delete it in the original object
                serializer = getattr(self.te_converters[key], 'serialize')
                if serializer:
                    setattr(self, key, serializer(tmp))
                else:
                    raise TypeError("Converter {} does not have a serialize method!".format(self.te_converters[key]))
        return vars(self)
    def restore(self):
        """Restore attributes from the database that needed converters"""
        if self.te_converters and type(self.te_converters)==dict:
            # have converters run
            for key in self.te_converters:
                tmp = getattr(self, key)
                delattr(self, key) # delete it in the original object
                deserializer = getattr(self.te_converters[key], 'deserialize')
                if deserializer:
                    setattr(self, key, deserializer(tmp))
                else:
                    raise TypeError("Converter {} does not have a deserialize method!".format(self.te_converters[key]))
