# porqua_test.py
import unittest

def calculate_portfolio_return(weights, returns):
    return sum(w * r for w, r in zip(weights, returns))

class TestPortfolioReturn(unittest.TestCase):
    def test_positive_returns(self):
        weights = [0.5, 0.5]
        returns = [0.1, 0.2]
        self.assertEqual(calculate_portfolio_return(weights, returns), 0.15)

    def test_negative_returns(self):
        weights = [0.3, 0.7]
        returns = [-0.1, 0.05]
        self.assertEqual(calculate_portfolio_return(weights, returns), 0.005)

if __name__ == '__main__':
    unittest.main()
