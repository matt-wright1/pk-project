"""Create the solution class"""


class Solution:
    """Creates the solution class.

    Default values are empty.

    :param q1: array of drug quantity in compartment 1
    :param q2: array of drug quantity in compartment 2
    :param q0: array of drug quantity in drug compartmen
    :param qC: array of drug quantity in central compartment"""

    def __init__(self, q1=None, q2=None, q0=None, qC=None):
        self.q1 = q1
        self.q2 = q2
        self.q0 = q0
        self.qC = qC
