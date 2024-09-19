# %% [markdown]
# ### Question 1 (d)

# %%
from pulp import LpProblem, LpMaximize, LpVariable, LpStatus, value

# Init LP Problem from Q1(a)
problem = LpProblem("Maximize_Profit", LpMaximize)

# Decision variables
x1 = LpVariable("x1", lowBound=0, cat='Integer')  # Number of products of the first type
x2 = LpVariable("x2", lowBound=0, cat='Integer')  # Number of products of the second type

# Objective function
problem += 7.8 * x1 + 7.1 * x2, "Total_Profit"

# Constraints
problem += (1/8) * x1 + (1/4) * x2 <= 90, "Assembly_Labor_Constraint"
problem += (1/2) * x1 + (1/6) * x2 <= 80, "Testing_Labor_Constraint"

# Solving LP Problem
problem.solve()

# Output the results
print("Status:", LpStatus[problem.status])
print("Number of products of the first type (x1):", value(x1))
print("Number of products of the second type (x2):", value(x2))
print("Total Profit:", value(problem.objective))


# %% [markdown]
# ### Question 3

# %%
from pulp import LpProblem, LpMinimize, LpVariable, LpStatus, LpStatusOptimal, value, lpSum

# # Relaxed LP Problem from Q3

# Cost Table 1
costs = [
    [0, 20, 13, 11, 28],  # From region 1
    [20, 0, 18, 8, 46],   # From region 2
    [13, 18, 0, 9, 27],   # From region 3
    [11, 8, 9, 0, 20],    # From region 4
    [28, 46, 27, 20, 0]   # From region 5
]

# Present Supply
p = [110, 335, 400, 420, 610]

# Needed Demand
n = [150, 200, 600, 200, 390]

# Init LP Problem from Q3
problem = LpProblem("Minimize_Cost_Moving_Cars", LpMinimize)

# Decision variables
x = LpVariable.dicts("x", (range(5), range(5)), lowBound=0, cat='Continuous')  # Number of products of the first type

# Objective function
problem += lpSum([costs[i][j] * x[i][j] for i in range(5) for j in range(5)]), "Total_Cost"

# Present Supply Constraints
for i in range(5):
    problem += lpSum([x[i][j] for j in range(5)]) <= p[i], f"Present_Supply_Constraint_{i}"

# Needed Demand Constraints
for j in range(5):
    problem += lpSum([x[i][j] for i in range(5)]) >= n[j], f"Needed_Demand_Constraint_{j}"

# Solving LP Problem
problem.solve()

# Output the optimal results
if problem.status == LpStatusOptimal:
    print("Relaxed LP Problem Status:", LpStatus[problem.status])
    print("Optimal value:", value(problem.objective))
    print("Optimal solution (number of cars moved):")
    for i in range(5):
        for j in range(5):
            if x[i][j].varValue != 0 and i != j:
                print(f"Move {x[i][j].varValue} cars from region {i+1} to region {j+1}")
else:
    print("No optimal solution found.")


# %%
from pulp import LpProblem, LpMinimize, LpVariable, LpStatus, LpStatusOptimal, value, lpSum

# # Non-relaxed LP Problem from Q3

# Cost Table 1
costs = [
    [0, 20, 13, 11, 28],  # From region 1
    [20, 0, 18, 8, 46],   # From region 2
    [13, 18, 0, 9, 27],   # From region 3
    [11, 8, 9, 0, 20],    # From region 4
    [28, 46, 27, 20, 0]   # From region 5
]

# Present Supply
p = [110, 335, 400, 420, 610]

# Needed Demand
n = [150, 200, 600, 200, 390]

# Init LP Problem from Q3
problem = LpProblem("Minimize_Cost_Moving_Cars", LpMinimize)

# Decision variables
x = LpVariable.dicts("x", (range(5), range(5)), lowBound=0, cat='Integer')  # Number of products of the first type

# Objective function
problem += lpSum([costs[i][j] * x[i][j] for i in range(5) for j in range(5)]), "Total_Cost"

# Present Supply Constraints
for i in range(5):
    problem += lpSum([x[i][j] for j in range(5)]) <= p[i], f"Present_Supply_Constraint_{i}"

# Needed Demand Constraints
for j in range(5):
    problem += lpSum([x[i][j] for i in range(5)]) >= n[j], f"Needed_Demand_Constraint_{j}"

# Solving LP Problem
problem.solve()

