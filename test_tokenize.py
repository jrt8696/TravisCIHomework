import unittest
import shunting_yard as sy


class TokenizeTest(unittest.TestCase):
    def test_single_operator(self):
        tokens = list(sy.tokenize('1+2'))
        self.assertListEqual(tokens, ['1', '+', '2'])
