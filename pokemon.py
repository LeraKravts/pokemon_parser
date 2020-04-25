
class Pokemon:
    def __init__(self, name, type1, type2, english, japan,url):
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.english = english
        self.japan = japan
        self.url = url

    def get_map(self):
        return {'name': self.name,
                'type1': self.type1,
                'type2': self.type2,
                'english': self.english,
                'japan': self.japan,
                'url': self.url}

    def __str__(self):

        return '{self.name},{self.type1},{self.type2}, \
        {self.english},{self.japan},{self.url}'.format(self=self)
