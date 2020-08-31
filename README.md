<b>lru_cache</b>

A least recently used (LRU) cache with O(1) get,put and delete operations, implemented in Python 3.8.5. It will place the
items on top whenever a get or put is used. If the cache is full, during the put operation the least recently used item will be
evicted from the cache. If the put operation is used for an existing key, it will get updated with the new value.


<b>Installation and Prerequisites</b>
- Python 3.8.5 installed and added in PATH

<b>Usage</b>
- Import LRUCache from lru_cache.py in your python script
- To create an LRUCache, provide an Integer value of the maximum size fot the cache as the constructor parameter, any other types or a value less than 1 will result in a Value Error
- Use the put(key,value) api to place the object in the cache, please note the key object must be hashable
- Use the get(key) api to retrieve the object from the cache
- Use the delete(key) to delete a key value pair from the cache
- Use the reset() api to empty the cache and initialize it back to the maximum size

<b>Testing</b>
- run the test.py from the command promtp or shell like the following:
	 </br>py test.py
- It has 9 basic test cases to cover most of the use cases
- You can modify the test.py to include your own tests or change the cache sizes as well
