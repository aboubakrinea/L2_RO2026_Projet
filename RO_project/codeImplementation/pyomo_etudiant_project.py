from pyomo.environ import *

model = ConcreteModel()
# Sets
students = [1, 2, 3]
projects = [1, 2, 3]
model.I = Set(initialize=students)
model.J = Set(initialize=projects)
# Cost matrix (preference scores)   
cost = {(1, 1): 3, (1, 2): 2, (1, 3): 1,
        (2, 1): 1, (2, 2): 3, (2, 3): 2,
        (3, 1): 2, (3, 2): 1, (3, 3): 3}
#project capacity
capacity = {1: 1, 2: 1, 3: 1}
# Decision variables
model.x = Var(model.I, model.J, domain=Binary)
# Objective function
def objective_rule(model):
    return sum(cost[i, j] * model.x[i, j] for i in model.I for j in model.J)    
model.objective = Objective(rule=objective_rule, sense=maximize)
# Constraints
def student_constraint_rule(model, i):
    return sum(model.x[i, j] for j in model.J) == 1
model.student_constraint = Constraint(model.I, rule=student_constraint_rule)
def project_capacity_constraint_rule(model, j):
    return sum(model.x[i, j] for i in model.I) <= capacity[j]
model.project_capacity_constraint = Constraint(model.J, rule=project_capacity_constraint_rule)
# Solve the model
solver = SolverFactory('glpk')  
results = solver.solve(model)
# Display results
print("Optimal assignment:")
for i in model.I:   
    for j in model.J:
        if model.x[i, j].value == 1:
            print(f"Student {i} is assigned to Project {j}")    
print(f"Total Preference Score: {model.objective.expr()}")