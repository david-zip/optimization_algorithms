"""
Useing the same ABC algorithm made but try to implement a more advanced termination criteria

Minimise the Rosenbrock equation for a = 1 and b = 100

Upper and lower bound of [-5,5]

Date: 08/03/22
"""
import time
import random
import numpy as np

# Define fitness function
def f(x,y):
    global a, b
    a = 20
    b = 100
    return (a - x)**2 + b*(y - x**2)**2

# Create employed bees and provide inital solutions
beehive_population = 100

employed_bee_militia = {}
employed_bee_solutions = {}

for i in range(int(beehive_population/2)):
    bee_name = "Employed Bee {}".format(i+1)
    employed_bee_militia[bee_name] = np.random.uniform(0, 10, [2,1])

    x, y = employed_bee_militia[bee_name][0], employed_bee_militia[bee_name][0]
    employed_bee_solutions[bee_name] = f(x,y)

# Shows solution found by each emplyed bee
"""
for name, array in employed_bee_militia.items():
    print("{}\t:\t{}\n\t\t\t{}\n\t\t\t{}\n".format(name, array[0], array[1], employed_bee_solutions[name]))
"""

# Creates a dictionary of abandoned food sources to determine whether a food source is abandoned
abandon_food = {} 
for name in employed_bee_militia.keys():
    abandon_food[name] = 0

# Start ABC search algorithm
best_value = 10
best_sol = np.array([0,0])
old_best_value = 11

end_counter = 0
iter_count = 1

time_start = time.time()
while True:

    for name, value in employed_bee_militia.items():

        # Generate a new solution using an update function
        new_search = np.random.uniform(0, a**2, [2, 1])
        new_solution = []
        for i in range(2):
            r1 = random.uniform(-1, 1)
            r2 = random.uniform(1e-4, 1)
            new_solution.append(value[i] + r1 * r2 * (value[i] - new_search[i]))

        # Generate solution values of new food sources
        new_sol_value = f(new_solution[0], new_solution[1])
        
        if new_sol_value < employed_bee_solutions[name]:
            # If a better solution is found, replace the old solution
            employed_bee_militia[name] = np.array(new_solution)
            employed_bee_solutions[name] = new_sol_value
        else:
            # Counter the abandon food value
            abandon_food[name] += 1

    # Calculate the probability values of each solution and store into a dictionary
    sol_prob = {}
    for name, value in employed_bee_solutions.items():
        sol_prob[name] = float(value / sum(sol for sol in employed_bee_solutions.values()))

    """
    # Sort probablity into ascending order 
    sol_prob = {name: value for name, value in sorted(sol_prob.items(), key=lambda item: item[1])}
    """

    # Onlooker bee work
    for name, value in employed_bee_militia.items():
        r1 = random.uniform(0, 1/(beehive_population/2))

        # Picks a solution based on a roulette wheel selection system?
        if r1 > sol_prob[name]:
            # Onlooker bees generate a new solution using random neighbourhood search
            new_search = np.random.uniform(0, value[1], [2, 1])
            new_solution = []
            for i in range(2):
                r1 = random.uniform(-1, 1)
                r2 = random.uniform(0, 1)
                r3 = random.randint(0, 3)
                new_solution.append(value[i] + r1 * r2**r3 * (value[i] - new_search[i]))

            # Generate solution values of new food sources
            new_sol_value = f(new_solution[0], new_solution[1])

            if new_sol_value < employed_bee_solutions[name]:
                # If a better solution is found, replace the old solution
                employed_bee_militia[name] = np.array(new_solution)
                employed_bee_solutions[name] = new_sol_value
            else:
                # Counter the abandon food value
                abandon_food[name] += 1

    # Scout bees will abandon food source if not worked on after 5 iterations
    for name in employed_bee_militia.keys():
        if abandon_food[name] > 100:
            # Scout bees will now search for new solutions between given bounds
            """
            lb = 0
            ub = a**2
            new_solution = []
            for i in range(2):
                r = random.uniform(-1, 1)
                new_solution.append(lb + r * (ub - lb))
            """
            min_sol_name = min(employed_bee_solutions, key=employed_bee_solutions.get)
            new_search = np.random.uniform(0, a**2, [2,1])
            new_solution = []
            for i in range(2):
                r2 = random.uniform(-1, 1)
                new_solution.append(employed_bee_militia[min_sol_name][i] + r2 * (employed_bee_militia[min_sol_name][i] - new_search[i]))

            # Generate solution values of new food sources
            new_sol_value = f(new_solution[0], new_solution[1])

            # Replaces abandoned food source with new one
            employed_bee_militia[name] = np.array(new_solution)
            employed_bee_solutions[name] = new_sol_value

            # Restarts abandon counter
            abandon_food[name] = 0

    # Identify best solution in each iteration 
    min_sol_name = min(employed_bee_solutions, key=employed_bee_solutions.get)

    if employed_bee_solutions[min_sol_name] < best_value:
        old_best_value = best_value
        best_sol = employed_bee_militia[min_sol_name]
        best_value = employed_bee_solutions[min_sol_name]

    # Termination conditions (problem with this)
    abs_diff = old_best_value - best_value
    rel_diff = (old_best_value - best_value)/old_best_value

    if best_value < 9e-3 and abs_diff < 0.01:
        end_counter += 1
    else:
        end_counter = 0

    iter_count += 1

    if iter_count % 100 == 0:
        print(
            """
                Best solution found = {}, {}
                Value of best = {}
                Value of rbest = {}
                Nu. of iterations = {} 
            """.format(float(best_sol[0]), float(best_sol[1]), float(best_value), float(rel_diff), iter_count)
            )

    # If after 10 iterations, there is no change then break the while loop
    if end_counter == 10:
        break

time_end = time.time()

# Prints final solution
print(
    """
    Artificial Bee Colony on Rosenbrock Equation (a={}, b={})
    Best solution found = {}, {}
    Value of best = {}
    Nu. of iterations = {} 
    Time elasped = {}s
    """.format(a, b, float(best_sol[0]), float(best_sol[1]), float(best_value), iter_count, (time_end - time_start))
)
