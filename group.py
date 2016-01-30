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
                        """
                        if not self.isValid():
                            print("PAS VALIDE")
                        else:
                            print("OK")
                        """
                        if block.isSolved():
                            lockedValues.append(block.values[0])
        if len(lockedValues) == self.count:
            self.isSolved = True
        # on va maintenant placer les chiffres non places
        if not self.isSolved:
            for val in range(1, self.count+1):
                if lockedValues.count(val) == 0:
                    # on compte le nombre de cases non solved qui peuvent contenir
                    matches = []
                    for k in range(self.count):
                        if self.values[k].values.count(val) == 1:
                            matches.append(self.values[k])
                    if len(matches) == 1:
                        matches[0].forceValue(val)
                        lockedValues.append(val)
                        hasChanged = True


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
