#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    A naive Linked List.
"""
__author__ = "Amittai"
__copyright__ = "Copyright 2021"
__credits__ = ["Amittai"]
__email__ = "Amittai.J.Wekesa.24@dartmouth.edu"
__github__ = "@siavava"

from typing import List, Optional

INDEX_ERROR = "Index out of range"
NODE_ERROR = "Node not found."

class _Node:
    """Internal node for the LL"""
    
    
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev: _Node = prev
        self.next: _Node = next
    
    def chain(self, node):
        """
            Chains a node into a sequence of nodes.\n
            NOTE: By default, `a.chain(b)` makes `b` the next node of `a`.
            To chain *before*, use `a.chain_before(b)`.
        """
        if self.next:
            node.next = self.next
            node.next.prev = node
        self.next: _Node = node
        node.prev = self
    
    def chain_before(self, node):
        if self.prev:
            self.prev.chain(node)
        else:
            self.prev: _Node = node
            node.next = self
    
    def unchain(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev
        
    def advance(self, steps):
        """
            Advances the node by steps 
            NOTE: Assumes that number of advances is valid. Caller should ascertain that!
        """
        node: _Node = self
        while node and steps > 0:
            node = node.next
            steps -= 1
        if not node:
            raise ValueError(NODE_ERROR)
        return node
    
    def rewind(self, steps):
        """
            Rewinds the node by steps
            NOTE: Assumes that number of rewinds is valid. Caller should ascertain that!
        """
        node: _Node = self
        while node and steps > 0:
            node = node.prev
            steps -= 1
        if not node:
            raise ValueError(NODE_ERROR)
        return node
        
    def __bool__(self):
        return self.value is not None
    
    def __eq__(self, other):
        return self.value == other.value
    
    def __lt__(self, other):
        return self.value < other.value
    
    def __gt__(self, other):
        return self.value > other.value
    
    def __str__(self):
        """ String representation of the node """
        s = f"(({self.value}))"
        
        # /// BACKCHAIN ///
        pred = self.prev
        while pred:
            s = f"{self.prev.value} -> " + s
            pred = pred.prev
            
        # /// FORWARD CHAIN ///
        succ = self.next
        while succ:
            s += f" -> {self.next.value}"
            succ = succ.next
        
        # /// RETURN ///
        return s
    
    @staticmethod
    def empty():
        return _Node(None)

class LinkedList(List):
    """ A naive implementation of a Linked List."""
        
    def __init__(self):
        self.__head = _Node.empty()
        self.__tail = _Node.empty()
        self.__size = 0

    def __str__(self):
        return str(self.to_list())

    def __repr__(self):
        return repr(self.to_list())

    def __len__(self):
        return self.__size
    
    def __bool__(self):
        return self.__size != 0
    
    
    def to_list(self):
        """
            Generate list version of LinkedList.
        """
        lst = []
        node = self.__head
        while node:
            lst.append(node.value)
            node = node.next
            
        return lst
    
    def append(self, value):
        if not self.__head:
            self.__head = _Node(value)
            self.__tail = self.__head
        else:
            self.__tail.chain(_Node(value))
            self.__tail = self.__tail.next
        self.__size += 1
            
    def __locate(self, index: int):
        # /// if valid index, proceed with location ///
        if 0 < index < self.__size \
            or -self.__size <= index < 0:
            # /// check target against midpoint,
            # /// use path that gives better performance! ///
            target = index if index >= 0 else self.__size + index
            mid = self.__size // 2
            if target <= mid:
                target_node: _Node = self.__head.advance(target)
            else:
                steps = (self.__size - (target + 1))
                target_node: _Node = self.__tail.rewind(steps)
            return target_node
        # /// invalid index, raise error ///
        raise IndexError(INDEX_ERROR)
        

    def __getitem__(self, index):
        target = self.__locate(index)       # /// throws exception
        return target.value
    
    def pop(self, index=-1):
        """
            Pop item, akin to a Stack operation.
            Removes and returns the item at the given index.
            If no index is specified, a.pop() removes and returns the last item.
            If the stack is empty, INDEX_ERROR is raised.
        """
        target = self.__locate(index)       # /// throws exception
        if not target.prev:
            self.__head = target.next\
                if target.next\
                    else _Node.empty()
        if not target.next:
            self.__tail = target.prev\
                if target.prev\
                    else _Node.empty()

        target.unchain()
        self.__size -= 1
        return target.value
        
    def reverse(self):
        """ Reverse *IN PLACE* """
        # /// BACKTRACK 
        # ///   SWAP PREDECESSOR,-SUCCESSOR ///
        rev = None
        forw = self.__head
        rev_head = None
        while forw:
            rev = _Node(forw.value, prev=rev)
            if not rev.prev: rev_head = rev
            elif rev.prev: rev.prev.next = rev
            forw = forw.next
        self.__head, self.__tail = rev_head, rev
        
    # /// QUEUE methofs ///
    """ Enqueue and Dequeue are the same as push and pop """
    def enqueue(self, obj):
        """ Enqueue item; akin to a Queue operation"""
        self.append(obj)
        
    def dequeue(self):
        """ Dequeue item; akin to a Queue operation"""
        return self.pop(0)
    
    def push(self, item):
        """ Push item; akin to a Stack operation"""
        self.append(item)

    def __setitem__(self, index, value):
        target = self.__locate(index)       # /// throws exception
        target.value = value

    def __delitem__(self, index):
        target: _Node = self.__locate(index)       # /// throws exception
        if index == 0: 
            self.__head = target.next
        elif index == 1: 
            self.tail = target.prev
        target.unchain()
        del target
        self.__size -= 1

    def __contains__(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next

    def __reversed__(self):
        current = self.tail
        while current:
            yield current.value
            current = current.prev
            
if __name__ == '__main__':
    
    import random
    lst = LinkedList()
    print(lst)
    
    for i in range(10):
        lst.append(random.randint(0, 1000))
        print(lst)
        
    # print(f"size = {len(lst)}")
        
    while lst:
        lst.pop()
        print(lst)
        # print(f"size = {len(lst)}")
                