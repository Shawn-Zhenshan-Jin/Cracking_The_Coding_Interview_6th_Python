#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 11:43:47 2017
@author: zhenshan
"""

import unittest
from MyLinkedList import LinkedList

def Partition(linkedList, k):
    head = linkedList.head
    if head == None:
        return head
    
    tail = head
    length = 0
    while tail.GetNext() != None:
        tail = tail.GetNext()
        length += 1
    
    counter = 0
    node = head.GetNext() #Start from second node
    headOld = head
    while counter < length:
        if node.GetData() < k:
            tempNode = node.GetNext()
            node.SetNext(head)
            head = node
            node = tempNode
        else:
            tempNode = node.GetNext()
            tail.SetNext(node)
            tail = node
            node = tempNode
        headOld.SetNext(node)# Remove the head link
        counter += 1
    tail.SetNext(None)
    
    return linkedList.GetDataList()

class Test(unittest.TestCase):
    testObject = [([1,2,3,4], 3.5, [3,2,1,4]),
                  ([1,2], 3, [2,1])]
    
    def testParition(self):
        for [testList, k, expected] in self.testObject:
            testLinkedList = LinkedList()
            testLinkedList.BuildUp(testList)
            actual = Partition(testLinkedList, k)
            self.assertEqual(actual, expected)
    
if __name__ == "__main__":
    unittest.main()