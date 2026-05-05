from pyomo.environ import *

Model = ConcreteModel()
# les variables
Model.x = Var(domain=NonNegativeReals)
Model.y = Var(domain=NonNegativeReals)
# la fonction objective
Model.obj = Objective(expr=20*Model.x + 30*Model.y, sense=maximize)
# les contraintes
Model.c1 = Constraint(expr=Model.x + 3*Model.y <= 18)
Model.c2 = Constraint(expr=Model.x + Model.y <= 8)
Model.c3 = Constraint(expr=3*Model.x + Model.y <= 14)
solver = SolverFactory('glpk')
solver.solve(Model)
# Resultat
print("x (Extra) =",value(Model.x))
print("y (sublime) =",value(Model.y))
print("profit =",value(Model.obj))