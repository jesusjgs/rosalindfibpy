# This class tests the class RabbitsCalculation.py it has erros and needs more to test too
#


import unittest


from Classes import RabbitsCalculation


class RabbitsCalculationTest(unittest.TestCase):

    def test_should_compute_One_Return_One(self):
        res = RabbitsCalculation.compute(1, 1, 1, 0)
        self.assertEqual(res, 1)
