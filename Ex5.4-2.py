from ortools.linear_solver import pywraplp

solver = pywraplp.Solver.CreateSolver("Glop")
x11 = solver.NumVar(0, solver.infinity(), "x11")
x12 = solver.NumVar(0, solver.infinity(), "x12")
x13 = solver.NumVar(0, solver.infinity(), "x13")
x14 = solver.NumVar(0, solver.infinity(), "x14")
x21 = solver.NumVar(0, solver.infinity(), "x21")
x22 = solver.NumVar(0, solver.infinity(), "x22")
x23 = solver.NumVar(0, solver.infinity(), "x23")
x24 = solver.NumVar(0, solver.infinity(), "x24")
x31 = solver.NumVar(0, solver.infinity(), "x31")
x32 = solver.NumVar(0, solver.infinity(), "x32")
x33 = solver.NumVar(0, solver.infinity(), "x33")
x34 = solver.NumVar(0, solver.infinity(), "x34")
x41 = solver.NumVar(0, solver.infinity(), "x41")
x42 = solver.NumVar(0, solver.infinity(), "x42")
x43 = solver.NumVar(0, solver.infinity(), "x43")
x44 = solver.NumVar(0, solver.infinity(), "x44")


varList = [
    x11,
    x12,
    x13,
    x14,
    x21,
    x22,
    x23,
    x24,
    x31,
    x32,
    x33,
    x34,
    x41,
    x42,
    x43,
    x44,
]

coefList = [1, 4, 6, 3, 9, 7, 10, 9, 4, 5, 11, 7, 8, 7, 8, 5]

solver.Add(x11 + x12 + x13 + x14 == 1)
solver.Add(x21 + x22 + x23 + x24 == 1)
solver.Add(x31 + x32 + x33 + x34 == 1)
solver.Add(x41 + x42 + x43 + x44 == 1)

solver.Add(x11 + x21 + x31 + x41 == 1)
solver.Add(x12 + x22 + x32 + x42 == 1)
solver.Add(x13 + x23 + x33 + x43 == 1)
solver.Add(x14 + x24 + x34 + x44 == 1)

objective = solver.Objective()
for i in range(16):
    objective.SetCoefficient(varList[i], coefList[i])
objective.SetMinimization()

solver.Solve()
print("Solution:")
print("Objective value =", solver.Objective().Value())
print("x11 = ", x11.solution_value())
print("x12 = ", x12.solution_value())
print("x13 = ", x13.solution_value())
print("x14 = ", x14.solution_value())
print("x21 = ", x21.solution_value())
print("x22 = ", x22.solution_value())
print("x23 = ", x23.solution_value())
print("x24 = ", x24.solution_value())
print("x31 = ", x31.solution_value())
print("x32 = ", x32.solution_value())
print("x33 = ", x33.solution_value())
print("x34 = ", x34.solution_value())
print("x41 = ", x41.solution_value())
print("x42 = ", x42.solution_value())
print("x43 = ", x43.solution_value())
print("x44 = ", x44.solution_value())
