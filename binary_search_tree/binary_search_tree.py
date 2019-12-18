import sys
sys.path.append('../stack_dll')
# from dll_queue import Queue
# from stack_dll import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        
        # print("Node",current_node,"Node Value" ,current_node.value)

        # If inserting we must already have a tree/root <-- ?
        #value = self.value

        # SIMPLIFY:
        if value > self.value:                            # If value is less than self.value
            if self.left == None:                         # If left node is empty
                return self.left.insert(value)                   # Insert the value
                # self.left = BinarySearchTree(value)        # Recursion to keep searching until empty node is found
            else:
                # return self.left.insert(value)
                self.left = BinarySearchTree(value)      # Recursion:  keep searching until empty node is found

        elif value >= self.value:
            if self.right == None:
                self.right = BinarySearchTree(value)
                # return self.right.insert(value)
            else:
                # self.right = BinarySearchTree(value)
                return self.right.insert(value)


    

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if target == self.value, return it,
        # go left or right based on smaller or bigger
        pass

    # Return the maximum value found in the tree
    def get_max(self):
        #  if right exists, go right
        # otherwise return self.value
        pass

    # Call the function `cb` on the value of each node
    # You may use a RECURSIVE or iterative approach
    def for_each(self, cb):
        pass

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
