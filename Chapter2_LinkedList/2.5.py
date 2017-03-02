#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 13:39:07 2017

@author: zhenshan
"""
#==============================================================================
# Summary: 
#   Start current node from head and pre node as None
#==============================================================================
import unittest
import MyLinkedList

def AddTwo(head1, head2):
    head = MyLinkedList.Node(0)
    dummyHead = head
    
    runner1 = head1
    runner2 = head2
    left = 0
    while runner1 and runner2:
        value = runner1.GetData() + runner2.GetData() + left
        head.SetNext(MyLinkedList.Node(value % 10))
        head = head.GetNext()
        left = value // 10
        runner1 = runner1.GetNext()
        runner2 = runner2.GetNext()
    
    while runner1:
        value = runner1.GetData() + left
        head.SetNext(MyLinkedList.Node(value % 10))
        head = head.GetNext()
        left = value // 10
        runner1 = runner1.GetNext()
        
    while runner2:
        value = runner2.GetData() + left
        head.SetNext(MyLinkedList.Node(value % 10))
        head = head.GetNext()
        left = value // 10
        runner2 = runner2.GetNext()
        
    if left != 0:
        head.SetNext(MyLinkedList.Node(left))
    
    return MyLinkedList.LinkedList(dummyHead.GetNext())

def Reverse(head):
    '''Two nodes reverse a linkedlist'''
    if head == None or head.GetNext() == None:
        return MyLinkedList.LinkedList(head)
    
    pre = None
    current = head
    while current != None:
        temp = current.GetNext()
        current.SetNext(pre)
        pre = current   
        current = temp
    
    return MyLinkedList.LinkedList(pre)
    

class Test(unittest.TestCase):
    testObject = [(([7,1,6],[5,9,2]), [2,1,9]),
                  (([1,2,3], [3,4,7,9]), [4, 6, 0, 0, 1]),
                  (([], []),[])]
    
    testObject1 = [([1,2,3], [3,2,1]),
                   ([1,2], [2,1]),
                   ([1], [1])]
    
    def testAddTwo(self):
        for [testCombo, expected] in self.testObject:
            linkedList1 = MyLinkedList.LinkedList()
            linkedList2 = MyLinkedList.LinkedList()
            linkedList1.BuildUp(testCombo[0])
            linkedList2.BuildUp(testCombo[1])  
            actual = AddTwo(linkedList1.head, linkedList2.head).GetDataList()
            self.assertEqual(actual, expected)
    
    def testReverse(self):
        """follow up: first reverse the list, them add two number together"""
        for [testList, expected] in self.testObject1:
            linkedList = MyLinkedList.LinkedList(listData = testList)
            actual = Reverse(linkedList.head).GetDataList()
            self.assertEqual(actual, expected)

            
if __name__ == "__main__":
    unittest.main()

    