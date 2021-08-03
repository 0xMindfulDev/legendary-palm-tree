'''
A Node is a record (or a data structure) with two elements - a value and a reference 
which may point to another node. The point of a node is to represent a value but 
potentially relate that value to some other value as pointed by the reference. Nodes 
are building blocks of data structures such as linked lists, graphs and trees. 
'''

class Node(object):
    '''
    in python, the object class is a generic type at the
    top of python's type hierarchy.
    '''
    def __init__(self, item, other = None):
        self. item = item
        self.other = other

    def getItem(self):
        return self.item

    def getOther(self):
        return self.other

    def setItem(self, item):
        self.item = item

    def setOther(self, other):
        self.other = other