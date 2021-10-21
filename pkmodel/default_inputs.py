"""Default inputs used in the absence of user making a choice"""

#Models
number_of_models = 2

"""Model 1"""
m1_time = 100

#Dose information
m1_continous_dose_amount = 1
m1_instantaneous_dose_amount = 1
m1_dose_times = [0, 1 / 2, 1]
m1_dose_entry = 'subcutaneous'

#Compartments
m1_number_of_compartments = 2

#Central comparment
m1_volume_c = 1
m1_q_c_initial = 1
m1_CL = 1

#First compartment
m1_volume_1 = 1
m1_q_1_initial = 1
m1_flux_1 = 1

#Second compartment
m1_volume_2 = 2
m1_q_2_initial = 1
m1_flux_2 = 2

#Subcutaneous dosing info
m1_k_a = 1
m1_q_0_initial = 1

"""Model 2"""
m2_time = 100

#Dose information
m2_continous_dose_amount = 1
m2_instantaneous_dose_amount = 1
m2_dose_times = [0, 1 / 2, 1]
m2_dose_entry = 'subcutaneous'

#Compartments
m2_number_of_compartments = 2

#Central comparment
m2_volume_c = 1
m2_q_c_initial = 1
m2_CL = 1

#First compartment
m2_volume_1 = 1
m2_q_1_initial = 1
m2_flux_1 = 1

#Second compartment
m2_volume_2 = 2
m2_q_2_initial = 1
m2_flux_2 = 2

#Subcutaneous dosing info
m2_k_a = 1
m2_q_0_initial = 1
