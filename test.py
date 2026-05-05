from ortools.linear_solver import pywraplp
solver = pywraplp.Solver.CreateSolver('GLOP')
x = solver.NumVar(0, solver.infinity(), 'x')
solver.Maximize(5*x)
solver.Add(x <= 10)
solver.Solve()
print(x.solution_value())