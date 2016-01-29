from block import *

class Sudoku :

    def __init__(self, size):
        self.size = size
        self.count = size * size;
        self.solved = False
        self.matrix = [[Block(self.count) for x in range(self.count)] for y in range(self.count)]

    def __str__(self):
        res = ""
        for y in range(self.count):
            for x in range(self.count):
                res += str(self.matrix[x][y])
            res += '\n'
        return res

    def __repr__(self):
        return self.__str__()

    def feed(self, tab):
        if len(tab) != self.count * self.count:
            raise Exception("Taille du tableau de donnees incorrecte")
        for x in range(0, self.count):
            for y in range(0, self.count):
                if tab[x+self.count*y] is None:
                    self.matrix[x][y].clear()
                else:
                    self.matrix[x][y].forceValue(tab[x+self.count*y])



"""
toto = Sudoku(3)
print(toto)
for i in range (1, 9):
    toto.block1.remove(i)
print(toto)
for i in range (1, 9):
    toto.matrix[1][1].remove(i)
print(toto)
toto.block1.forceValue(7)
print(toto)
"""