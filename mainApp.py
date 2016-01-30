from sudoku import Sudoku
from solver import Solver

def main():
    sudoku = Sudoku(3)
    print(sudoku)
#    sudoku.feed([1,2,4,3,3,None,None,None,2,1,3,None,None,3,2,1])
    # test
    #sudoku.feed([None,7,5,None,9,None,None,None,6,None,2,3,None,8,None,None,4,None,8,None,None,None,None,3,None,None,1,5,None,None,7,None,2,None,None,None,None,4,None,8,None,6,None,2,None,None,None,None,9,None,1,None,None,3,9,None,None,4,None,None,None,None,7,None,6,None,None,7,None,5,8,None,7,None,None,None,1,None,3,9,None])
    # rem
    sudoku.feed([None,5,None,None,None,None,2,8,None,None,None,None,None,7,6,None,None,None,None,None,2,1,None,None,None,None,None,9,4,None,None,1,None,None,None,None,None,None,1,5,None,4,None,None,None,None,None,6,None,None,3,9,None,None,6,None,None,3,None,None,None,None,None,None,2,None,7,None,1,6,4,None,None,None,None,None,None,None,5,None,3])
    print(sudoku)
    solver = Solver(sudoku)
    solved = solver.solve()
    if solved: print("SOLVED !!")
    print(sudoku)
    sudoku.printIncertitudes()


if __name__ == "__main__":
    main()


#main()