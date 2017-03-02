#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 11:43:02 2017

@author: zhenshan
"""
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
    def __init__(self, node = None, listData = None):
        if node == None and listData == None:
            self.head = None
        elif node == None and listData != None:
            self.head = None
            self.BuildUp(listData)
        elif node != None and listData == None:
            self.head = node
        else:
            print("Ambiguous parameter combination, only first node are initalized")
            self.head = node
            
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

    def __str__(self):
        outString = "["
        node = self.head
        while node != None:
            outString += str(node.GetData()) + ","
            node = node.GetNext()
        return outString[:-1] + "]"