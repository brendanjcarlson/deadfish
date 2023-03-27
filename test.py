import unittest
from whiteboard import solution

class WhiteboarTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(solution('iiiisddosoddo'), [14, 196, 194])

    def test_2(self):
        self.assertEqual(solution('iiosiisdo'), [2, 35])

    def test_3(self):
        self.assertEqual(solution('ddsosdddiiddddso'), [4, 121])

    def test_4(self):
        self.assertEqual(solution('asoiouscfcusiofusifa'), [0, 1, 2])

    def test_5(self):
        self.assertEqual(solution('isssoddorio'), [1, -1, 1])

if __name__ == '__main__':
    unittest.main()