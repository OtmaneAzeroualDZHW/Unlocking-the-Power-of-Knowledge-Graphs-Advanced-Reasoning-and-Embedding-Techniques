# Rule-based reasoning mathematical formulation implementation
def rule_based_reasoning(kb, rules):
    inferred_facts = set()
    for rule in rules:
        premises, conclusion = rule
        if all(premise in kb for premise in premises):
            inferred_facts.add(conclusion)
    return inferred_facts

# Example knowledge base and rules
knowledge_base = {"A", "B"}
rules = [(("A", "B"), "C"), (("C", "D"), "E")]

# Applying rule-based reasoning
inferred = rule_based_reasoning(knowledge_base, rules)
print("Inferred facts:", inferred)

# Constraint-based reasoning example for a scheduling problem
from ortools.sat.python import cp_model

def constraint_based_reasoning():
    model = cp_model.CpModel()
    # Example variables and constraints
    task1 = model.NewIntVar(0, 10, 'task1')
    task2 = model.NewIntVar(0, 10, 'task2')
    model.Add(task1 != task2)
    
    # Solver
    solver = cp_model.CpSolver()
    status = solver.Solve(model)
    if status == cp_model.FEASIBLE:
        print(f'Task 1: {solver.Value(task1)}, Task 2: {solver.Value(task2)}')

# Example usage
constraint_based_reasoning()


