from pyomo.environ import *
model = ConcreteModel()

# les variables
model.x = Var(domain=NonNegativeReals)
model.y = Var(domain=NonNegativeReals)
# la fonction objective
model.obj = Objective(expr=model.x + model.y, sense=minimize)
# les contraintes   
model.c1 = Constraint(expr=10*model.x + 3*model.y >= 50)
model.c2 = Constraint(expr=5*model.x + 2*model.y >= 25)
model.c3 = Constraint(expr=8*model.x + 4*model.y >= 40)
# SOLVEUR   
solver = SolverFactory('glpk')
solver.solve(model)
# Resultat
print("nombre de sacs (x) =",value(model.x))
print("nombre de cartons (y) =",value(model.y))
print("Valeur minimale Z =",value(model.obj))