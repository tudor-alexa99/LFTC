from Node import Node


class BST:

    def __init__(self):
        self.root = None

    def insert(self, value):

        if self.root is None:
            self.root = Node(value)
            return self.root

        else:
            parent = None
            current = self.root
            direction = ""

            while current is not None:
                parent = current

                if current.data < value:
                    current = current.left
                    direction = "left"

                elif current.data > value:
                    current = current.right
                    direction = "right"

                else:
                    # if the current symbol already exists, return the node containing it
                    return current

            if direction == "left":
                parent.left = Node(value)
                return parent.left

            else:
                parent.right = Node(value)
                return parent.right

    def search(self, value):
        if self.root is None:
            return None

        current = self.root
        while current is not None:
            if current.data == value:
                return current

            elif current.data < value:
                current = current.right

            elif current.data > value:
                current = current.left

        return None
