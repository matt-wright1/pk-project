'''
import unittest
from pkmodel import model, number_of_models, model_1_inputs, create_model, model_2_inputs


class CreateModelTest(unittest.TestCase):
    """
    Tests the function createmodel.
    """

    #def test_dosing_m1(self, model_1, model_1_inputs):
    #"""Tests the right dosing values are submitted to the class"""

    #def test_central_compartments_m1(self, model_1, model_1_inputs):
    #"""Tests the right comparment information is submitted to the class"""

    # run the create model function
    def test_createmodel(self, number_of_models = number_of_models, model_1_inputs = model_1_inputs, model_2_inputs = model_2_inputs):
        #put the model data into classes and create a solution class with a time array of the solution
        if number_of_models == 2:
            model1, model2, solution1, solution2 = create_model(2, model_1_inputs, model_2_inputs)      
        else:
            model1, solution1 = create_model(1, model_1_inputs)

        self.assertEqual(model1.time, model_1_inputs["m1_time"])
        self.assertEqual(model1.timestep, model_1_inputs["m1_timestep"])
        self.assertEqual(['central' in model1.compartments,'dose' in model1.compartments, 'peripheral_1' in model1.compartments, \
            'peripheral_2' in model1.compartments], [True,True,True,True])

        #self.assertEqual(model_1.Central.v, model_1_inputs["m1_volume_c"])
        #self.assertEqual(model_1.Central.q, model_1_inputs["m1_q_c_initial"])
        #self.assertEqual(model_1.Central.CL, model_1_inputs["m1_CL"])


if __name__ == '__main__':
    unittest.main()
'''