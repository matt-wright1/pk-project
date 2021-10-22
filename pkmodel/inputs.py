"""Default inputs used in the absence of user making a choice

Variables:
    number_of_models: number of models to compare (int)
    model_1_inputs: input information for model 1 (dict)
    model_2_inputs: input information for model 2 (dict)
"""

#Models
number_of_models = 2  # number of models to compare

model_1_inputs = {"m1_time": 100,  #time the first model runs for
                  "m1_continous_dose_amount": 1,  # |Dose| [ng]
                  "m1_instantaneous_dose_amount": 1,  # |Dose| [ng]
                  "m1_dose_times": [0, 1 / 2, 1],  #(t) in Dose(t) [hours]
                  "m1_dose_entry": 'subcutaneous', #subcutaneous or intravenous bolus

                  "m1_number_of_compartments": 2, # number of peripheral compartments

                  "m1_volume_c": 1, # V_c [mL]
                  "m1_q_c_initial": 1, # q_c(t=0) [ng]
                  "m1_CL": 1, # CL [mL/hour]

                  "m1_volume_1": 1, # V_{p1} [mL]
                  "m1_q_1_initial": 1, # q_{p1}(t=0) [ng]
                  "m1_flux_1": 1, #Q_{p1} [mL/hour]

                  "m1_volume_2": 2, # V_{p2} [mL]
                  "m1_q_2_initial": 1, # q_{p2}(t=0) [ng]
                  "m1_flux_2": 2, #Q_{p2} [mL/hour]

                  "m1_k_a": 1, # k_a [/hour]
                  "m1_q_0_initial": 1} #  q_0(t=0) [ng]

model_2_inputs = {"m2_time": 100, #time the first model runs for
                  "m2_continous_dose_amount": 1, # |Dose| [ng]
                  "m2_instantaneous_dose_amount": 1, # |Dose| [ng]
                  "m2_dose_times": [0, 1 / 2, 1], #(t) in Dose(t) [hours]
                  "m2_dose_entry": 'subcutaneous', #  subcutaneous or intravenous bolus

                  "m2_number_of_compartments": 2, # number of peripheral compartments

                  "m2_volume_c": 1, # V_c [mL]
                  "m2_q_c_initial": 1, # q_c(t=0) [ng]
                  "m2_CL": 1, # CL [mL/hour]

                  "m2_volume_1": 1, # V_{p1} [mL]
                  "m2_q_1_initial": 1, # q_{p2}(t=0) [ng]
                  "m2_flux_1": 1, #Q_{p1} [mL/hour]

                  "m2_volume_2": 2, # V_{p2} [mL]
                  "m2_q_2_initial": 1, # q_{p2}(t=0) [ng]
                  "m2_flux_2": 2, #Q_{p2} [mL/hour]

                  "m2_k_a": 1, # k_a [/hour]
                  "m2_q_0_initial": 1} #  q_0(t=0) [ng]

