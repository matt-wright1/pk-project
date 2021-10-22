import unittest
import pkmodel
from pkmodel import number_of_models, model_1_inputs, create_model


class CreateModelTest(unittest.TestCase):
    """
    Tests the function createmodel.
    """

    #def test_dosing_m1(self, model_1, model_1_inputs):
    #"""Tests the right dosing values are submitted to the class"""

    #def test_central_compartments_m1(self, model_1, model_1_inputs):
    #"""Tests the right comparment information is submitted to the class"""

    # run the create model function
    def build_model(self, number_of_models, model_1_inputs, model_2_inputs=None):
        #put the model data into classes and create a solution class with a time array of the solution
        if number_of_models == 2:
            model1, model2, solution1, solution2 = create_model(2, model_1_inputs, model_2_inputs)      
        else:
            model1, solution1 = create_model(1, model_1_inputs)

        self.assertEqual(model_1.c_amount, model_1_inputs["m1_continous_dose_amount"])
        self.assertEqual(model_1.i_amount, model_1_inputs["m1_instantaneous_dose_amount"])
        self.assertEqual(model_1.i_times, model_1_inputs["m1_dose_times"])

        self.assertEqual(model_1.Central.v, model_1_inputs["m1_volume_c"])
        self.assertEqual(model_1.Central.q, model_1_inputs["m1_q_c_initial"])
        self.assertEqual(model_1.Central.CL, model_1_inputs["m1_CL"])


if __name__ == '__main__':
    unittest.main()