import unittest

from pkmodel import Dose

class DoseTest(unittest.TestCase):
    """
    Tests the :class:`Dose` class.
    """
    # def test_dose_defaults(self):
    #     """
    #     Tests dose class has correct default values of 0.
    #     """
    #     TestDose = Dose()
    #     self.assertEqual([TestDose.c_amount, TestDose.i_amount, TestDose.i_times], [0, 0, [0]])

    # def test_dose_positives(self):
    #     """
    #     Tests dose class works with positive integers.
    #     """
    #     TestDose = Dose(7,10,5)
    #     self.assertEqual([TestDose.c_amount, TestDose.i_amount, TestDose.i_times], [7, 10, [5]])

    def test_dose_negatives(self):
        """
        Tests dose class raises errors with negative integers.
        """
        with self.assertRaises(ValueError):
            TestDose = Dose(-1, 0, [0])
        
        with self.assertRaises(ValueError):
            TestDose = Dose(0, 0, -5)
        
        with self.assertRaises(ValueError):
            TestDose = Dose(0, 0, [-5, 0 ,1])


    # def test_dose_add_time(self):
    #     """
    #     Tests dose class correctly adds times to list.
    #     """
    #     TestDose = Dose(1, 1, 0)
    #     TestDose.add_i_time(5)
    #     self.assertEqual([TestDose.c_amount, TestDose.i_amount, TestDose.i_times], [1, 1, [0, 5]])

if __name__ == '__main__':
    unittest.main()