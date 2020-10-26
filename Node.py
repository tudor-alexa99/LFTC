class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return "Node ['" + self.data + "']"

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right
