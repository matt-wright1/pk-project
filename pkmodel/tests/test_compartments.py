import unittest
import pkmodel
from pkmodel import *

class CompartmentTest(unittest.TestCase):
    """
    Tests the :class:`Compartments` class.
    """
    def test_compartment_defaults(self):
        """
        Tests compartment class has correct default values of 0.
        """
        TestComp = Compartments()
        self.assertEqual([TestComp.v, TestComp.q], [1, 0])

    def test_compartment_positives(self):
        """
        Tests compartment values.
        """
        TestComp = Compartments(1,2)
        self.assertEqual([TestComp.v,TestComp.q], [1, 2])

    def test_central_defaults(self):
        """
        Tests central class has correct default values of 0.
        """
        TestCent = Central()
        self.assertEqual([TestCent.v, TestCent.q, TestCent.CL], [1, 0, 0])

    def test_central_postives(self):
        """
        Tests central compartment values.
        """
        TestCent = Central(1,2,3)
        self.assertEqual([TestCent.v, TestCent.q, TestCent.CL], [1 ,2, 3])

    def test_peripheral_defaults(self):
        """
        Tests peripheral class has correct default values of 0.
        """
        TestPeri = Peripheral()
        self.assertEqual([TestPeri.v, TestPeri.q, TestPeri.Q], [1, 0, 0])

    def test_peripheral_postives(self):
        """
        Tests central compartment values.
        """
        TestPeri = Peripheral(1,2,3)
        self.assertEqual([TestPeri.v, TestPeri.q, TestPeri.Q], [1, 2, 3])

    def test_dosing_defaults(self):
        """
        Tests dosing class has correct default values of 0.
        """
        TestDosn = Dosing()
        self.assertEqual([TestDosn.v, TestDosn.q, TestDosn.ka], [1, 0, 0])

    def test_dosing_postives(self):
        """
        Tests dosing compartment values.
        """
        TestDosn = Dosing(1,2,3)
        self.assertEqual([TestDosn.v, TestDosn.q, TestDosn.ka], [1, 2, 3])

if __name__ == '__main__':
    unittest.main()
