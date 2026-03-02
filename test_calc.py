import unittest
from calc import add

class TestCalculator(unittest.TestCase):
    def test_add(self):
        # 1 + 2가 3인지 확인하는 테스트 케이스
        self.assertEqual(add(1, 2), 3)

if __name__ == "__main__":
    unittest.main()
