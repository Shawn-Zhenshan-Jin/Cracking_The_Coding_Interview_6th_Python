#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 10:14:15 2017

@author: zhenshan
"""
# time: O(n)
# space: O(1)

import unittest

def ZeroOut(matrix):
    if matrix[0] == 0:
        return matrix
    
    ## Create indicator
    # First row and col indicator
    zeroFirstRow = False
    zeroFirstCol = False
    for i in range(len(matrix)):
        if(matrix[i][0] == 0):
            zeroFirstCol = True
    for j in range(len(matrix[0])):
        if(matrix[0][j] == 0):
            zeroFirstRow = True
            
    # Rest rows and cols indicator
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
    
    ## Zero Out 
    for i in range(1, len(matrix)):
        if matrix[i][0] == 0:
            for j in range(1,len(matrix[0])):
                matrix[i][j] = 0
    for j in range(1, len(matrix[0])):
        if matrix[0][j] == 0:
            for i in range(1,len(matrix)):
                matrix[i][j] = 0
    
    if zeroFirstRow:
        for j in range(len(matrix[0])):
            matrix[0][j] = 0 
    if zeroFirstCol:
        for i in range(len(matrix)):
            matrix[i][0] = 0
    
    return matrix

class Test(unittest.TestCase):
    testObject = [
        ([
            [1, 2, 3, 4, 0],
            [6, 0, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 0, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [11, 0, 13, 14, 0],
            [0, 0, 0, 0, 0],
            [21, 0, 23, 24, 0]
        ])
    ]
    def testZeroOut(self):
        for [testMatrix, expected] in self.testObject:
            actual = ZeroOut(testMatrix)
            self.assertEqual(actual, expected)
            
if __name__ == "__main__":
    unittest.main()