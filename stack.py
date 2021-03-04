# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 13:50:32 2021

@author: HSIPL39
"""

class Stack:
    
    def __init__(self):
        self.__list = []
    
    def push(self,x):
        return self.__list.append(x)
        
    def pop(self):
        return self.__list.pop()
    
    def peek(self):
        if self.__list:
            return self.__list[-1]
        else:
            return None
    def is_empty(self):
        if self.__list:
            return False
        return True
    
    def size(self):
        return len(self.__list)
    

if __name__ == "__main__":
    s = Stack()
    
    for i in range(1,5):
        s.push()
    print(s.size())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.size())
    print(s.peek())
    print(s.is_empty())
    