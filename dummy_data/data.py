class Item(object):
    def __init__(self, path):
        self.path = path

    def __str__(self):
        return self.path


class File(Item):

    def __init__(self, path, content):
        Item.__init__(self, path)
        self.content = content

    def __str__(self):
        return str(Item) + " - " + self.content


class Folder(Item):

    def __init__(self, path, content=[]):
        Item.__init__(self, path)
        self.content = content

    def __str__(self):
        return str(Item) + " - number of items: " + str(len(self.content))
