# This class tests the class RabbitsCalculation.py it has erros and needs more to test too
#


import unittest
import mockito

from unittest.test.test_case import Test

from mockito import mock, when, verify

from Classes import RabbitsCalculation


class RabbitsCalculationTest(unittest.TestCase):

    def test_should_compute_One_Return_One(self):
        res = RabbitsCalculation.compute(1, 1, 1, 0)
        self.assertEqual(res, 1)
