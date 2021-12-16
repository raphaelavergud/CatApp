#!/usr/bin/env python3

import unittest
import kitty
from kitty import uncomfy_checker
import mock

class TestProgram(unittest.TestCase):
    def test_comfy(self):
        kitty.uncomfy_checker = mock.Mock(return_value='comfortable')
        self.assertIn(uncomfy_checker(), 'comfortable')


if __name__ == '__main__':
    unittest.main()