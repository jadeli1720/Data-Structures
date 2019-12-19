import sys
sys.path.append('../queue_and_stack')
from queue_and_stack import Queue
from queue_and_stack import Stack

# any time you are cutting things in half is O(log n)

class BinarySearchTree:                              # worst case O(n), average case O(log n)
    def __init__(self, value: int):                  # restricting the input value to a number
        self.value = value
        self.left = None                             # use to traverse left ==> pointers
        self.right = None                            # use to traverse right ==> pointers

    # self is the node itself, while self.value is the value of that node

    # Insert the given value into the tree
    def insert(self, value):
        # SIMPLIFY:
        if  self.value > value:                       # If value is less than self.value
            if self.left == None:                     # If left node is empty
                 self.left = BinarySearchTree(value)  # A new Binary Search Tree with our new value
            else:
                return self.left.insert(value)        # Recursion - passing the value back into the insert() to check again if the node is empty or not on the left

        if  self.value <= value:
            if self.right == None:
                self.right = BinarySearchTree(value)
            else:
                return self.right.insert(value) 


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if target == self.value, return True,
        # go left or right based on smaller or bigger
        # If target is bigger or smaller than the self.value
        # a lot like binary search

        # base case
        if target == self.value:                      # If target == self.value
            return True                               # return true
        elif target > self.value:                     # if target > self.value
            if self.right != None:                    # if node on the right isn't a leaf
                return self.right.contains(target)    # recursively call contains to check the target value again
            else:                                     # else if we've come to a leaf and still haven't found target value 
                    return False                      # return False
            
        elif target < self.value:                     # if target < self.value
            if self.left != None:                     # if node on the left isn't a leaf
                return self.left.contains(target)     # recursively call contains to check the target value again
            else:                                     # else if we've come to a leaf and still haven't found the target value                
                    return False                      # return False
            

    # Return the maximum value found in the tree
    def get_max(self):
        #  You can only go right for largest, and you know you are at the end of the tree when the node is a leaf and there are no more children.

        if self.right != None:                        #  if right node exists
            return self.right.get_max()               # recursively call function again to keep going right. Make sure to return the recursive call
        else:
            return self.value                         # otherwise return self.value
        

    # Call the function `cb` on the value of each node
    # You may use a RECURSIVE or iterative approach
    def for_each(self, cb):                            # Just did (sneakely) a Depth First Traversal
        # Search each node in the entire tree
        
        cb(self.value)                                 # Call cb on the value of each node
        if self.right:                                 # If there is a pointer on the right
            self.right.for_each(cb)
        if self.left:                                  # If there is a pointer on the left
            self.left.for_each(cb)

        # Iterative solution: --> what do we need to use? -->need to import stack for this to work
            # Need a loop and stack
        # stack = Stack()
        # stack.push(self)
        # # Loop --> when do we know we are done? when there is nothing in the stack
        # while stack.len() > 0:
        #     current_node = stack.pop()
        #     # Check if there is a left or right
        #     if current_node.right:
        #         stack.push(current_node.right)
        #     if current_node.left:
        #         stack.push(current_node.left)
        #     cb(current_node.value)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node): # 
        # Travel left to the end of the tree
        # if node is None --> return
        if node == None:
            return
        # read node. value at end an repeat recursively
        self.in_order_print(node.left)
        print(node.value)
        # recursion to the right
        self.in_order_print(node.right)
        

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node): #annoying loops
        # instantiate a queue
        queue = Queue()
        # put root in the queue
        queue.enqueue(node)
        # while queue is not empty (meaning length in zero)
        while queue.len() > 0:
            # pop the root out of the front of the queue
            current_node = queue.dequeue()
            print(current_node.value)
            # DO SOMETHING --> I.E PRINT value
            # if left:
            if current_node.left:
                # add left to back of queue
                queue.enqueue(current_node.left)
            # if right:
            if current_node.right:
                # add right to back of queue
                queue.enqueue(current_node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # Instantiate the stack
        stack = Stack()
        # Put root node in stack 
        stack.push(node)
        # while stack not empty (meaning length in zero)
        while stack.len() > 0:
            # pop the root out of stack => stack.pop()
            current_node = stack.pop()
            # DO SOMETHING --> I.E PRINT value
            print(current_node.value)
            # if self.left:
            if current_node.left:
                # add left to the stack => stack.push()
                stack.push(current_node.left)
            # if self.right:
            if current_node.right:
                # add left to the stack => stack.push()
                stack.push(current_node.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node): # -->
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
