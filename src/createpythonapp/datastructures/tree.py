class Tree(object):
    "Generic tree node."
    def __init__(self, name, contents, isFile, children=None):
        self.name = name
        self.isFile = isFile
        self.children = []
        self.contents = contents
        if children is not None:
            for child in children:
                self.add_child(child)
    def __repr__(self):
        return self.name
    def add_child(self, node):
        assert isinstance(node, Tree)
        self.children.append(node)

