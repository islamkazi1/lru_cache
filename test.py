'''
Created on Aug 30, 2020

@author: kislam
'''
import unittest

from lru_cache import LRUCache


class Test(unittest.TestCase):


    def test_get_should_make_it_top(self):
        lru_cache = LRUCache(3)
        lru_cache.put(1, "abc")
        lru_cache.put(2, "edf")
        lru_cache.put(3, "ghi")
        
        self.assertEqual(lru_cache._get_head_key(), 3, "Failed")
        
        lru_cache.get(1)
        
        self.assertEqual(lru_cache._get_head_key(), 1, "Failed")
        
    def test_item_removal_with_get(self):
        lru_cache = LRUCache(3)
        lru_cache.put(1, "abc")
        lru_cache.put(2, "edf")
        lru_cache.put(3, "ghi")
        lru_cache.get(1)
        
        lru_cache.put(4, "jkl")
        
        self.assertIsNone(lru_cache.get(2), "Failed")
        
    def test_put_should_add_new_and_evict_tail(self):
        lru_cache = LRUCache(3)
        lru_cache.put(1, "abc")
        lru_cache.put(2, "edf")
        lru_cache.put(3, "ghi")
        
        lru_cache.put(4, "jkl")
        
        self.assertIsNone(lru_cache.get(1), "Failed")
        self.assertEqual(lru_cache.get(4), "jkl", "Failed")
    
    def test_put_should_place_item_at_top_and_update_existing_key_value(self):
        lru_cache = LRUCache(3)
        lru_cache.put(1, "abc")
        lru_cache.put(2, "edf")
        lru_cache.put(3, "ghi")
        
        self.assertEqual(lru_cache._get_head_key(), 3, "Failed")
        
        lru_cache.put(2, "jkl")
        self.assertEqual(lru_cache._get_head_key(), 2, "Failed")
        
        self.assertEqual(lru_cache.get(2), "jkl", "Failed")
        
    def test_non_existing_key(self):
        lru_cache = LRUCache(3)
        self.assertIsNone(lru_cache.get(1), "Failed")
    
    def test_del_should_remove_key_value(self):
        lru_cache = LRUCache(3)
        lru_cache.put(1, "abc")
        lru_cache.put(2, "edf")
        lru_cache.put(3, "ghi")
        
        #deleting head
        lru_cache.delete(3)
        
        self.assertEqual(lru_cache._get_head_key(), 2, "Failed")
        self.assertEqual(lru_cache._get_head_value(), "edf", "Failed")
        
        self.assertIsNone(lru_cache.get(3), "Failed")
        
        #deleting tail
        lru_cache.put(3, "ghi")
        lru_cache.delete(1)
        
        self.assertEqual(lru_cache._get_tail_key(), 2, "Failed")
        
    
    def test_del_should_do_no_op_when_key_not_found(self):
        
        lru_cache = LRUCache(3)
        lru_cache.put(1, "abc")
        lru_cache.put(2, "edf")
        lru_cache.put(3, "ghi")
        lru_cache.delete(4)
        
        self.assertEqual(lru_cache._get_head_value(), "ghi", "Failed")
    
    def test_no_max_size_should_throw_error(self):
        
        with self.assertRaises(ValueError):
            LRUCache(0)
     
    def test_reset_should_clear(self):
        lru_cache = LRUCache(3)
        lru_cache.put("a", "abc")
        lru_cache.put("b", "edf")
        lru_cache.put("c", "ghi")
        
        self.assertEqual(len(lru_cache._get_cache()), 3, "Failed")
        
        lru_cache.reset()
        
        self.assertEqual(len(lru_cache._get_cache()), 0, "Failed")
            
if __name__ == "__main__":
    unittest.main()