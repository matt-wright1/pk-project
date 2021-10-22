"""Define functions that are used to plot different graphs of the solutions to the PK problem.
"""

from model import Model
from solution import Solution

def single_plot(model):
    """Define a function which makes a single plot of the solution
    as a function of time.

    :param model: model object
    """
    from pkmodel import Dose, Model, Solution
    import matplotlib.pyplot as plt

    solution = solve(model)

    fig = plt.figure()
    x_values = solution.t[:]
    for q_values in [solution.q1, solution.q2, solution.q0, solution.qC]:
        if q == None: return
        else:
            plt.plot(x_values, q_values, label = "")

    plt.legend()
    plt.ylabel('drug mass [ng]')
    plt.xlabel('time [hr]')
    plt.show()

def double_plot(model1, model2):
    """Define a function which makes a plot comparing the solutions
    of two models as a function of time.

    :param model1: model object
    :param model2: model object

    """
    
    from pkmodel import Dose, Model, Solution
    import matplotlib.pyplot as plt
    
    solution1 = solve(model1)
    solution2 = solve(model2)

    fig = plt.figure()

    x_values = solution1.t[:]
    for q_values in [solution1.q1, solution1.q2, solution1.q0, solution1.qC]:
        if q == None: return
        else:
            plt.plot(x_values, q_values, label = "")

    x_values = solution2.t[:]
    for q_values in [solution2.q1, solution2.q2, solution2.q0, solution2.qC]:
        if q == None: return
        else:
            plt.plot(x_values, q_values, label = "")

    plt.legend()
    plt.ylabel('drug mass [ng]')
    plt.xlabel('time [hr]')
    plt.show()