# Output the optimal results
if problem.status == LpStatusOptimal:
    print("Non-relaxed LP Problem Status:", LpStatus[problem.status])
    print("Optimal value:", value(problem.objective))
    print("Optimal solution (number of cars moved):")
    for i in range(5):
        for j in range(5):
            if x[i][j].varValue != 0 and i != j:
                print(f"Move {x[i][j].varValue} cars from region {i+1} to region {j+1}")
else:
    print("No optimal solution found.")


# %% [markdown]
# ### Question 4

# %%
from pulp import LpProblem, LpMinimize, LpVariable, LpStatus, LpStatusOptimal, value, lpSum

# # Relaxed LP Problem from Q4

# Graph Matrix from qn 4
M = 100
W = [
    [M, 5, 4, M, M, M, M, M],
    [5, M, M, 3, M, 7, M, M],
    [4, M, M, M, 1, 2, M, M],
    [M, 3, M, M, 2, M, M, M],
    [M, M, 1, 2, M, M, 2, 5],
    [M, 7, 2, M, M, M, M, 3],
    [M, M, M, M, 2, M, M, 1],
    [M, M, M, M, 5, 3, 1, M]
]

# count number of nodes in the graph matrix
n = len(W)

# Init LP Problem from Q4
problem = LpProblem("Shortest_path_problem", LpMinimize)

# Decision variables
x = LpVariable.dicts("x", (range(n), range(n)), lowBound=0, cat='Continuous') 

# Objective function
problem += lpSum([W[i][j] * x[i][j] for i in range(n) for j in range(n)]), "Shortest_Cumulative_Path"

# Constraints
# Constraints for source node
problem += lpSum([x[0][j] for j in range(1, n)]) == 1, "Constraint_1"

# Constraints for destination node
problem += lpSum([x[i][n-1] for i in range(n-1)]) == 1, "Constraint_n"

# Flow Conservation Constraints
for i in range(1, n-1):
    problem += lpSum([x[i][j] for j in range(n)]) - lpSum([x[j][i] for j in range(n)]) == 0, f"Flow_Conservation_Constraint_{i}"



# Solving LP Problem
problem.solve()

# Output the optimal results
if problem.status == LpStatusOptimal:
    print("Relaxed LP Problem Status:", LpStatus[problem.status])
    print("Optimal value:", value(problem.objective))
    print("Optimal solution (path taken):")
    for i in range(n):
        for j in range(n):
            if x[i][j].varValue != 0:
                print(f"Path from node {i+1} to node {j+1}: {x[i][j].varValue}")
else:
    print("No optimal solution found.")


# %%
from pulp import LpProblem, LpMinimize, LpVariable, LpStatus, LpStatusOptimal, value, lpSum

# # Non-Relaxed LP Problem from Q4

# Graph Matrix from qn 4
M = 100
W = [
    [M, 5, 4, M, M, M, M, M],
    [5, M, M, 3, M, 7, M, M],
    [4, M, M, M, 1, 2, M, M],
    [M, 3, M, M, 2, M, M, M],
    [M, M, 1, 2, M, M, 2, 5],
    [M, 7, 2, M, M, M, M, 3],
    [M, M, M, M, 2, M, M, 1],
    [M, M, M, M, 5, 3, 1, M]
]

# count number of nodes in the graph matrix
n = len(W)

# Init LP Problem from Q4
problem = LpProblem("Shortest_path_problem", LpMinimize)

# Decision variables
x = LpVariable.dicts("x", (range(n), range(n)), lowBound=0, cat='Integer') 

# Objective function
problem += lpSum([W[i][j] * x[i][j] for i in range(n) for j in range(n)]), "Shortest_Cumulative_Path"

# Constraints
# Constraints for source node
problem += lpSum([x[0][j] for j in range(1, n)]) == 1, "Constraint_1"

# Constraints for destination node
problem += lpSum([x[i][n-1] for i in range(n-1)]) == 1, "Constraint_n"

# Flow Conservation Constraints
for i in range(1, n-1):
    problem += lpSum([x[i][j] for j in range(n)]) - lpSum([x[j][i] for j in range(n)]) == 0, f"Flow_Conservation_Constraint_{i}"



# Solving LP Problem
problem.solve()

# Output the optimal results
if problem.status == LpStatusOptimal:
    print("Non-Relaxed LP Problem Status:", LpStatus[problem.status])
    print("Optimal value:", value(problem.objective))
    print("Optimal solution (path taken):")
    for i in range(n):
        for j in range(n):
            if x[i][j].varValue != 0:
                print(f"Path from node {i+1} to node {j+1}: {x[i][j].varValue}")
else:
    print("No optimal solution found.")



