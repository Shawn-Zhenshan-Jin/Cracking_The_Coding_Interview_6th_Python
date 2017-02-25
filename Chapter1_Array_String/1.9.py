#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 12:33:18 2017

@author: zhenshan
"""
#==============================================================================
# # Idea: 
#   rotated: BA, concatenate two: BABA
#   original: AB
#==============================================================================
import unittest

def is_substring(string, sub):
    return string.find(sub) != -1

def StringRotation(rotated, original):
    return is_substring(rotated + rotated, original)

class Test(unittest.TestCase):
    testObject = [
            ("","", True),
            ("melonwater", "watermelon", True),
            ("hey", "hi", False)]
    def testStringRotation(self):
        for [rotated, original, expected] in self.testObject:
            actual = StringRotation(rotated, original)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()