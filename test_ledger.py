import unittest
from ledger import apply
class T(unittest.TestCase):
    def test_final_only(self):
        self.assertEqual(apply([{"amount": 1}, {"amount": 2}]), 3)
if __name__ == "__main__":
    unittest.main()
