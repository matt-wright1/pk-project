"""Imports values from the file default_inputs.py and creates the models

model_1 is all the informaiton for model_1
model_1 is all the informaiton for model_1
solution_1 contains a time array for plotting the solution
solution_2 contains a time array for plotting the solution
"""

#this needs to go in main

#choose initial file for inputs
from default_inputs import *

#import classes
from dose import *
from compartments import *
from solution import *
from model import *

def create_model():

    #setup model 1
    model_1 = Model()

    dose_m1 = Dose(c_amount=m1_continous_dose_amount, i_amount=m1_instantaneous_dose_amount, i_times=m1_dose_times)
    model_1.dose = dose_m1
    if dose_m1.c_amount == 0:
        model_1.dose_type = 'i'
    elif dose_m1.i_amount == 0:
        model_1.dose_type = 'c'
    else:
        model_1.dose_type = 'b'

    if m1_dose_entry == 'subcutaneous':
        dose_compartment_m1 = Dosing(v = 0, q = m1_q_0_initial, ka = m1_k_a)
        model_1.compartments.append(dose_compartment_m1)

    central_compartment_m1 = Central(v=m1_volume_c, q=m1_q_c_initial, CL=m1_CL)
    model_1.compartments.append(central_compartment_m1)

    peripheral_compartment_m1_1 = Peripheral(v=m1_volume_1, q=m1_q_1_initial, Q=m1_flux_1)
    model_1.compartments.append(peripheral_compartment_m1_1)

    solution_m1 = Solution(t = m1_time)

    if m1_number_of_compartments==2:
        peripheral_compartment_m1_2 = Peripheral(v=m1_volume_2, q=m1_q_2_initial, Q=m1_flux_2)
        model_1.compartments.append(peripheral_compartment_m1_1)

    model_1.num_compartments = len(model_1.compartments)

    #setup model 2

    if number_of_models==2:
        model_2 = Model()

        dose_m2 = Dose(c_amount=m2_continous_dose_amount, i_amount=m2_instantaneous_dose_amount, i_times=m2_dose_times)
        model_2.dose = dose_m2

        if dose_m2.c_amount == 0:
            model_2.dose_type = 'i'
        elif dose_m2.i_amount == 0:
            model_2.dose_type = 'c'
        else:
            model_2.dose_type = 'b'

        if m2_dose_entry == 'subcutaneous':
            dose_compartment_m2 = Dosing(v = 0, q = m1_q_0_initial, ka = m1_k_a)
            model_2.compartments.append(dose_compartment_m2)
        central_compartment_m2 = Central(v=m1_volume_c, q=m1_q_c_initial, CL=m1_CL)
        model_2.compartments.append(central_compartment_m2)
        peripheral_compartment_m2_1 = Peripheral(v=m1_volume_1, q=m1_q_1_initial, Q=m1_flux_1)
        model_2.compartments.append(peripheral_compartment_m2_1)
        solution_m2 = Solution(t = m2_time)

        if m2_number_of_compartments==2:
            peripheral_compartment_m2_2 = Peripheral(v=m1_volume_2, q=m1_q_2_initial, Q=m1_flux_2)
            model_2.compartments.append(peripheral_compartment_m2_2)
        
        model_2.num_compartments = len(model_2.compartments)
    
    return model_1, model_2, solution_m1, solution_m2

