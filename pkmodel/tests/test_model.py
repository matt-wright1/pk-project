from typing import Type
import unittest
from pkmodel import *

class ModelTest(unittest.TestCase):
    """
    Tests the :class:`Model` class.
    """
    def test_model(self):
        """
        Tests model default values.
        """
        TestModel = Model()
        self.assertEqual([TestModel.num_compartments, TestModel.dose_type, TestModel.compartments, TestModel.dose], [1,'i',{},[]])

    def test_model_errors(self):
        with self.assertRaises(TypeError):
            TestModel = Model(1, 'wrong string',[], [])

        with self.assertRaises(TypeError):
            TestModel = Model('string', 'i',[], [])

        with self.assertRaises(ValueError):
            TestModel = Model(-2, 'c', [], [])
    
    def test_model_string(self):
        TestModel = Model()
        self.assertEqual(TestModel.__str__(),'This model has 1 peripheral compartment(s) with a dose type of i')

            
if __name__ == '__main__':
    unittest.main()