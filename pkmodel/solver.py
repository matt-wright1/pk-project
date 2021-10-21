"""Imports values from the file default_inputs.py and creates the models

model_1 is all the informaiton for model_1
model_1 is all the informaiton for model_1
solution_1 contains a time array for plotting the solution
solution_2 contains a time array for plotting the solution
"""

#import packages
import os
os.chdir('pkmodel/')
os.getcwd()
import numpy as np
import scipy.integrate
import matplotlib.pylab as plt

#import classes
#from dose import *
#from compartments import *
#from solution import *
from model import *

def dose(t, X):
    return X

def intravenous(t, y, Q_p1, V_c, V_p1, CL, X):
    q_c, q_p1 = y
    transition = Q_p1 * (q_c / V_c - q_p1 / V_p1)
    dqc_dt = dose(t, X) - q_c / V_c * CL - transition
    dqp1_dt = transition
    return [dqc_dt, dqp1_dt]

def subcutaneous(t, y, Q_p1, V_c, V_p1, CL, X):
    q_c, q_p1 = y
    transition = Q_p1 * (q_c / V_c - q_p1 / V_p1)
    dqc_dt = dose(t, X) - q_c / V_c * CL - transition
    dqp1_dt = transition
    return [dqc_dt, dqp1_dt]

def solve(model):
    model_args = {
        'name': 'change this if we have a model name property?',
        'Q_p1': 1.0,
        'V_c': 1.0,
        'V_p1': 1.0,
        'CL': 1.0,
        'X': 1.0,
    }
    for model in [model_args]:
        args = [model['Q_p1'], model['V_c'], model['V_p1'], model['CL'], model['X']]
        sol = scipy.integrate.solve_ivp(
            fun=lambda t, y: rhs(t, y, *args),
            t_span=[t_eval[0], t_eval[-1]],
            y0=y0, t_eval=t_eval
            )
        plt.plot(sol.t, sol.y[0, :], label=model['name'] + '- q_c')
        plt.plot(sol.t, sol.y[1, :], label=model['name'] + '- q_p1')
    plt.legend()
    plt.ylabel('drug mass [ng]')
    plt.xlabel('time [h]')
    plt.show()




###main test
t_eval = np.linspace(0, 1, 1000)
y0 = np.array([0.0, 0.0]) 
solution = solve('Model1')
