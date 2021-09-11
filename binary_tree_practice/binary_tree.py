from node import Node

class BinaryTree:
    def __init__(self, head: Node):
        self.head = head
    
    def add(self, new_node: Node):
        current_node = self.head
        while current_node:
            if new_node == current_node:
                raise ValueError(f"The node {current_node} already exists")
            
            elif new_node < current_node:
                if current_node.left is not None:
                    current_node = current_node.left
                elif current_node.left is None:
                    current_node.left = new_node
                    break
            
            elif new_node > current_node:
                if current_node.right:
                    current_node = current_node.right
                else:
                    current_node.right = new_node
                    break
    
    def find(self, value: int):
        current_node = self.head
        while current_node is not None:
            if current_node == value:
                return current_node
            elif value < current_node.value:
                current_node = current_node.left
            elif value > current_node.value:
                current_node = current_node.right
        #if after all the iterations no value is found in the tree
        raise LookupError(f"A node with {value} was not found)
