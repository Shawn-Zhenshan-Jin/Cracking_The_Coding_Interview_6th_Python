#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 09:53:51 2017

@author: zhenshan
"""
#==============================================================================
# Summary
# attention to start and end of the loop
#==============================================================================
import unittest

def Compressor(string):
    if len(string) <= 1:
        return string
    
    compressed = ""
    charHead = None
    counter = 1
    for i in range(len(string)):
        if charHead != string[i]:
            compressed  += str(counter)
            charHead = string[i]
            compressed += string[i]
            counter = 1
        else:
            counter += 1
    compressed = compressed[1:]# Remove the fist element
    compressed += str(counter)# Append the last counter
    
    if len(compressed) >= len(string):
        return string
    else:
        return compressed
            
        
class Test(unittest.TestCase):
    testObject = [("",""),
                  ("aabcc","aabcc"),
                  ("aabcccccaaa","a2b1c5a3")]
    
    def testCompressor(self):
        for [string, expected] in self.testObject:
            actual = Compressor(string)
            self.assertEqual(actual, expected)
            
if __name__ == "__main__":
    unittest.main()