from sudoku import Sudoku
from group import Group

class Solver :

    def __init__(self, sudoku):
        self.sudoku = sudoku
        self.rows = [Group(self.sudoku.count) for i in range(self.sudoku.count)]
        self.cols = [Group(self.sudoku.count) for i in range(self.sudoku.count)]
        self.squares = [Group(self.sudoku.count) for i in range(self.sudoku.count)]
        for y in range(0, sudoku.count):
            for x in range(0, sudoku.count):
                self.rows[y].append(sudoku.matrix[x][y])
                self.cols[x].append(sudoku.matrix[x][y])
                self.squares[x//self.sudoku.size+(y//self.sudoku.size)*self.sudoku.size].append(sudoku.matrix[x][y])
        self.iteration = 0


    def checkValid(self):
        return True

    def solve(self):
        self.iteration = 0
        if not self.checkValid():
            raise Exception("Le sudoku n'est pas valide")

        while True:
            hasChanged = self.iterate()
            self.iteration += 1
            if not hasChanged:
                print(str(self.iteration) + "ITERATIONS")
                return self.isSolved()



    def iterate(self):
        hasChanged = False
        for k in range(self.sudoku.count):
            hasChanged = hasChanged or self.rows[k].iterate()
            hasChanged = hasChanged or self.cols[k].iterate()
            hasChanged = hasChanged or self.squares[k].iterate()
        return hasChanged

    def isSolved(self):
        return True;
