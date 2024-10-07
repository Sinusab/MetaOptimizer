import numpy as np
from scipy.optimize import linprog

def optimize_metabolites():
    """
    This function optimizes the production of metabolites P, N, and Q
    based on a set of constraints and an objective function.
    
    Returns:
    - Optimization result message
    - Optimal values of the variables X1 to X15
    - Optimal value of the objective function (sum of P, N, and Q)
    """
    # Objective function coefficients: maximize P + N + Q (minimize -P, -N, -Q)
    c = np.array([0,0,0,0,0,0,0,0,0,0,0,-1,0,-1,-1])

    # Equality constraints (steady state conditions)
    A_eq = ([[1,-1,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [1,0,0,0,-1,0,0,0,0,0,0,0,0,0,0],
             [1,0,0,0,0,-1,0,0,0,0,0,0,0,0,-1],
             [0,0,0,0,0,1,-1,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,1,0,-1,0,0,0,0,0,0,0],
             [0,0,-1,0,0,0,1,0,0,0,0,0,0,0,0],
             [0,0,0,1,0,0,0,0,0,-1,0,0,0,0,0],
             [0,0,0,1,0,0,0,0,0,0,0,-1,0,0,0],
             [0,0,0,1,0,0,0,0,-1,0,0,0,0,0,0],
             [0,0,0,1,0,0,0,0,0,0,0,-1,0,-1,0],
             [0,0,1,0,0,0,-1,0,-1,0,0,0,0,0,0],
             [0,0,0,0,0,0,1,-1,0,0,0,-1,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,1,-1,0]])

    # Right-hand side of the equality constraints
    b_eq = ([0,0,0,0,0,0,0,0,0,0,0,0,0])

    # Bounds for each variable X1 to X15
    bounds = [
        (0, 1700),   # X1 < 1700
        (300, None), # X2 > 300
        (None, None),# X3 unrestricted
        (0, 700),    # X4 < 700
        (None, None),# X5 unrestricted
        (None, None),# X6 unrestricted
        (None, None),# X7 unrestricted
        (None, None),# X8 unrestricted
        (None, None),# X9 unrestricted
        (None, None),# X10 unrestricted
        (None, 1100),# X11 < 1100
        (None, None),# X12 unrestricted
        (None, None),# X13 unrestricted
        (None, 500), # X14 < 500
        (None, 1100) # X15 < 1100
    ]

    # Solve the linear programming problem
    result = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=bounds)

    # Return result details
    return result.message, result.x, result.fun

# Example: Run the optimization
message, optimal_values, optimal_function_value = optimize_metabolites()

print(f"Optimization Status: {message}")
print(f"Optimal Values for X1 to X15: {optimal_values}")
print(f"Optimal Value of the Objective Function: {optimal_function_value}")
