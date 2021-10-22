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
        self.assertEqual([TestSol.q1, TestSol.q2, TestSol.q0, TestSol.qC, TestSol.t], [None,None,None,None,None])

if __name__ == '__main__':
    unittest.main()