"""Imports values from the file default_inputs.py and creates the models

Inputs:
\n number_of_models: number of models to compare as int
\n model_1_inputs: Initial model 1 parameters as dictionaries stored in inputs.py
\n model_2_inputs: Initial model 2 parameters as dictionaries stored in inputs.py
\n Default: None if the user does not want to compare 2 models

Outputs:
\n model_1 is all the informaiton for model_1
\n model_2 is all the informaiton for model_2
\n solution_1 contains a time array for plotting the solution
\n solution_2 contains a time array for plotting the solution

"""

#import classes
from .model import Model
from .dose import Dose
from .solution import Solution

def create_model(number_of_models, model_1_inputs, model_2_inputs=None):

    #setup model 1
    model_1 = Model()

    #assign the dose information to the Dose class
    dose_m1 = Dose(c_amount=model_1_inputs["m1_continous_dose_amount"],
                   i_amount=model_1_inputs["m1_instantaneous_dose_amount"],
                   i_times=model_1_inputs["m1_dose_times"])

    #add the dose information to the model
    model_1.dose = dose_m1

    #set the type of dosing
    if dose_m1.c_amount == 0:
        model_1.dose_type = 'i'
    elif dose_m1.i_amount == 0:
        model_1.dose_type = 'c'
    else:
        model_1.dose_type = 'b'

    #create a dose comparment if the dose type is subcutaneous
    if model_1_inputs["m1_dose_entry"] == 'subcutaneous':
        dose_compartment_m1 = Dosing(v=0,
                                     q=model_1_inputs["m1_q_0_initial"],
                                     ka=model_1_inputs["m1_k_a"])
        model_1.compartments.append(dose_compartment_m1)

    #add information about the central compartment to the model class
    central_compartment_m1 = Central(v=model_1_inputs["m1_volume_c"],
                                     q=model_1_inputs["m1_q_c_initial"],
                                     CL=model_1_inputs["m1_CL"])
    model_1.compartments.append(central_compartment_m1)

    #add information about the peripheral compartment to the model class
    peripheral_compartment_m1_1 = Peripheral(v=model_1_inputs["m1_volume_1"],
                                             q=model_1_inputs["m1_q_1_initial"],
                                             Q=model_1_inputs["m1_flux_1"])
    model_1.compartments.append(peripheral_compartment_m1_1)

    model_1.time = model_1_inputs["m1_time"]

    #add up a time array into the solution class
    solution_m1 = Solution(t=model_1_inputs["m1_time"])

    #add information about the 2nd peripheral compartment to the model class
    if model_1_inputs["m1_number_of_compartments"] == 2:
        peripheral_compartment_m1_2 = Peripheral(v=model_1_inputs["m1_volume_2"],
                                                 q=model_1_inputs["m1_q_2_initial"],
                                                 Q=model_1_inputs["m1_flux_2"])
        model_1.compartments.append(peripheral_compartment_m1_2)

    model_1.num_compartments = len(model_1.compartments)

    #setup model 2

    if number_of_models == 2:
        model_2 = Model()

        #assign the dose information to the Dose class
        dose_m2 = Dose(c_amount=model_2_inputs["m2_continous_dose_amount"],
                       i_amount=model_2_inputs["m2_instantaneous_dose_amount"],
                       i_times=model_2_inputs["m2_dose_times"])
        #add the dose information to the model
        model_2.dose = dose_m2

        #set the type of dosing
        if dose_m2.c_amount == 0:
            model_2.dose_type = 'i'
        elif dose_m2.i_amount == 0:
            model_2.dose_type = 'c'
        else:
            model_2.dose_type = 'b'

        #create a dose comparment if the dose type is subcutaneous
        if model_2_inputs["m2_dose_entry"] == 'subcutaneous':
            dose_compartment_m2 = Dosing(v=0,
                                        q=model_2_inputs["m2_q_0_initial"],
                                        ka=model_2_inputs["m2_k_a"])
            model_2.compartments.append(dose_compartment_m2)

        #add information about the central compartment to the model class
        central_compartment_m2 = Central(v=model_2_inputs["m2_volume_c"],
                                        q=model_2_inputs["m2_q_c_initial"],
                                        CL=model_2_inputs["m2_CL"])
        model_2.compartments.append(central_compartment_m2)

        #add information about the peripheral compartment to the model class
        peripheral_compartment_m2_1 = Peripheral(v=model_2_inputs["m2_volume_1"],
                                                q=model_2_inputs["m2_q_1_initial"],
                                                Q=model_2_inputs["m2_flux_1"])
        model_2.compartments.append(peripheral_compartment_m2_1)

        model_2.time = model_2_inputs["m2_time"]

        #add up a time array into the solution class
        solution_m2 = Solution(t=model_2_inputs["m2_time"])

        #add information about the 2nd peripheral compartment to the model class
        if model_2_inputs["m2_number_of_compartments"] == 2:
            peripheral_compartment_m2_2 = Peripheral(v=model_2_inputs["m2_volume_2"],
                                                    q=model_2_inputs["m2_q_2_initial"],
                                                    Q=model_2_inputs["m2_flux_2"])
            model_2.compartments.append(peripheral_compartment_m2_2)

        model_2.num_compartments = len(model_2.compartments)

        return model_1, model_2, solution_m1, solution_m2
    else:
        return model_1, solution_m1


