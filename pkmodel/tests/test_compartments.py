import unittest
import pkmodel

class CompartmentTest(unittest.TestCase):
    """
    Tests the :class:`Compartments` class.
    """
    def test_compartment(self):
        """
        Tests compartment values.
        """
        TestComp = pkmodel.Compartments(1,2)
        self.assertEqual(TestComp._volume, 1)
        self.assertEqual(TestComp._q, 2)
    def test_central(self):
        """
        Tests central compartment values.
        """
        TestComp = pkmodel.Central(1,2,3)
        self.assertEqual(TestComp._volume, 1)
        self.assertEqual(TestComp._q, 2)
        self.assertEqual(TestComp._clearance, 3)

if __name__ == '__main__':
    unittest.main()