from pyomo.environ import *
# create a model
model = ConcreteModel()
# sets
workers = [1, 2, 3]
tasks = [1, 2, 3]
model.I = Set(initialize=workers)
model.J = Set(initialize=tasks)
# cost matrix
cost = {(1, 1): 9, (1, 2): 2, (1, 3): 7,
        (2, 1): 6, (2, 2): 4, (2, 3): 3,
        (3, 1): 5, (3, 2): 8, (3, 3): 1}
# decision variables
model.x = Var(model.I, model.J, domain=Binary)
# objective function
def objective_rule(model):
    return sum(cost[i, j] * model.x[i, j] for i in model.I for j in model.J)
model.objective = Objective(rule=objective_rule, sense=minimize)
# constraints
def worker_constraint_rule(model, i):
    return sum(model.x[i, j] for j in model.J) == 1
model.worker_constraint = Constraint(model.I, rule=worker_constraint_rule)
def task_constraint_rule(model, j):
    return sum(model.x[i, j] for i in model.I) == 1
model.task_constraint = Constraint(model.J, rule=task_constraint_rule)
# solve the model
solver = SolverFactory('glpk')
results = solver.solve(model)
# display results
print("Optimal assignment:")
for i in model.I:
    for j in model.J:
        if model.x[i, j].value == 1:
            print(f"Worker {i} is assigned to Task {j}")
print(f"Total Cost: {model.objective.expr()}")