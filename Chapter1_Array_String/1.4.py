#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 14:10:57 2017

@author: zhenshan
"""
# Time: O(n)
# Space: O(n)

import unittest
from collections import Counter # High performance python collections

def PalindromePermutationChecker(string):
    # Remove space from string
    string = "".join([str.lower(_) for _ in list(string) if _ != " "])
    
    # Frequency of each character
    counter = Counter(string)
    
    # Counting the number of character with odd frequency
    totalOddPair = 0
    for i in "".join(set(string)):# return string with unique value
        if counter[i] % 2 != 0:
            totalOddPair += 1
    
    # odd pair and string length should be both odd or even
    if totalOddPair == 1 and len(string) % 2 == 1:
        return True
    elif totalOddPair == 0 and len(string) % 2  == 0:
        return True
    else:
        return False

class Test(unittest.TestCase):
    testString = [
        ('Tact Coa', True),
        ('jhsabckuj ahjsbckj', True),
        ('Able was I ere I saw Elba', True),
        ('So patient a nurse to nurse a patient so', False),
        ('Random Words', False),
        ('Not a Palindrome', False),
        ('no x in nixon', True),
        ('azAZ', True)]
    
    def testPPChecker(self):
        for [testStr, expected] in self.testString:
            actual = PalindromePermutationChecker(testStr)
            self.assertEqual(actual, expected)
            
if __name__ == "__main__":
    unittest.main()
