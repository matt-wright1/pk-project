from typing import Type
import unittest
import pkmodel

class ModelTest(unittest.TestCase):
    """
    Tests the :class:`Model` class.
    """
    def test_model(self):
        """
        Tests model default values.
        """
        TestModel = pkmodel.Model()
        self.assertEqual(TestModel, [None,None,None,None,None])

    def test_model_errors(self):
        with self.assertRaises(TypeError):
            TestModel = Model(1,'hi',[],[])

        with self.assertRaises(TypeError):
            TestModel = Model('wrong type','i',[],[])

        with self.assertRaises(ValueError):
            TestModel = Model(-2,'c',[],[])
            
if __name__ == '__main__':
    unittest.main()