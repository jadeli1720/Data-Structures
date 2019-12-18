import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage list that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10): #The max_number is limited to only 10 nodes within the cache
       
        self.max = limit #--> max number of nodes
        self.nodes = 0 #--> current number of nodes set to 0
        self.list = DoublyLinkedList() # --> will hold [key:value] entries and give access to methods from dll
        self.cache = {} # --> 

        # the current number of nodes!!!!

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    # What needs to be done:
        # [x] - get the value of a given key
        # [x]- move [key:value] to the head --> most-recently used comes first
        # [x] - return the value associated with the key or none if [key:value] != exist

    def get(self, key):
        ### Key in Cache = Key in node => key:value pair
                                #            0    1
        # cache key --> node  node-value =>[key:value]

        if key not in self.cache: # check if cache is empty
            return None 
        node = self.cache[key]  # Using the node to access the key. (reference)
        
        self.list.move_to_front(node) # move accessed pair to the head of the cache --> move_to_front
        return node.value[1] # returns the value associated with that key 
        

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the case that the key already exists in the cache, we simply want to overwrite the old value associated with the key with the newly-specified value.
    """
    def set(self, key, value):#creating a key:value pair as a list or array
        # [x] - Adds [key:pair] to cache
        # [x] - Recently added [key:pair] should be at the head of the cache (most-recently used)
        # [x] - If cache == self.max, remove entry at the tail(oldest entry)
        # [x] - In case KEY ALREADY EXISTS, overwrite the old value associated with the key with the newly-specified value ****


        # If the key exists in self.cache
        if key in self.cache:
            node = self.cache[key] # Using the node to reference and access the key in the cache
            node.value = (key, value) # setting the value of the node to a [key:value]
            self.list.move_to_front(node)# move accessed pair to the head of the cache 

        elif self.nodes == self.max: # If the cache is already at max capacity, remove it from the tail
            del self.cache[self.list.tail.value[0]]
            self.list.remove_from_tail() #remove node from tail
            self.nodes -= 1
        
        self.nodes += 1
        value = (key,value)
        self.list.add_to_head(value) # add the new [key:pair] to cache
        self.cache[key] = self.list.head #add the node to the head of the cache
            

