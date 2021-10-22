#
# Compartments class
#

class Compartments:
    '''Pharmokinetic compartments, used to model the body.

    Parameters
    ----------
    v: number
        the volume of a compartment, units mL
    q: number
        inital quantity of drug, units ng
    '''
    def __init__(self, v = 1, q = 0):
        self.v = self._is_volume_valid(v)
        self.q = self._is_data_negative(q)

    def _is_data_negative(self, value):
        if value < 0:
            raise ValueError("Entry cannot be negative")
    
        return value
    def _is_volume_valid(self, value):
        if value <= 0:
            raise ValueError("Volume must be greater than 0")
        
        return value
class Central(Compartments):
    '''Central compartment to which the drug is typically administered and from which the drug is removed.

    Parameters
    ----------
    CL: number
        the clearance/elimination rate from the central compartment, units mL/h
    '''
    def __init__(self, v = 1, q = 0, CL = 0):
        super().__init__(v, q)
        self.CL = CL
    
class Peripheral(Compartments):
    '''Periheral compartments to which the drug can be distributed to/from the central compartment.

    Parameters
    ----------
    Q: number
        the transition rate between central compartment and peripheral component, units mL/h
    '''
    def __init__(self, v = 1, q = 0, Q = 0):
        super().__init__(v, q)
        self.Q = Q
    
class Dosing(Compartments):
    '''Additional compartment from which the drug is absorbed to the central compartment.
    Used for subcutaneous dosing.

    Parameters
    ----------
    ka: number
        the absorption quantity for subcutaneous dosing, units mL
    '''
    def __init__(self, v = 1, q = 0, ka = 0):
        super().__init__(v, q)
        self.ka = ka
    
