import sys
sys.path.append('../doubly_linked_list') #windows may have trouble with this import go to FAQ to read about it. Copy and Paste???
from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10): #The max_number is limited to only 10 nodes within the cache
       
        self.max = limit
        self.list = DoublyLinkedList()
        self.cache = {}

        # the current number of nodes!!!!
        
        # cache key --> node  node-value =>(key,value)
    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key): # Any item we access gets moved to the head of the cache
        # Key in Cache = Key in node => key:value pair
        if key not in self.cache[key]: # check if cache is empty
            return None 
        self.cache[key] = node # Using the node to access the key
        self.list.move_to_front(node) # move accessed pair to top of the cache --> move_to_front
        return node.value[1] # returns the value associated with that key 
        

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used *(at the head)
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. NEED TO ADD THIS NEXT PART: Additionally, in the case that the key already exists in the cache, we simply want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):#creating a key:value pair as a dictionary
        self.cache[key]=value
        
        if len(self.cache) == self.max:
           self.list.remove_from_tail()
        else:
           self.list.add_to_head(key)


