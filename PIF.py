class PIF:
    def __init__(self):
        self.data = []  # empty dictionary

    def add(self, token, node):
        self.data.append([token, node])

    def search(self, token):
        return self.data[token]

    def __str__(self):
        s = ""
        for d in self.data:
            s = s + d[0] + " --> " + d[1].__str__() + "\n"
        return s