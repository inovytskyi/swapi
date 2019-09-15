import json
class Entity(object):

    def __init__(self, dict_data, entity_type):
        for key, value in dict_data.items():
            setattr(self, key, value)
        self.entity_type = entity_type

    def __repr__(self):
        if hasattr(self, 'name'):
            name = self.name
        elif hasattr(self, 'title'):
            name = self.title
        else:
            name = ""
        return "{} - {}".format(self.entity_type, name)

