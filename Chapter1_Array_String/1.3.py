#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 12:49:51 2017

@author: zhenshan
"""

#==============================================================================
# Summary
# By reversing storaging process, avoid over-writing
#==============================================================================
import unittest

def SpaceReplacer(strCombo):
    string = strCombo[0]
    length = strCombo[1]
    stringTrue = strCombo[2]
    
    lengthCounter = len(string)
    for i in reversed(range(length)):
        if string[i] == " ":
            # Replace space
            string[(lengthCounter - 3): lengthCounter] = "20%"
            lengthCounter -= 3
        else:
            # Move characters
            string[lengthCounter - 1] = string[i]
            lengthCounter -= 1
    
    print(string, "\n", stringTrue)
    if string == stringTrue:
        return True
    else:
        return False

class Test(unittest.TestCase):
    testString = [(list("Mr John Smith     "),13, 
                   list("Mr20%John20%Smith")),
                  (list(" ado haha    "), 9, 
                   list("20%ado20%haha"))]
    
    def testReplacer(self):
        for s in self.testString:
            result = SpaceReplacer(s)
            self.assertTrue(result, "Don't match with each other")
            
if __name__ == "__main__":
    unittest.main()
    
    
        for s in testString:
            result = SpaceReplacer(s)
            print(result)
            