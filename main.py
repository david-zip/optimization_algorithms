"""
Run optimization algorithms on test functions

Date 13/03/22
"""
import numpy as np
import matplotlib.pyplot as plt

from algorithms.simulated_annealling import SA
from algorithms.particle_swarm_optimization import PSO
from algorithms.artificial_bee_colony import ABC
from algorithms.genetic_algorithm import GA

from algorithms.test_equations import other, rosenbrock

# Variable bounds
xBounds = [-5,5]
yBounds = [-5,5]

print("\nRosenbrock Equation")
# Simulated annealling
sim_ann = SA(xBounds, yBounds, maxIter=1e4)
R_SA_values = sim_ann.algorithm(rosenbrock.f)

# Particle swarm optimization
par_swa_op = PSO(xBounds, yBounds, maxIter=1e4)
R_PSO_values = par_swa_op.algorithm(rosenbrock.f)

# Artificial bee colony
art_bee_col = ABC(xBounds, yBounds, maxIter=1e4)
R_ABC_values = art_bee_col.algorithm(rosenbrock.f)

# Genetic algorithm
genetic = GA(xBounds, yBounds, maxiter=1e4)
R_GA_values = genetic.algorithm(rosenbrock.f)


print("\n'Other' Equation")
# Simulated annealling
sim_ann = SA(xBounds, yBounds, maxIter=1e4)
A_SA_values = sim_ann.algorithm(other.f)

# Particle swarm optimization
par_swa_op = PSO(xBounds, yBounds, maxIter=1e4)
A_PSO_values = par_swa_op.algorithm(other.f)

# Artificial bee colony
art_bee_col = ABC(xBounds, yBounds, maxIter=1e4)
A_ABC_values = art_bee_col.algorithm(other.f)

# Genetic algorithm
genetic = GA(xBounds, yBounds, maxiter=1e4)
A_GA_values = genetic.algorithm(other.f)

# Plot figures
# Rosenbrock Equation
plt.figure()
plt.suptitle("Simulated Annealing with Rosenbrock Equation - Single Run")
plt.plot(range(len(R_SA_values)), R_SA_values)
plt.ylabel("Objective function")
plt.xlabel("Number of iterations")
plt.savefig('plots/simulated_annealling/Rosenbrock Equation - Single Run.png', dpi=300)

plt.figure()
plt.suptitle("Particle Swarm Optimization with Rosenbrock Equation - Single Run")
plt.plot(range(len(R_PSO_values)), R_PSO_values)
plt.ylabel("Objective function")
plt.xlabel("Number of iterations")
plt.savefig('plots/particle_swarm_optimization/Rosenbrock Equation - Single Run.png', dpi=300)

plt.figure()
plt.suptitle("Artificial Bee Colony with Rosenbrock Equation - Single Run")
plt.plot(range(len(R_ABC_values)), R_ABC_values)
plt.ylabel("Objective function")
plt.xlabel("Number of iterations")
plt.savefig('plots/artificial_bee_colony/Rosenbrock Equation - Single Run.png', dpi=300)

plt.figure()
plt.suptitle("Genetic Algorithm with Rosenbrock Equation - Single Run")
plt.plot(range(len(R_GA_values)), R_GA_values)
plt.ylabel("Objective function")
plt.xlabel("Number of iterations")
plt.savefig('plots/genetic_algorithm/Rosenbrock Equation - Single Run.png', dpi=300)

# 'Antonio' Equation
plt.figure()
plt.suptitle("Simulated Annealing with 'Other' Equation - Single Run")
plt.plot(range(len(A_SA_values)), A_SA_values)
plt.ylabel("Objective function")
plt.xlabel("Number of iterations")
plt.savefig('plots/simulated_annealling/Other Equation - Single Run.png', dpi=300)

plt.figure()
plt.suptitle("Particle Swarm Optimization with 'Other' Equation - Single Run")
plt.plot(range(len(A_PSO_values)), A_PSO_values)
plt.ylabel("Objective function")
plt.xlabel("Number of iterations")
plt.savefig('plots/particle_swarm_optimization/Other Equation - Single Run.png', dpi=300)

plt.figure()
plt.suptitle("Artificial Bee Colony with 'Other' Equation - Single Run")
plt.plot(range(len(A_ABC_values)), A_ABC_values)
plt.ylabel("Objective function")
plt.xlabel("Number of iterations")
plt.savefig('plots/artificial_bee_colony/Other Equation - Single Run.png', dpi=300)

plt.figure()
plt.suptitle("Genetic algorithm with 'Other' Equation - Single Run")
plt.plot(range(len(A_GA_values)), A_GA_values)
plt.ylabel("Objective function")
plt.xlabel("Number of iterations")
plt.savefig('plots/genetic_algorithm/Other Equation - Single Run.png', dpi=300)

# Create 3D plots
xaxis = np.arange(xBounds[0], xBounds[1], 0.1)
yaxis = np.arange(yBounds[0], yBounds[1], 0.1)

x, y = np.meshgrid(xaxis, yaxis)

# Rosenbrock Equation
results = rosenbrock.f(x, y)

figure = plt.figure()
contour = plt.contour(x, y, results, cmap='jet')

x_min = x.ravel()[results.argmin()]
y_min = y.ravel()[results.argmin()]

plt.plot(x_min, y_min, '*')

plt.suptitle('Rosenbrock Equation')
plt.xlabel('x')
plt.ylabel('y')
plt.clabel(contour, inline=1, fontsize=10)

plt.savefig('plots/solutions/Rosenbrock Equation.png', dpi=300)

# 'Antonio' Equation
results = other.f(x, y)

figure = plt.figure()
contour = plt.contour(x, y, results, cmap='jet')

x_min = x.ravel()[results.argmin()]
y_min = y.ravel()[results.argmin()]

plt.plot(x_min, y_min, '*')

plt.suptitle("'Other' Equation")
plt.xlabel('x')
plt.ylabel('y')
plt.clabel(contour, inline=1, fontsize=10)

plt.savefig('plots/solutions/Other Equation.png', dpi=300)
