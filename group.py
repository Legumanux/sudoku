class Group:

    def __init__(self, count):
        self.count = count
        self.values = []
        self.isSolved = False

    def append(self, block):
        self.values.append(block)

    def iterate(self):
        if self.isSolved:
            return False
        hasChanged = False
        lockedValues = []
        lockedValues.clear()
        for block in self.values:
            if block.isSolved():
                lockedValues.append(block.values[0])
        for block in self.values:
            if not block.isSolved():
                for value in block.values:
                    if lockedValues.count(value) > 0:
                        block.remove(value)
                        hasChanged = True

                        if not self.isValid():
                            print("PAS VALIDE")
                        else:
                            print("OK")
                        if block.isSolved():
                            lockedValues.append(block.values[0])
        self.isSolved = len(lockedValues) == self.count
        return hasChanged

    def isValid(self):
        lockedValues = []
        for block in self.values:
            if block.isSolved():
                lockedValues.append(block.values[0])
        for block in self.values:
            if block.isSolved() and lockedValues.count(block.values[0]) > 1:
                return False
        return True

    def __str__(self):
        res = ""
        for b in self.values:
            res += str(b)
        return res

    def __repr__(self):
        return self.__str__()
