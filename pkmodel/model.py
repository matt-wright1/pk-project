'''Create the model class'''
class Model:
    """Creates the model class.

    :num_components: number of peripherial compartments
    :dose_type: either 'c' (continuous), 'i' (instantaneous), or 'both'
    :self.compartments: list of compartment objects in model
    :self.doses : list of dose objects in model

    """
    def __init__(self, num_compartments = 1, dose_type = 'i', compartments = [], doses = []):
        self.num_compartments = self._is_data_valid(num_compartments)
        self.dose_type = self._is_dose_type_valid(dose_type)
        self.compartments = compartments
        self.doses = doses

    def _is_data_valid(self, value):
        if value < 0:
            raise ValueError("Entry cannot be negative")
        elif type(value) != (int or float):
            raise TypeError('Number of compartments must be a number!')
        return value

    def _is_dose_type_valid(self, value):
        if value == 'i' or value == 'c' or value == 'both':
            return value
        else:
            raise TypeError('The dose type must be i, c or both')

    def __str__(self):
        return 'This model has {self.num_compartments} peripherial compartments with a dose type of {self.dose_type}'

