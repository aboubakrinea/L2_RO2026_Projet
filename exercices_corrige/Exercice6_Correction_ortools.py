from ortools.linear_solver import pywraplp
solver = pywraplp.Solver.CreateSolver('GLOP')
x = solver.NumVar(0, solver.infinity(), 'x')
y = solver.NumVar(0, solver.infinity(), 'y')
# contraintes
solver.Add(x + 3*y <= 18)
solver.Add(x + y <= 8)
solver.Add(2*x + y <= 14)
# fonction objectif
solver.Maximize(20*x + 30*y)
solver.Solve()
print("x (Extra) =", x.solution_value())
print("y (sublime) =", y.solution_value())
print("profit =", solver.Objective().Value())