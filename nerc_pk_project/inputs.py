"""Default inputs used in the absence of user making a choice. \n
For information on the physical meaning of each of the constants see scientific background.

Variables:
    number_of_models: number of models to compare (int) \n
    model_1_inputs: input information for model 1 (dict) \n
    model_2_inputs: input information for model 2 (dict)

    model_dictionaries:
        mX_time: time the model runs for (h) \n
        mX_timestep: time step for model calculations (h) \n

        mX_continous_dose_amount: |Dose| [ng] \n
        mX_instantaneous_dose_amount: |Dose| [ng] \n
        mX_dose_times: (t) in Dose(t) [hours] \n
        mX_dose_entry: subcutaneous or intravenous bolus \n

        mX_number_of_compartments: number of peripheral compartments \n

        mX_volume_c: V_c [mL] \n
        mX_q_c_initial: q_c(t=0) [ng] \n
        mX_CL: CL [mL/hour] \n

        mX_volume_1: V_{p1} [mL] \n
        mX_q_1_initial: q_{p1}(t=0) [ng] \n
        mX_flux_1: Q_{p1} [mL/hour] \n

        mX_volume_2: V_{p2} [mL] \n
        mX_q_2_initial: q_{p2}(t=0) [ng] \n
        mX_flux_2": Q_{p2} [mL/hour] \n

        mX_k_a": k_a [/hour] \n
        mX_q_0_initial: q_0(t=0) [ng] \n

"""

#Models
number_of_models = 2  # number of models to compare


model_1_inputs = {"m1_time": 1,  #time the first model runs for
                  "m1_timestep": 0.001, #time step for model calculations

                  "m1_continous_dose_amount": 1,  # |Dose| [ng]
                  "m1_instantaneous_dose_amount": 1,  # |Dose| [ng]
                  "m1_dose_times": [0, 1 / 2, 1],  # (t) in Dose(t) [hours]
                  "m1_dose_entry": 'subcutaneous',  # subcutaneous or intravenous bolus

                  "m1_number_of_compartments": 2,  # number of peripheral compartments

                  "m1_volume_c": 1,  # V_c [mL]
                  "m1_q_c_initial": 1,  # q_c(t=0) [ng]
                  "m1_CL": 1,  # CL [mL/hour]

                  "m1_volume_1": 1,  # V_{p1} [mL]
                  "m1_q_1_initial": 1,  # q_{p1}(t=0) [ng]
                  "m1_flux_1": 1,  # Q_{p1} [mL/hour]

                  "m1_volume_2": 2,  # V_{p2} [mL]
                  "m1_q_2_initial": 1,  # q_{p2}(t=0) [ng]
                  "m1_flux_2": 2,  # Q_{p2} [mL/hour]

                  "m1_k_a": 1,  # k_a [/hour]
                  "m1_q_0_initial": 1}  # q_0(t=0) [ng]


model_2_inputs = {"m2_time": 1, #time the first model runs for
                  "m2_timestep": 0.001, #time step for model calculations

                  "m2_continous_dose_amount": 1, # |Dose| [ng]
                  "m2_instantaneous_dose_amount": 1, # |Dose| [ng]
                  "m2_dose_times": [0, 1 / 2, 1], #(t) in Dose(t) [hours]
                  "m2_dose_entry": 'subcutaneous', #  subcutaneous or intravenous bolus

                  "m2_number_of_compartments": 2,  # number of peripheral compartments

                  "m2_volume_c": 1,  # V_c [mL]
                  "m2_q_c_initial": 1,  # q_c(t=0) [ng]
                  "m2_CL": 1,  # CL [mL/hour]

                  "m2_volume_1": 1,  # V_{p1} [mL]
                  "m2_q_1_initial": 1,  # q_{p2}(t=0) [ng]
                  "m2_flux_1": 1,  # Q_{p1} [mL/hour]

                  "m2_volume_2": 2,  # V_{p2} [mL]
                  "m2_q_2_initial": 1,  # q_{p2}(t=0) [ng]
                  "m2_flux_2": 2,  # Q_{p2} [mL/hour]

                  "m2_k_a": 1,  # k_a [/hour]
                  "m2_q_0_initial": 1}  # q_0(t=0) [ng]

