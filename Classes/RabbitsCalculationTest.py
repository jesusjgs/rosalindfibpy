# This class tests the class RabbitsCalculation.py
#


import unittest
import mockito

from unittest.test.test_case import Test

from mockito import mock, when, verify

from Classes import RabbitsCalculation


class RabbitsCalculationTest(unittest.TestCase):

    def test_should_compute_One_Return_One(self):
        # Create mock object
        rabbits: RabbitsCalculation = mock()
        # Stubing
        when(rabbits).compute(1, 1, 1, 0).thenReturn(True)
        # Execute
        compute_order: RabbitsCalculation = RabbitsCalculation(0)
        res: int = compute_order.compute(1, 1, 1, 0)
        # Verify
        verify(res == 1)
