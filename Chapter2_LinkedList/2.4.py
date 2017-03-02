#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 11:43:47 2017
@author: zhenshan
"""
#==============================================================================
# Summry:
#     1. Edge case: tail and switch node is the same one
#     2. Binary problem: only select the ones smaller than k to previous
#==============================================================================
# time: O(n), Space: O(1)
import unittest
import MyLinkedList 

def Partition(head, k):
    if head == None:
        return head
    
    node = head.GetNext()
    headOld = head
    while node:
        if node.GetData() < k:
            tempNode = node.GetNext()
            node.SetNext(head)
            head = node
            node = tempNode
            headOld.SetNext(node)
        else:
            headOld = node
            node = node.GetNext()
    
    result = MyLinkedList.LinkedList(head)
    return result.GetDataList()

class Test(unittest.TestCase):
    testObject = [([1,2,3,4], 3.5, [3,2,1,4]),
                  ([1,2,3,4], 5, [4,3,2,1]),
                  ([1,2,3,4], 0, [1,2,3,4])]
    
    def testParition(self):
        for [testList, k, expected] in self.testObject:
            testLinkedList = MyLinkedList.LinkedList(listData = testList)
            actual = Partition(testLinkedList.head, k)
            self.assertEqual(actual, expected)
    
if __name__ == "__main__":
    unittest.main()