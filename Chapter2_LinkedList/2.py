#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 17:51:29 2017

@author: zhenshan
"""
import unittest

class Node():
    def __init__(self, data=None, nextNode=None):
        self.data = data
        self.nextNode = nextNode

    def GetData(self):
        return self.data
    
    def SetData(self, newData):
        self.data = newData

    def GetNext(self):
        return self.nextNode

    def SetNext(self, node):# SetNext by node rather by value
        self.nextNode = node#Node(nextData): not right to create a new object
        
class LinkedList():
    def __init__(self):
        self.head = None
            
    def Add(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            node = self.head
            while node.GetNext() != None:
                node = node.GetNext()
            node.SetNext(Node(data))
            
    def BuildUp(self, dataList):
        for data in dataList:
            self.Add(data)
            
    def GetDataList(self):
        node = self.head
        dataList = []
        while node != None:
            dataList.append(node.GetData())
            node = node.GetNext()
        return dataList
    
    def RemoveDuplicate(self):
        node = self.head
        while node != None:
            preRunner = node
            runner = node.GetNext()
            while runner != None:
                if runner.GetData() == node.GetData():
                    preRunner.SetNext(runner.GetNext())
                else:
                    preRunner = runner
                runner = runner.GetNext()
            node = node.GetNext()
    
    def RemoveLastK(self, k):
        if self.head == None:
            return self.GetDataList()
        
        length = 0
        runner = self.head
        while runner != None:
            length += 1
            runner = runner.GetNext()
        
        if length <= (k + 1):
            if (length - k) == 1:
                self.head = self.head.GetNext()
                return self.GetDataList()
            else:
                return self.GetDataList()
        else:
            # Remove: current/pre start together
            current = self.head
            pre = self.head
            for i in range(length - (k + 1)):
                pre = current
                current = current.GetNext()
            pre.SetNext(current.GetNext())
            return self.GetDataList()
    
    def RemoveMiddle(self, k):
        node = self.head
        counter = 0
        while counter < k and node != None:
            node = node.GetNext()
            counter += 1
        
        node.SetData(node.GetNext().GetData())
        node.SetNext(node.GetNext().GetNext())
        
        return self.GetDataList()
        
    def __str__(self):
        outString = "["
        node = self.head
        while node != None:
            outString += str(node.GetData()) + ","
            node = node.GetNext()
        return outString[:-1] + "]"

class Test(unittest.TestCase):
    testObject = [([1,2,3,2,4],[1,2,3,4]),
                  ([1,2,3,4], [1,2,3,4]),
                  ([], [])]
    testObject1 = [([1,2,3,4,5], 3, [1,3,4,5]),
                   ([1], 0, []),
                   ([1,2],2,[1,2])]
    
    testObject2 = [([1,2,3,4,5], 2, [1,2,4,5])]
    
    def testDuplicateRemove(self):
        for [testDataList, expected] in self.testObject:
            testLList = LinkedList()
            testLList.BuildUp(testDataList)
            testLList.RemoveDuplicate()
            self.assertEqual(testLList.GetDataList(), expected)
    
    def testRemoveLastK(self):
        for [testDataList, k, expected] in self.testObject1:
            testLList = LinkedList()
            testLList.BuildUp(testDataList)
            actual = testLList.RemoveLastK(k)
            self.assertEqual(actual, expected)
    
    def testRemoveMiddle(self):
        for [testDataList, k, expected] in self.testObject2: 
            testLList = LinkedList()
            testLList.BuildUp(testDataList)
            actual = testLList.RemoveMiddle(k)
            self.assertEqual(actual, expected)
            
if __name__ == "__main__":
    unittest.main()
    
