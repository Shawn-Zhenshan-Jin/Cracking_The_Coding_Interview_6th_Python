#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 16:22:27 2017

@author: zhenshan
"""
#==============================================================================
# # Solution for LeetCode: https://leetcode.com/problems/intersection-of-two-linked-lists/
#==============================================================================

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

## Double reverse linkedList
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        else:
            reversedA = self.reverseLinkedList(headA)
            reversedB = self.reverseLinkedList(headB)
            dummyA = reversedA
            dummyB = reversedB
            if reversedA is not reversedB:
                self.reverseLinkedList(dummyA)
                self.reverseLinkedList(dummyB)
                return None
            previousNode = reversedA
            while reversedA and reversedB:
                if reversedA is not reversedB:
                    self.reverseLinkedList(dummyA)
                    self.reverseLinkedList(dummyB)
                    return previousNode
                else:
                    previousNode = reversedA
                    reversedA = reversedA.next
                    reversedB = reversedB.next
            self.reverseLinkedList(dummyA)
            self.reverseLinkedList(dummyB)  
            if not reversedA and not reversedB:
                return previousNode
            return None    
                
            
    def reverseLinkedList(self, head):
        if not head.next:
            return head
        else:
            previousNode = None
            while head:
                copyHeadNext = head.next
                head.next = previousNode
                previousNode = head
                head = copyHeadNext
            return previousNode


## Recursive method: O(N), O(N)        
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA == None or headB == None:
            return None
        else:
            intersectNode, _ = self.IntersectionNodeHelp(headA, headB)
            return intersectNode
        
    def IntersectionNodeHelp(self, headA, headB):
        if headA.next == None and headB.next == None:
            return None, True
        else:
            next1 = headA.next if headA.next != None else headA
            next2 = headB.next if headB.next != None else headB
            
            intersectNode, matchedInd = self.IntersectionNodeHelp(next1, next2)
            
            if matchedInd:
                if headA != headB:
                    return intersectNode, False
                else:
                    return headA, True
            else:
                return intersectNode, False

