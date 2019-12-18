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

    # def search(self, data):
    #     current = self.head
    #     found = False
    #     while current and found is False:
    #         if current.get_data() == data:
    #             found = True
    #         else:
    #             current = current.get_next()
    #     if current is None:
    #         raise ValueError("Data not in list")
    #     return current

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key): # Any item we access gets moved to the head of the cache
        # access key:value pair
        # move accessed pair to top of the cache --> move_to_front
        # move other pairs down one spot in cache
        # returns the value associated with that key or
        # returns none if key:value pair doesn't exist
        pass
        

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used *(at the head)
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):#creating a key:value pair as a dictionary
        self.cache[key]=value
        
        if len(self.cache) == self.max:
           self.list.remove_from_tail()
        else:
           self.list.add_to_head(key)


# LRUCache()