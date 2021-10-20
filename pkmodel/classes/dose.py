"""A class that stores the doseage amount and type
"""

class Dose:
    def __init__(self, c_amount, i_amount, i_times):
        self.c_amount = c_amount
        self.i_amount = i_amount
        self.i_times = i_times
    
    def __str__(self):
        return "The current doseage is {self.c_amount} ng/hr and {self.i_amount} ng at times {self.i_times}"
