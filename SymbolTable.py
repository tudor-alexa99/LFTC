from BST import *


class SymbolTable:
    def __init__(self):
        self.table = BST()

    def pos(self, value):
        return self.table.insert(value)

    def search(self, value):
        return self.table.search(value)
