#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 12:32:16 2017

@author: zhenshan
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 11:24:14 2017

@author: zhenshan
"""
import unittest
from collections import Counter # High performance python collections

# Sorting method
def Permutation(string1, string2):
    if len(string1) != len(string2):
        return False
    
    sortedString1 = sorted(string1)
    sortedString2 = sorted(string2)
    
    for i in range(len(sortedString1)):
        if sortedString1[i] != sortedString2[i]:
            return False
    return True

# Collection method
def PermutationCounter(string1, string2):
    if len(string1) != len(string2):
        return False
    
    counter = Counter()
    for s in string1:
        counter[s] += 1
    for s in string2:
        if counter[s] == 0:
            return False
        counter[s] -= 1
    return True

class Test(unittest.TestCase):
    testString1 = ["asdf)g","wert","fds f"]
    testString2 = ["sfgad)","trew","fd sf"]
    
    def testPermutation(self):
        length = len(self.testString1)
        
        for i in range(length):
            result = Permutation(self.testString1[i], self.testString2[i])
            self.assertTrue(result)
    
    def testPermutationCounter(self):
        length = len(self.testString1)
        
        for i in range(length):
            result = PermutationCounter(self.testString1[i], self.testString2[i])
            self.assertTrue(result)
            
if __name__ == '__main__':
    unittest.main()