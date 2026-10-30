"""Basic verification using unittest; run python labs/semester-01/week-01/test_numerical_derivative.py."""
import unittest
from numerical_derivative import analytic_derivative, central_difference


class NumericalDerivativeTests(unittest.TestCase):
    def test_derivative_at_two(self):
        self.assertEqual(analytic_derivative(2.0), -2.0)

    def test_central_difference_approximation(self):
        self.assertAlmostEqual(central_difference(2.0, 0.001), -2.0, places=4)


if __name__ == "__main__":
    unittest.main()
