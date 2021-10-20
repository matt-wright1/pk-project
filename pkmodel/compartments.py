#
# Compartments class
#

class Compartment:
    '''Pharmokinetic compartments, used to model the body.

    Parameters
    ----------
    v: number
        the volume of a compartment, units mL
    q: number
        inital quantity of drug, units ng
    '''
    def __init__(self, v, q):
        self.v = v
        self.q = q
    
    @property
    def _volume(self):
        return self.v
    
    @property
    def _q(self):
        return self.q
class Central(Compartment):
    '''Central compartment to which the drug is typically administered and from which the drug is removed.

    Parameters
    ----------
    CL: number
        the clearance/elimination rate from the central compartment, units mL/h
    '''
    def __init__(self, q, v, CL):
        super().__init__(q,v)
        self.CL = CL
    
    @property
    def _clearance(self):
        return self.CL
class Peripheral(Compartment):
    '''Periheral compartments to which the drug can be distributed to/from the central compartment.

    Parameters
    ----------
    Q: number
        the transition rate between central compartment and peripheral component, units mL/h
    '''
    def __init__(self, q, v, Q):
        super().__init__(q,v)
        self.Q = Q
    
    @property
    def _flux(self):
        return self.Q
class Dosing(Compartment):
    '''Additional compartment from which the drug is absorbed to the central compartment.
    Used for subcutaneous dosing.

    Parameters
    ----------
    ka: number
        the absorption quantity for subcutaneous dosing, units mL
    '''
    def __init__(self,q,v,ka):
        super().__init__(q,v)
        self.ka = ka
    
    @property
    def _ka(self):
        return self.ka
