class Node:
    def __init__(self, name):
        self.childern = []
        self.name = name

    def addChild(self, name):
        self.childern.append(Node(name))

    def depthFirstSearch(self, array):
        array.append(self.name)
        for child in self.childern:
            child.depthFirstSearch(array)
        return array