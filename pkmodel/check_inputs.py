def check_inputs(number_of_models, model_1_inputs, model_2_inputs=None):

    """Checks that the user inputs make logical sense
    e.g. have they specified the number of models to be 2
    but only given data for one model."""

    # check model comparison information

    # check model 2 is added if number of models is set to 2
    if number_of_models == 2 and model_2_inputs is None:
        raise ValueError("Expect model 2 data and got None. To fix either set number_of_models = 1 \
            or enter data for Model 2")

    # warning if number of models is set to 1 but data for model 2 exists
    if number_of_models == 1 and model_2_inputs is not None:
        raise ValueError("Warning: model 2 data will not be used. \
            To fix set number_of_models = 2.")

    # check model 1 data

    # warning if instantenous dose is specified
    # but no times are given for the dose
    if model_1_inputs["m1_instantaneous_dose_amount"] != 0 \
            and model_1_inputs["m1_dose_times"] == []:
        raise ValueError("Warning: enter times for instantenous dose \
            or set m1_instantaneous_dose_amount to 0.")

    # warning if times are given for the instantanous dose
    # but no dose quantity is given
    if model_1_inputs["m1_instantaneous_dose_amount"] == 0 \
            and model_1_inputs["m1_dose_times"]:
        raise ValueError("Warning: enter m1_instantenous_dose_amount \
            or set m1_dose_times to [].")

    # warnings if compartment volumes are zero or negative
    if model_1_inputs["m1_volume_c"] <= 0:
        raise ValueError("Set m1_volume_c to a positive value.")

    if model_1_inputs["m1_volume_1"] <= 0:
        raise ValueError("Set m1_volume_1 to a positive value.")

    if model_1_inputs["m1_number_of_compartments"] == 2 \
            and model_1_inputs["m1_volume_2"] <= 0:
        raise ValueError("Set m1_volume_2 to a positive value \
            or set m1_number_of_compartments to 1.")

    # warning if size of second peripheral compartment is non-zero
    # and number of compartments is set to 1
    if model_1_inputs["m1_number_of_compartments"] == 1 \
            and model_1_inputs["m1_volume_2"] != 0:
        raise ValueError("2nd peripheral compartment won't be included. \
            Set m1_number_of_compartments to 2 to include.")

    # warning if dosing is set to subcutaneous but ka is 0
    if model_1_inputs["m1_dose_entry"] == 'subcutaneous' \
            and model_1_inputs["m1_k_a"] == 0:
        raise ValueError("Dosing is set to subcutaneous and ka = 0 \
            so dose won't be absorbed.")

    # warning if dosing is not subcutenous but ka is non-zero
    if model_1_inputs["m1_dose_entry"] != 'subcutaneous' \
            and model_1_inputs["m1_k_a"] != 0:
        raise ValueError("m1_dose_entry not subcutaneous \
            so dose compartment won't be added.")

    # check model 2 data

    # warning if instantenous dose is specified
    # but no times are given for the dose
    if model_2_inputs["m2_instantaneous_dose_amount"] != 0 \
            and model_2_inputs["m2_dose_times"] == []:
        raise ValueError("Warning: enter times for instantenous dose \
            or set m2_instantaneous_dose_amount to 0.")

    # warning if times are given for the instantanous dose
    # but no dose quantity is given
    if model_2_inputs["m2_instantaneous_dose_amount"] == 0 \
            and model_2_inputs["m2_dose_times"]:
        raise ValueError("Warning: enter m2_instantenous_dose_amount \
            or set m2_dose_times to [].")

    # warnings if compartment volumes are zero or negative
    if model_2_inputs["m2_volume_c"] <= 0:
        raise ValueError("Set m2_volume_c to a positive value.")

    if model_2_inputs["m2_volume_1"] <= 0:
        raise ValueError("Set m2_volume_1 to a positive value.")

    if model_2_inputs["m2_number_of_compartments"] == 2 \
            and model_2_inputs["m2_volume_2"] <= 0:
        raise ValueError("Set m2_volume_2 to a positive value \
            or set m2_number_of_compartments to 1.")

    # warning if size of second peripheral compartment is non-zero
    # and number of compartments is set to 1
    if model_2_inputs["m2_number_of_compartments"] == 1 \
            and model_2_inputs["m2_volume_2"] != 0:
        raise ValueError("2nd peripheral compartment won't be included. \
            Set m2_number_of_compartments to 2 to include.")

    # warning if dosing is set to subcutaneous but ka is 0
    if model_2_inputs["m2_dose_entry"] == 'subcutaneous' \
            and model_2_inputs["m2_k_a"] == 0:
        raise ValueError("Dosing is set to subcutaneous and ka = 0 \
            so dose won't be absorbed.")

    # warning if dosing is not subcutenous but ka is non-zero
    if model_2_inputs["m2_dose_entry"] != 'subcutaneous' \
            and model_2_inputs["m2_k_a"] != 0:
        raise ValueError("m2_dose_entry not subcutaneous \
            so dose compartment won't be added.")
