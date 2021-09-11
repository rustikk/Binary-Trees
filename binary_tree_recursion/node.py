class Node:
    #initialize a node object with no children
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f"<Node {self.value}>"


