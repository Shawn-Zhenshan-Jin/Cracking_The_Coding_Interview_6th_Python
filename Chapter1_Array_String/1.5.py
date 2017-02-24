#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 09:01:23 2017

@author: zhenshan
"""

import unittest

def EditChecker(strCombo):
    # Exctract value from input list
    if len(strCombo[0]) >= len(strCombo[1]):
        stringLong = strCombo[0]
        stringShort = strCombo[1]
    else:
        stringLong = strCombo[1]
        stringShort = strCombo[0]
    
    if len(stringLong) - len(stringShort) >= 2:
        return False
    
    mismatch = 0
    # long & short string with different pointer
    longIdx = 0
    shortIdx = 0
    while shortIdx < len(stringShort) and mismatch <= 1:
        if stringLong[longIdx] != stringShort[shortIdx]:
            if len(stringLong) > len(stringShort):
                # insert/remove
                longIdx += 1
            else:
                # replace
                longIdx += 1
                shortIdx += 1
            mismatch += 1
        else:
            longIdx += 1
            shortIdx += 1
    
    # insert: end of string
    if longIdx + 1 < len(stringLong):
        mismatch += 1
        
    if mismatch <= 1:
         return True
    else:
         return False
     
class Test(unittest.TestCase):
    testObject = [
        (('pale', 'ple'), True),
        (('pales', 'pale'), True),
        (('pale', 'bale'), True),
        (('paleabc', 'pleabc'), True),
        (('pale', 'ble'), False),
        (('a', 'b'), True),
        (('', 'd'), True),
        (('d', 'de'), True),
        (('pale', 'pale'), True),
        (('pale', 'ple'), True),
        (('ple', 'pale'), True),
        (('pale', 'bale'), True),
        (('pale', 'bake'), False),
        (('pale', 'pse'), False),
        (('ples', 'pales'), True),
        (('pale', 'pas'), False),
        (('pas', 'pale'), False),
        (('pale', 'pkle'), True),
        (('pkle', 'pable'), False),
        (('pal', 'palks'), False),
        (('palks', 'pal'), False)
    ]
    
    def testEdit(self):
        for [strCombo, expected] in self.testObject:
            actual = EditChecker(strCombo)
            self.assertEqual(actual, expected)
            
if __name__ == "__main__":
    unittest.main()