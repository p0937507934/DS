# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 14:17:20 2021

@author: HSIPL39
"""


class Node:
    
    
    def __init__(self,val):
        self.val = val
        self.next = None
    

class SingleLinkedList:
    
    def __init__(self,head=None):
        self.head = head
    
    def is_empty(self):
        return self.head == None
    
    def append(self,val):
        node = Node(val)
        
        if self.is_empty():
            self.head = node
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = node
    
    def travel(self):
        cur = self.head
        while cur:
            print(cur.val)
            cur =  cur.next
            
    
    def length(self):
        count = 0
        cur = self.head
        while cur:
            count = count + 1
            cur = cur.next
        print(count)
        return count 
    
    def insert(self,pos,val):
      
            
    def add(self,val):    
        node = Node(val)
        node.next = self.head
        self.head = node
        
            
            
        
    
s = SingleLinkedList()
s.append(1)
s.append(2)
s.append(3)
s.append(4)
s.append(5)
s.travel()
s.length()
                
            
            
            
            
            
            
        
    