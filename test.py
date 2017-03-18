#!/bin/env python3

import unittest
from permutate import permutate

class TestMutationMethods (unittest.TestCase):
    def test_single (self):
        list = [['human']]
        result = permutate(list, [''])
        expected = ['human']
        self.assertEqual(result, expected)
    def test_start_single_end_single (self):
        list = [['hum'], ['an']]
        result = permutate(list, [''])
        expected = ['human']
        self.assertEqual(result, expected)
    def test_start_single_end_multiple (self):
        list = [['human'], ['', ' being']]
        result = permutate(list, [''])
        expected = ['human', 'human being']
        self.assertEqual(result, expected)
    def test_start_multiple_end_single(self):
        list = [['trans', 'semi'], ['human']]
        result = permutate(list, [''])
        expected = ['transhuman', 'semihuman']
        self.assertEqual(result, expected)
    def test_start_multiple_end_multiple (self):
        list = [['trans', 'semi'], ['human', 'machine']]
        result = permutate(list, [''])
        expected = ['transhuman', 'transmachine', 'semihuman', 'semimachine']
        self.assertEqual(result, expected)
    def test_complex(self):
        list = [['correct', 'wrong'], ['battery'], ['', ' '], ['staple', 'pencil']]
        result = permutate(list, [''])
        expected = [
            'correctbatterystaple',
            'correctbatterypencil',
            'correctbattery staple',
            'correctbattery pencil',
            'wrongbatterystaple',
            'wrongbatterypencil',
            'wrongbattery staple',
            'wrongbattery pencil'
        ]
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
