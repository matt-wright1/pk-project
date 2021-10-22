class Dose:
    """Specifies the dosage applied continually at a constant rate
    and instantaneously at given timestamps.
    
    :c_amount: float, dosage applied continually in ng/hr
    :i_amount: float, dosage applied instantaneously in ng
    :i_times: float, time(s) in hours at which dosage is applied instantaneously
    """
    def __init__(self, c_amount = 0, i_amount = 0, i_times = [0]):
        self.c_amount = self._is_data_valid(c_amount)
        self.i_amount = self._is_data_valid(i_amount)
        if type(i_times) == list:
            self.i_times = self._are_times_valid(i_times)
        else:
            self.i_times = [self._is_data_valid(i_times)]

    def _is_data_valid(self, value):
        if value < 0:
            raise ValueError("Entry cannot be negative")
        
        return value

    def _are_times_valid(self, list):
        for i in range(len(list)):
            if list[i] < 0:
                raise ValueError("Entry cannot be negative")
        
        return list
    
    def __str__(self):
        return f"The current doseage is {self.c_amount} ng/hr and {self.i_amount} ng at times {self.i_times}"

    def add_i_time(self, time):
        self.i_times.append(time)