"""Contains the method for stating that a class needs a converter"""

def needsconverter(obj, attribs=None):
    """Set the converters for an object's attributes. This is mostly here to improve readability"""
    obj.te_converters = attribs
