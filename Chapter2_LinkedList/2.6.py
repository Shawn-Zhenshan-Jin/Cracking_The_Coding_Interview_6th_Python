#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 12:08:23 2017

@author: zhenshan
"""
#space:O(N), time:O(N)
import unittest
import MyLinkedList

def PalindromeChecker(head):
    wordList = []
    while head is not None:
        wordList.append(head.GetData())
        head = head.GetNext()
    
    l = len(wordList)
    
    idx = 0
    while idx < l//2:
        if wordList[idx] != wordList[l - idx - 1]:
            return False
        idx += 1
    return True

def PalindromeRunner(head):
    if head != None or head.GetNext() != None:
        return True
    
    slow = fast = head
    half = []
    while fast.GetNext() != None and fast.GetNext() != None:
        half.append(slow.GetData())
        slow = slow.GetNext()
        fast = fast.GetNext().GetNext()
        
    if fast != None:
        slow = slow.GetNext()
    
    while slow != None:
        if slow.GetData() != half.pop():
            return False
        slow = slow.GetNext()
    
    return True

class Test(unittest.TestCase):
    testObject = [([1,2,3,3,2,1], True),
                  ([1,2,3,2,1], True),
                  ([], True),
                  ([1,2,3], False)]
    
    def testPalindromeChecker(self):
        for [testList, expected] in self.testObject:
            testLinkedList = MyLinkedList.LinkedList(listData = testList)
            actual = PalindromeChecker(testLinkedList.head)
            self.assertEqual(actual, expected)
            
if __name__ == "__main__":
    unittest.main()