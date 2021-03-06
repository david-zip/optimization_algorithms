"""
Simulated Annealling

Date: 13/03/22
"""
import time
import numpy as np

class SA():
    """
    Simulated annealling for minimisation problems
    """

    def __init__(self, xBounds: list[float], yBounds: list[float], Ti: float = 1, Tf: float = 0.1, maxIter: int = 1000, maxTime: int = 100):
        """
        Initialize algorithm hyper-parameters

        xBounds = x-axis boundaries

        yBounds = y-axis boundaries

        Ti = Initial temperature (default: 1)

        Tf = Final temperature (default: 0.1)

        maxIter = Maximum number of iterations (default: 1000)

        maxTime = Maximum run time in seconds (default: 100)
        """
        # x boundaries
        self.xlb = min(xBounds)
        self.xub = max(xBounds)

        # y boundaries
        self.ylb = min(yBounds)
        self.yub = max(yBounds)

        # Store initial tempeartures
        self.Ti0 = Ti
        self.Tf0 = Tf
        self.T0 = Ti
        self.eps0 = 1 - (Tf/Ti)**(maxIter**(-1))

        # Maximum iterations/time
        self.maxIter = maxIter
        self.maxTime = maxTime

    def _initialize(self, f):
        """
        Initialize random starting solutions
        """
        # Initialize random positions
        x = np.random.uniform(self.xlb, self.xub)
        y = np.random.uniform(self.ylb, self.yub)
        
        # Store best solutions
        self.best_solution = np.array([x,y])
        self.best_value = f(self.best_solution[0], self.best_solution[1])

        # Initialize inital temperatures
        self.Ti = self.Ti0
        self.Tf = self.Tf0
        self.T = self.Ti0
        self.eps = self.eps0

        return self.best_solution, self.best_value

    def _neighbourhood_search(self, f):
        """
        Random neighbourhood search
        """
        # Generate random solutions within bounds
        x = np.random.uniform(self.xlb, self.xub)
        y = np.random.uniform(self.ylb, self.yub)

        # Generate new solutions
        self.new_solution = np.array([x,y])
        self.new_value = f(self.new_solution[0], self.new_solution[1])

    def _find_best(self):
        """
        Replaces best solution and Metropolis acceptance probability
        """
        # Identify best solution
        if self.new_value < self.best_value:
            self.best_solution = self.new_solution
            self.best_value = self.new_value
        else:
            # Metropolis acceptance probability
            r = np.random.uniform()
            if r < np.exp((self.best_value - self.new_value)/self.T):
                self.best_solution = self.new_solution
                self.best_value = self.new_value
        
        return self.best_solution, self.best_value

    def _cooling_schedule(self):
        """
        Geometric cooling schedule
        """
        self.T *= (1 - self.eps)

        return self.T

    def algorithm(self, f: any, print_output: bool = True):
        """
        Simulated annealling algorithm

        f = Objective function (input a python function)

        print_output = Prints final solution, objective function of solution, number of iterations, and time elapsed (default: True)
        """
        best_values = []

        # Initialize solutions
        self._initialize(f)

        # Store values in a list
        best_values.append(self.best_value)

        # Start algorithm
        nIter = 0
        time_start = time.time()
        while self.T > self.Tf:
            self._neighbourhood_search(f)
            self._find_best()
            self._cooling_schedule()

            # Store values in a list    
            best_values.append(self.best_value)

            # Iteration counter
            nIter += 1
        time_end = time.time()

        if print_output == True:
            print(
    f"""
    Simulated Annealling Solution
    Best solution found = {self.best_solution[0]}, {self.best_solution[1]}
    Value of best = {self.best_value}
    No. iterations = {nIter}
    Time elasped = {time_end - time_start}s
    """
                )

        return best_values
    
    def time_algorithm(self, f: any, print_output: bool = True):
        """
        Simulated annealling algorithm

        f = Objective function (input a python function)

        print_output = Prints final solution, objective function of solution, number of iterations, and time elapsed (default: True)
        """
        best_values = []
        best_values_time = []

        # Initialize solutions
        self._initialize(f)

        # Store values in a list
        best_values.append(self.best_value)

        # Start algorithm
        nIter = 0
        time_start = time.time()
        time_elapsed = 0
        while time_elapsed < self.maxTime:
            self._neighbourhood_search(f)
            self._find_best()
            self._cooling_schedule()
            
            # Store values in a list    
            time_current = time.time()
            time_elapsed = time_current - time_start

            best_values_time.append(time_elapsed)

            best_values.append(self.best_value)

            # Iteration counter
            nIter += 1
        
        time_end = time.time()

        if print_output == True:
            print(
    f"""
    Simulated Annealling Solution
    Best solution found = {self.best_solution[0]}, {self.best_solution[1]}
    Value of best = {self.best_value}
    No. iterations = {nIter}
    Time elasped = {time_end - time_start}s
    """
                )

        return best_values, best_values_time


if __name__=="__main__":
    
    def f(x,y):
        return x**2 + y**2 
    
    xBounds = [-3,3]
    yBounds = [-3,3]

    test = SA(xBounds, yBounds, Ti=100, Tf=0.01, maxIter=10000, maxTime=60)
    test.time_algorithm(f)

    def f(x,y):
        return (x + 2*y - 7)**2 + (2*x + y - 5)**2

    xBounds = [-10,10]
    yBounds = [-10,10]

    test2 = SA(xBounds, yBounds)
    test2.time_algorithm(f)