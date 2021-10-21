"""Default inputs used in the absence of user making a choice"""

#Models
number_of_models = 2  # number of models to compare

model_1_inputs = {"m1_time": 100,  #time the first model runs for
                  "m1_continous_dose_amount": 1,  #
                  "m1_instantaneous_dose_amount": 1,  # adf
                  "m1_dose_times": [0, 1 / 2, 1],
                  "m1_dose_entry": 'subcutaneous',

                  "m1_number_of_compartments": 2,

                  "m1_volume_c": 1,
                  "m1_q_c_initial": 1,
                  "m1_CL": 1,

                  "m1_volume_1": 1,
                  "m1_q_1_initial": 1,
                  "m1_flux_1": 1,

                  "m1_volume_2": 2,
                  "m1_q_2_initial": 1,
                  "m1_flux_2": 2,

                  "m1_k_a": 1,
                  "m1_q_0_initial": 1}

model_2_inputs = {"m2_time": 100,
                  "m2_continous_dose_amount": 1,
                  "m2_instantaneous_dose_amount": 1,
                  "m2_dose_times": [0, 1 / 2, 1],
                  "m2_dose_entry": 'subcutaneous',

                  "m2_number_of_compartments": 2,

                  "m2_volume_c": 1,
                  "m2_q_c_initial": 1,
                  "m2_CL": 1,

                  "m2_volume_1": 1,
                  "m2_q_1_initial": 1,
                  "m2_flux_1": 1,

                  "m2_volume_2": 2,
                  "m2_q_2_initial": 1,
                  "m2_flux_2": 2,

                  "m2_k_a": 1,
                  "m2_q_0_initial": 1}

