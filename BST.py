from Node import Node

COUNT = [10]


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

    def printBST(self, nodes=None):
        if nodes is None:
            list = []
            list.append(self.root.get_left())
            list.append(self.root.get_right())
            return str(self.root)

    def print2DUtil(self, root, space):

        # Base case
        if (root == None):
            return

        # Increase distance between levels
        space += COUNT[0]

        # Process right child first
        self.print2DUtil(root.right, space)

        # Print current node after space
        # count
        print()
        for i in range(COUNT[0], space):
            print(end=" ")
        print(root)

        # Process left child
        self.print2DUtil(root.left, space)

    def print2D(self, root):

        # space=[0]
        # Pass initial space count as 0
        self.print2DUtil(root, 0)

    def print(self):
        self.print2D(self.root)

    def print_nodes(self, current):
        if current is None:
            return

