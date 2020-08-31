'''
Created on Aug 28, 2020

@author: kislam
'''

class DoublyLlist(object):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
       '''
        self.head = None
        self.tail = None
       
    def add_node(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.prev = self.head
            self.head.next = node
            self.head = node
            
        
        
    def remove_node(self, node):

        if self.tail == node:
            self.tail = node.next
            self.tail.prev = None
            
        if self.head == node:
            self.head = node.prev
            self.head.next = None
        
        if node.prev is not None:
            node.prev.next = node.next
            
        if node.next is not None:
            node.next.prev = node.prev
        
    def clear(self):
        self.head = None
        self.tail = None
        
                
class Node():
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
