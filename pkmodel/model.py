'''Create the model class'''
class Model:
    """Creates the model class.

    :num_components: number of peripherial compartments
    :dose_type: either 'c' (continuous), 'i' (instantaneous), or 'both'
    :self.compartments: list of compartment objects in model
    :self.doses : list of dose objects in model

    """
    def __init__(self, num_compartments = 1, dose_type = 'i', compartments = [], doses = []):
        self.num_compartments = num_compartments
        self.dose_type = dose_type
        self.compartments = compartments
        self.doses = doses

    def __str__(self):
        return 'This model has {self.num_compartments} peripherial compartments with a dose type of {self.dose_type}'

