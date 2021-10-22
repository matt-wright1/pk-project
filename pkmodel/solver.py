"""
Solves the differential equations for a given model.

Inputs:
\n model: model parameters, dosage information.

Outputs:
\n solution: the concentration in each compartment as a function of time

"""
#import packages
import os
os.chdir('pkmodel/')
#os.getcwd()
import numpy as np
import scipy.integrate
import matplotlib.pylab as plt

#import classes
from .model import Model

def create_dose_array(model):
    """
    Function to calculate the dose as a time array based on the inputs to the model.

    :param model: Model object with information on dosage

    Returns an array of the dose to be applied at every timestep.
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

def dose(t, X):
    return X

def rhs(t, y, protocol, Q_p1, Q_p2, V_c, V_p1, V_p2, CL, X, k_a):
    q_0, q_c, q_p1, q_p2 = y
    if protocol == 'intravenous':
        ka_q0 = dose(t, X)
    else:
        ka_q0 = k_a * q_0
    transition1 = Q_p1 * (q_c / V_c - q_p1 / V_p1)
    transition2 = Q_p2 * (q_c / V_c - q_p2 / V_p2)
    dq0_dt = dose(t, X) - ka_q0
    dqc_dt = ka_q0 - q_c / V_c * CL - transition1 - transition2
    dqp1_dt = transition1
    dqp2_dt = transition2
    return [dq0_dt, dqc_dt, dqp1_dt, dqp2_dt]


def solve(model, solution):
    t_eval = np.arange(0, (model.time + model.timestep), model.timestep)
    y0 = np.array([model.compartments['dose'].q,
                   model.compartments['central'].q,
                   model.compartments['peripheral_1'].q,
                   model.compartments['peripheral_2'].q,])

    model_args = {
        'protocol': 'subcutaneous',
        'Q_p1': model.compartments['peripheral_1'].Q,
        'Q_p2': model.compartments['peripheral_2'].Q,
        'V_c': model.compartments['central'].v,
        'V_p1': model.compartments['peripheral_1'].v,
        'V_p2': model.compartments['peripheral_2'].v,#this term must always be non-zero
        'CL': model.compartments['central'].CL,
        'X': 1.0,
        'k_a': model.compartments['dose'].ka}

    for model in [model_args]:
        args = [
            model['protocol'],
            model['Q_p1'],
            model['Q_p2'],
            model['V_c'],
            model['V_p1'],
            model['V_p2'],
            model['CL'],
            model['X'],
            model['k_a']]
        sol = scipy.integrate.solve_ivp(
            fun=lambda t, y: rhs(t, y, *args),
            t_span=[t_eval[0], t_eval[-1]],
            y0=y0, t_eval=t_eval)

    solution.t = sol.t
    solution.q0 = sol.y[0, :]
    solution.qC = sol.y[1, :]
    solution.q1 = sol.y[2, :]
    solution.q2 = sol.y[3, :]

    return solution


###main test
#protocol = 'intravenous'
#protocol = 'subcutaneous'

'''
plt.plot(sol.t, sol.y[0, :], label='- q_0')
plt.plot(sol.t, sol.y[1, :], label='- q_c')
plt.plot(sol.t, sol.y[2, :], label='- q_p1')
plt.plot(sol.t, sol.y[3, :], label='- q_p2')
plt.legend()
plt.ylabel('drug mass [ng]')
plt.xlabel('time [h]')
plt.show()
'''



