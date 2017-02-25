#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 10:14:04 2017

@author: zhenshan
"""
# time: O(N*N), size of the matrix
# space: O(N)
# N*N matrix

import unittest

def MatrixRotation(matrix):
    start = 0
    end = len(matrix) - 1

    while end > start:
        tempStorage = [None for i in range(end - start)]
        direction = [start, end, end, start]
        leftStartC = [start, start, end, end]
        rightStartC = [end, end, start, start]
        
        directionP = [end, end, start, start]
        leftStartP = [start, end, end, start]
        rightStartP = [end, start, start, end]
        
        for i in range(4):
            tempIdx = 0
            for jc in range(leftStartC[i], rightStartC[i]):
                if i % 2:
                    left = direction[i]
                    right = jc
                else:
                    left = jc
                    right = direction[i]
                tempStorage[tempIdx] = matrix[left][right]
                tempIdx += 1
                
            tempIdx = 0
            for jp in range(leftStartP[i], rightStartP[i]):
                if i % 2:
                    left = jp
                    right = directionP[i]
                else:
                    left = directionP[i]
                    right = jp
                matrix[left][right] = tempStorage[tempIdx]
                tempIdx += 1
                print(matrix)
                
        start += 1
        end -= 1
    
    return matrix

class Test(unittest.TestCase):
    testObject = [
        ([
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [21, 16, 11, 6, 1],
            [22, 17, 12, 7, 2],
            [23, 18, 13, 8, 3],
            [24, 19, 14, 9, 4],
            [25, 20, 15, 10, 5]
        ])
    ]
    def testMatrixRotation(self):
        for [testMatrix, expected] in self.testObject:
            actual = MatrixRotation(testMatrix)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
