from z3 import *


def solver(table):
    # 9x9 matrix of integer variables
    X = [[Int("x_%s_%s" % (i+1, j+1)) for j in range(9)] for i in range(9)]

    # each cell contains a value in {1, ..., 9}
    cells_c = [And(1 <= X[i][j], X[i][j] <= 9) for i in range(9) for j in range(9)]

    # each row contains a digit at most once
    rows_c = [Distinct(X[i]) for i in range(9)]

    # each column contains a digit at most once
    cols_c = [Distinct([X[i][j] for i in range(9)]) for j in range(9)]

    # each 3x3 square contains a digit at most once
    sq_c = [Distinct([X[3*i0 + i][3*j0 + j] for i in range(3)
                    for j in range(3)]) for i0 in range(3) for j0 in range(3)]

    sudoku_c = cells_c + rows_c + cols_c + sq_c

    instance_c = [If(table[i][j] == 0, True, X[i][j] == table[i][j]) for i in range(9) for j in range(9)]

    s = Solver()
    s.add(sudoku_c + instance_c)

    if s.check() == sat:
        m = s.model()
        r = [[m.evaluate(X[i][j]) for j in range(9)] for i in range(9)]

    return r

