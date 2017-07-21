class Group:
    def __init__(self, name=None, header=None, footer=None, id=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id

    def __str__(self):
        return "Group: {}, {}, {}".format(self.name, self.header, self.footer)

    def __repr__(self):
        return "<Group: id {}, {}, {}, {}>".format(self.id, self.name, self.header, self.footer)

    def __lt__(self, other):
        if self.id is None:
            return False
        elif other.id is None:
            return True
        return self.id < other.id

    def __gt__(self, other):
        return self.id > other.id

    def __eq__(self, other):
        result = (self.name == other.name and self.header == other.header and self.footer == other.footer)
        if self.id is None or other.id is None:
            return result
        return result and self.id == other.id


if __name__ == "__main__":
    g = Group(name="Test", id = 5)
    g2 = Group(name="Test", id=10)

    print(g2 < g)
