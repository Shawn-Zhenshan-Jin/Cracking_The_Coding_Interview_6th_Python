#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 20:54:20 2017

@author: zhenshan
"""
#==============================================================================
# # Circular detection
#==============================================================================
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        try:
            slow = head.next
            fast = head.next.next
            while fast != None and slow != fast:
                slow = slow.next
                fast = fast.next.next
            if slow == fast:
                return True
            else:
                return False
        except:
            return False
        
# Circular detection + 