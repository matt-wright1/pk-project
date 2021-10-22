"""Define functions that are used to plot different graphs of the solutions to the PK problem.
"""

from .model import Model
from .solution import Solution

def single_plot(solution):
    """Define a function which makes a single plot of the solution
    as a function of time.

    :param model: model object
    """
    from pkmodel import Dose, Model, Solution
    import matplotlib.pyplot as plt

    

    fig = plt.figure()
    x_values = solution.t[:]
    label=['q1', 'q2', 'q0', 'qc']
    i=0 # created for labelling
    for q_values in [solution.q1, solution.q2, solution.q0, solution.qC]:
        if q_values.all() == None: return
        else:
            plt.plot(x_values, q_values, label = "%s" %label[i])
        i=+1
    #import labels from inputs.py
    from pkmodel.inputs import model_1_inputs
    dose_entry=model_1_inputs["m1_dose_entry"]
    no_comp=model_1_inputs["m1_number_of_compartments"]
    

    plt.title('Pharmokinetic model: {} peripheral compartments, {} dosing'.format(no_comp,dose_entry))
    plt.legend()
    plt.ylabel('drug mass [ng]')
    plt.xlabel('time [hr]')
    plt.show()

def double_plot(solution1, solution2):
    """Define a function which makes a plot comparing the solutions
    of two models as a function of time.

    :param model1: model object
    :param model2: model object

    """
    
    from pkmodel import Dose, Model, Solution
    import matplotlib.pyplot as plt
    
    

    fig = plt.figure(figsize=[20,15],tight_layout=True)
    ax1=plt.subplot(1,2,1)
    x_values = solution1.t[:]
    q_values=[solution1.q1, solution1.q2, solution1.q0, solution1.qC]
    label=['q1', 'q2', 'q0', 'qc']
    i=0 # created for labelling
    for q in q_values:
        
        if q.all() == None: return
        else:
            ax1.plot(x_values, q, label = "%s" %label[i])
        i=+1
    ax1.legend()
    #import labels from inputs.py can change labels in title below
    from pkmodel.inputs import model_1_inputs
    dose_entry=model_1_inputs["m1_dose_entry"]
    no_comp=model_1_inputs["m1_number_of_compartments"]

    plt.title('Pharmokinetic model: {} peripheral compartments, {} dosing'.format(no_comp,dose_entry))
    plt.ylabel('drug mass [ng]')
    plt.xlabel('time [hr]')

    #create new subplot for second model
    ax2=plt.subplot(1,2,2)
    x_values = solution2.t[:]
    label=['q1', 'q2', 'q0', 'qc']
    i=0 # created for labelling
    for q_values in [solution2.q1, solution2.q2, solution2.q0, solution2.qC]:
        if q_values.all() == None: return
        else:
            ax2.plot(x_values, q_values, label = "%s" %label[i])
        i=+1
    ax2.legend()
    #import labels from inputs.py can change labels in title below
    from pkmodel.inputs import model_2_inputs
    dose_entry=model_2_inputs["m2_dose_entry"]
    no_comp=model_2_inputs["m2_number_of_compartments"]

    plt.title('Pharmokinetic model: {} peripheral compartments, {} dosing'.format(no_comp,dose_entry))
    plt.ylabel('drug mass [ng]')
    plt.xlabel('time [hr]')

    
    plt.show()