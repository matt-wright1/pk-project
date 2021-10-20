"""Create the Dose class.
"""

class Dose:
    """Specifies the dosage applied continually at a constant rate
    and instantaneously at given timestamps.
    
    :c_amount: float, dosage applied continually in ng/hr
    :i_amount: float, dosage applied instantaneously in ng
    :i_times: float, time(s) in hours at which dosage is applied instantaneously
    """
    def __init__(self, c_amount = 0, i_amount = 0, i_times = [0]):
        self.c_amount = c_amount
        self.i_amount = i_amount
        self.i_times = i_times
    
    def __str__(self):
        return "The current doseage is {self.c_amount} ng/hr and {self.i_amount} ng at times {self.i_times}"
