from doubly_llist import DoublyLlist, Node


class LRUCache(object):
    '''
    This LRUCache will initialize with a maximum capacity. As the keys
    are added, if the maximum capacity is exceeded the least recently used
    entry will be discarded
    '''
    
    def __init__(self, max_size:int):
        
        if type(max_size)!=int or max_size <= 0:
            raise ValueError ("max_size should be greater than 0")
        
        self.init_capacity = max_size
        self.space_left = max_size
        self.cache = {}             #the main cache to hold the values for the keys
        self.dlist = DoublyLlist()  #the doubly linked list for keeping the order of use
    
    def reset(self):
        '''
        Clears all key value pairs and resets the cache to the original max capacity
        '''
        self.space_left = self.init_capacity
        self.cache.clear()
        self.dlist.clear()
       
    def delete(self, key):
        '''
        Removes the key value pair of the given key from the LRUCache
        :param key:
        '''
        if key not in self.cache:
            return
        
        node = self.cache.pop(key)        
        self.dlist.remove_node(node)
        
    def get(self, key):
        '''
        Returns the value of the given key from the cache
        and will make it the most recently used item
        :param key:
        '''
        if key not in self.cache:
            return None
        
        node = self.cache[key]
        
        if self.dlist.head == node:   #if the node is at the top just return the value
            return node.value
        
        self.dlist.remove_node(node)
        self.dlist.add_node(node)
            
        return node.value
        
    def put(self, key, value):
        '''
        Adds the key value pair to the cache, if the cache is full 
        removes the least recently used key value pair. If the key already exists, 
        it will update the value for the key and make it the most recently used item
       .
        :param key:
        :param value:
        '''
        if key in self.cache:
            
            node = self.cache[key]
            node.value = value
            
            if node != self.dlist.head:
                self.dlist.remove_node(node)
                self.dlist.add_node(node)
        else:
            node = Node(key, value)
            #If capacity is exhausted remove the item at the tail of the dlist (the lru item)
            #and also remove from the cache
            if self.space_left <= 0 and self.dlist.tail:
                tail_key = self.dlist.tail.key
                self.dlist.remove_node(self.dlist.tail)
                self.cache.pop(tail_key)
                self.space_left += 1
                 
            self.dlist.add_node(node)
            self.cache[key] = node
            self.space_left -= 1
    
    #Protected Interface for testing    
    def _get_cache(self):
        return self.cache
    
    def _increase_capacity(self, capacity):
        self.space_left +=capacity
    
    def _get_head_value(self):
        if self.dlist.head:
            return self.dlist.head.value
        return None
    
    def _get_head_key(self):
        if self.dlist.head:
            return self.dlist.head.key
        return None
    
    def _get_tail_key(self):
        if self.dlist.tail:
            return self.dlist.tail.key
        return None