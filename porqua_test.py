# porqua_test.py
import unittest

# Simulate a PorQua function to calculate portfolio return based on weights and asset returns
def calculate_portfolio_return(weights, returns):
    """
    Calculate the total return of a portfolio given weights and asset returns.
    Args:
        weights (list): List of portfolio weights (e.g., [0.5, 0.5]).
        returns (list): List of asset returns (e.g., [0.1, 0.2]).
    Returns:
        float: Total portfolio return.
    """
    if len(weights) != len(returns):
        raise ValueError("Weights and returns must have the same length")
    return sum(w * r for w, r in zip(weights, returns))

class TestPortfolioReturn(unittest.TestCase):
    def test_positive_returns(self):
        """Test portfolio return with positive asset returns."""
        weights = [0.5, 0.5]
        returns = [0.1, 0.2]
        self.assertEqual(calculate_portfolio_return(weights, returns), 0.15)

    def test_negative_returns(self):
        """Test portfolio return with mixed positive and negative returns."""
        weights = [0.3, 0.7]
        returns = [-0.1, 0.05]
        self.assertEqual(calculate_portfolio_return(weights, returns), 0.005)

    def test_invalid_input(self):
        """Test error handling for mismatched weights and returns."""
        weights = [0.5, 0.5]
        returns = [0.1]  # Length mismatch
        with self.assertRaises(ValueError):
            calculate_portfolio_return(weights, returns)

    def test_zero_weights(self):
        """Test portfolio return when all weights are zero."""
        weights = [0.0, 0.0]
        returns = [0.1, 0.2]
        self.assertEqual(calculate_portfolio_return(weights, returns), 0.0)

if __name__ == '__main__':
    unittest.main()
