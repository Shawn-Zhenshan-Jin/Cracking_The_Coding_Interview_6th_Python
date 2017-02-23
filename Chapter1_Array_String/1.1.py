#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 11:24:14 2017

@author: zhenshan
"""
import unittest

def UniqueChar(string):
    # Assuming character set is ASCII (128 characters)
    if len(string) > 128:
        return False
    
    stringHash = {}
    value = 0
    for s in string:
        if s in stringHash:
            return False
        else:
            stringHash[s] = value
            value += 1
    return True

class UniqueTest(unittest.TestCase):
    testTrue = [('abcd'), ('s4fad'), (' ')]
    testFalse = [('23ds2'), ('hb 627jh=j ()')]
        
    def testUnique(self):
        print("Inside test")
        for testStr in self.testTrue:
            self.assertTrue(UniqueChar(testStr))
        for testStr in self.testFalse:
            self.assertFalse(UniqueChar(testStr))
    
if __name__ == '__main__':
    unittest.main()