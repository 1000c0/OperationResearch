from ortools.linear_solver import pywraplp

solver = pywraplp.Solver.CreateSolver('Glop')
x12 = solver.NumVar(0, solver.infinity(), 'x12')
x13 = solver.NumVar(0, solver.infinity(), 'x13')
x23 = solver.NumVar(0, solver.infinity(), 'x23')
x34 = solver.NumVar(0, solver.infinity(), 'x34')
x35 = solver.NumVar(0, solver.infinity(), 'x35')
x42 = solver.NumVar(0, solver.infinity(), 'x42')
x45 = solver.NumVar(0, solver.infinity(), 'x45')


varList = [x12, x13, x23, x34, x35, x42, x45]
coefList = [100, 30, 20, 10, 60, 15, 50]

solver.Add(x12 + x13 == 1)
solver.Add(-x12 + x23 - x42 == -1)
solver.Add(-x13 - x23 + x34 + x35 == 0)
solver.Add(x34 + x42 + x45 == 0)
solver.Add(-x35 - x45 == 0)

objective = solver.Objective()
for i in range(7):
    objective.SetCoefficient(varList[i], coefList[i])
objective.SetMinimization()

solver.Solve()
print('Solution:')
print('Objective value =', solver.Objective().Value())
print('x12 = ', x12.solution_value())
print('x13 = ', x13.solution_value())
print('x23 = ', x23.solution_value())
print('x34 = ', x34.solution_value())
print('x42 = ', x42.solution_value())
print('x45 = ', x45.solution_value())
