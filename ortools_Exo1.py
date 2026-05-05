from ortools.linear_solver import pywraplp
solver = pywraplp.Solver.CreateSolver('GLOP')
x = solver.NumVar(0, solver.infinity(), 'x')
y = solver.NumVar(0, solver.infinity(), 'y')
# contraintes
solver.Add(10*x + 3*y >= 50)
solver.Add(5*x + 2*y >= 25)
solver.Add(8*x + 4*y >= 40)
# fonction objective
solver.Minimize(x + y)
# resolution
status = solver.Solve()
# Resultat
if status == pywraplp.Solver.OPTIMAL:
    print("nombre de sacs (x) =", x.solution_value())
    print("nombre de cartons (y) =", y.solution_value())
    print("Valeur minimale Z =", solver.Objective().Value())