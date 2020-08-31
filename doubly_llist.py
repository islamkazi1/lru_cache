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
        '''
        Adds node as the head and tail, if list is empty otherwise adds it after the head,
        links the existing head as the previous of the node. Finally makes the node current head
        :param node:
        '''
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.prev = self.head
            self.head.next = node
            self.head = node
        
    def remove_node(self, node):
        '''
        Removes the node from the list and adjusts the previous and next links accordingly
        :param node:
        '''
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
