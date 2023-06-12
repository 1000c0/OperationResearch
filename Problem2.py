from ortools.linear_solver import pywraplp


def main():
    solver = pywraplp.Solver.CreateSolver('GLOP')

    x11 = solver.NumVar(0, solver.infinity(), 'x11')
    x12 = solver.NumVar(0, solver.infinity(), 'x12')
    x13 = solver.NumVar(0, solver.infinity(), 'x13')
    x21 = solver.NumVar(0, solver.infinity(), 'x21')
    x22 = solver.NumVar(0, solver.infinity(), 'x22')
    x23 = solver.NumVar(0, solver.infinity(), 'x23')

    solver.Add(x11 + x21 <= 150)
    solver.Add(x12 + x22 <= 200)
    solver.Add(x13 + x23 <= 350)
    solver.Add(x11 + x12 + x13 <= 100)
    solver.Add(x21 + x22 + x23 <= 200)

    solver.Maximize(4 * x11 + 4 * x12 + 3 * x13 + 5 * x21 + 5 * x22 + 4 * x23)
    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        print('Objective value =', solver.Objective().Value())
        print('x11 =', x11.solution_value())
        print('x12 =', x12.solution_value())
        print('x13 =', x13.solution_value())
        print('x21 =', x21.solution_value())
        print('x22 =', x22.solution_value())
        print('x23 =', x23.solution_value())
    else:
        print('There is no solution')


if __name__ == "__main__":
    main()
