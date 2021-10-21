import unittest
import pkmodel

class SolutionTest(unittest.TestCase):
    """
    Tests the :class:`Solution` class.
    """
    def test_solution(self):
        """
        Tests solution default values.
        """
        TestSol = pkmodel.Solution()
        self.assertEqual(TestSol, [None,None,None,None,None])

if __name__ == '__main__':
    unittest.main()