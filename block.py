class Block:

    def __init__(self, count):
        self.values = [i for i in range(1,count+1)]
        self.count = count

    def isSolved(self):
        return self.count == 1

    def remove(self, value):
        if self.count <= 1:
            raise Exception("ERROR")
        if self.values.count(value) > 0:
            self.values.remove(value)
            self.count -= 1


    def __str__(self):
        res = "?"
        if self.count == 1:
            res = ""+str(self.values[0])
        return res

    def __repr__(self):
        return self.__str__()

    def forceValue(self, value):
        self.values.clear()
        self.values.append(value)
        self.count = 1

    def clear(self):
        self.__init__(self.count)


"""
toto = Block(9)
print(toto.values)
toto.remove(3)
print(toto.values)
toto.remove(3)
print(toto.values)
print(toto.isSolved())
print(toto)
"""
