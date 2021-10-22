#import packages
#import os
#os.chdir('pkmodel/')
#os.getcwd()
import numpy as np
import scipy.integrate
import matplotlib.pylab as plt

#import classes
#from dose import *
#from compartments import *
#from solution import *
#from pkmodel import *


def create_dose_array(model):
    """
    Function to calculate the dose as a time array based on the inputs to the model.
    """
    #assign variables to information from the model
    time = model.time
    timestep = model.time[1] - model.time[0] #assuming constant timestep
    dose_c_amount = timestep * model.dose(c_amount)
    dose_i_amount = model.dose(i_amount)
    dose_i_times = model.dose(i_times)

    # define empty array with same number of rows as number of time steps and 2 columns
    dose_array = np.zeros((len(time)))
    #add continuous amount at each value of time
    dose_array[:] += dose_c_amount

    #add instantaneous dose inputs at the specified times
    for t in dose_i_times:
        loc = np.where(t == time)
        dose_array[loc] += dose_i_amount

    return dose_array[:]

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
        args = [
            model['Q_p1'],
            model['V_c'],
            model['V_p1'],
            model['CL'],
            model['X']]
        sol = scipy.integrate.solve_ivp(
            fun=lambda t, y: intravenous(t, y, *args),
            t_span=[t_eval[0], t_eval[-1]],
            y0=y0, t_eval=t_eval)
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
