from ortools.linear_solver import pywraplp
solver = pywraplp.Solver.CreateSolver('GLOP')
x = solver.NumVar(0, solver.infinity(), 'x')
y = solver.NumVar(0, solver.infinity(), 'y')
# contraintes
solver.Add(x + 2*y <= 10)
solver.Add(2*x + y <= 8)
solver.Add(x >= 4)
solver.Add(y >= 3)
# fonction objectif
solver.Maximize(2*x + 3*y)
# Resolution
status = solver.Solve()
# Resultat
if status == pywraplp.Solver.OPTIMAL:
   print("x =", x.solution_value())
   print("y =", y.solution_value())
   print("cout minimale =", solver.Objective().Value())
else:   print("Le problème n'a pas de solution optimale.")
