# # MAT3007 HW2 Q4 # #
# python code for question 4 to solve vertex covering problem

import cplex

def _main():
    # Init CPLEX Problem
    problem = cplex.Cplex()
    problem.set_problem_name("Vertex_Covering_Problem (Q4)")

    # set problem type as minimization LP problem
    problem.set_problem_type(cplex.Cplex.problem_type.LP)
    problem.objective.set_sense(problem.objective.sense.minimize) # maximize objective function (smallest set of vertices)

    # Init variables
    nodes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

    # Decision variables
    obj = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    # linear integer constraints, x_i in {0, 1}
    # lower bound = 0, upper bound = 1
    lbound = [0] * len(nodes)
    ubound = [1] * len(nodes)

    # add decision variables to the problem
    problem.variables.add(obj=obj, lb=lbound, ub=ubound, names=nodes)

    # Define variable type (this is a relaexed continuous constraint)
    all_var_integers = [(var, problem.variables.type.continuous) for var in nodes]      # uncomment these 2 lines to
    problem.variables.set_types(all_var_integers)                                       # set the variable type as continuous
    
    # Define variable type (this is a integer constraint)
    # all_var_integers = [(var, problem.variables.type.integer) for var in nodes]       # uncomment these 2 lines to 
    # problem.variables.set_types(all_var_integers)                                     # set the variable type as integer

    # Init constraints
    constraints = []

    # Constraints for edge (a, b)
    constraints.append([['a', 'b'], [1, 1]])
    # Constraints for edge (a, f)
    constraints.append([['a', 'f'], [1, 1]])
    # Constraints for edge (a, e)
    constraints.append([['a', 'e'], [1, 1]])
    # Constraints for edge (b, c)
    constraints.append([['b', 'c'], [1, 1]])
    # Constraints for edge (b, g)
    constraints.append([['b', 'g'], [1, 1]])
    # Constraints for edge (c, d)
    constraints.append([['c', 'd'], [1, 1]])
    # Constraints for edge (c, h)
    constraints.append([['c', 'h'], [1, 1]])
    # Constraints for edge (d, e)
    constraints.append([['d', 'e'], [1, 1]])
    # Constraints for edge (d, i)
    constraints.append([['d', 'i'], [1, 1]])
    # Constraints for edge (e, j)
    constraints.append([['e', 'j'], [1, 1]])
    # Constraints for edge (f, h)
    constraints.append([['f', 'h'], [1, 1]])
    # Constraints for edge (f, i)
    constraints.append([['f', 'i'], [1, 1]])
    # Constraints for edge (g, i)
    constraints.append([['g', 'i'], [1, 1]])
    # Constraints for edge (g, j)
    constraints.append([['g', 'j'], [1, 1]])
    # Constraints for edge (h, j)
    constraints.append([['h', 'j'], [1, 1]])

    # constraint names
    constraint_names = [f"Constraint_{i}" for i in range(len(constraints))]

    # each edge must be covered by at least one vertex
    rhs = [1] * len(constraints)

    # add senses to the constraints i.e. tell cplex if constraints are <=, >= or ==
    constraint_senses = ['G'] * len(constraints)

    # add constraints to the problem
    problem.linear_constraints.add(lin_expr=constraints, senses=constraint_senses, rhs=rhs, names=constraint_names)

    # Solve the problem
    print(f"The problem type is: {problem.get_problem_type()}")
    problem.solve()
    print(f"Solution status: {problem.solution.get_status()}")
    print(f"The solution result is: {problem.solution.get_status_string()}")
    print(f"Objective value: {problem.solution.get_objective_value()}")
    print(f"Optimal solution (vertex covering):")
    for i, node in enumerate(nodes):
        if problem.solution.get_values(node) != 0:
            print(f"Vertex {node} is in the vertex cover")



if __name__ == "__main__":
    _main()