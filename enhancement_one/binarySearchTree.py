#=======================================================================================
# Name        : BinarySearchTree.py
# Author      : Quintin B. Rozelle
# Version     : 1.0
# Date        : 2025-05-16
# Description : Conversion of BinarySearchTree.cpp to Python for Enhancement 1 in CS-499
#               Contains BinarySearchTree class
#=======================================================================================

from typing import NewType, Any, NoReturn

# New type definitions
# Prefixed with 't_' to differentiate from 
Node = NewType('Node', 'Node')

class Node:
    """
    Node class for BinarySearchTree
    
    Attributes
    ----------
    key : Any
        The key stored in the node
    leftNode : Node
        The left child node
    rightNode : Node
        The right child node
    """
    
    def __init__(self, key: Any) -> NoReturn:
        """
        Initialize a new node with the given key
        
        Parameters
        ----------
        key : Any
            The key to be stored in the node
        leftNode : Node
            The left child node (default is None)
        rightNode : Node
            The right child node (default is None)
        """
        self.key : Any = key
        self.leftNode : Node = None
        self.rightNode: Node = None
    
    # Comparitor methods for Node class
    def __eq__(self, other: Node) -> bool:
        """
        Compares two nodes for equality based on their keys
        
        Parameters
        ----------
        other: Node
            Second node to compare with
        
        Returns
        -------
        bool
            True if the keys are equal, False otherwise        
        """
        if isinstance(other, Node):
            return self.key == other.key
        return False
    
    def __lt__(self, other: Node) -> bool:
        """
        Compares two nodes for less than inequality based on their keys
        
        Parameters
        ----------
        other: Node
            Second node to compare with
            
        Returns
        -------
        bool
            True if the first node's key is less than the second node's key, False otherwise
        """
        if isinstance(other, Node):
            return self.key < other.key
        return False
    
    def __le__(self, other: Node) -> bool:
        """
        Compares two notes for less than or equal to inequality based on their keys
        
        Parameters
        ----------
        other: Node
            Second node to compare with
            
        Returns
        -------
        bool
            True if the first node's key is less than or equal to the second node's key, False otherwise
        """
        if isinstance(other, Node):
            return self.key <= other.key
        return False
    
    def __gt__(self, other: Node) -> bool:
        """
        Compares two notes for greater than inequality based on their keys
        
        Parameters
        ----------
        other: Node
            Second node to compare with
            
        Returns
        -------
        bool
            True if the first node's key is greater than the second node's key, False otherwise
        """
        if isinstance(other, Node):
            return self.key > other.key
        return False
    
    def __ge__(self, other: Node) -> bool:
        """
        Compares two notes for greater than or equal to inequality based on their keys
        
        Parameters
        ----------
        other: Node
            Second node to compare with
            
        Returns
        -------
        bool
            True if the first node's key is greater than or equal to the second node's key, False otherwise
        """
        if isinstance(other, Node):
            return self.key >= other.key
        return False
    
    def __str__(self) -> str:
        """
        Returns a string representation of the node
        
        Returns
        -------
        str
            A string representation of the node's key
        """
        return f"{self.key}"

# BinarySearchTree class
class BinarySearchTree:
    """
    Binary Search Tree (BST) implementation
    
    Methods
    -------
    insert(key=Any)
        Inserts a new key into the BST
    remove(key=any)
        Removes a key from the BST
    search(key=any)
        Searches for a key in the BST
    inOrderTraversal()
        Traverses the BST in order
    """
    def __init__(self) -> NoReturn:
        """
        Initialize a new binary search tree
        
        Parameters
        ----------
        root : Node
            The root node of the BST (default is None)
        """
        self.root = None
    
    def insert(self, key: Any) -> NoReturn:
        """
        Insert a new key into the BST
        
        Parameters
        ----------
        key : Any
            The key to be inserted into the BST
        """        
        # Base case
        if self.root is None:
            self.root = Node(key)
        
        # Iteratvely traverse tree to insertion point
        parentNode : Node = None
        currentNode : Node = self.root
        while currentNode is not None:
            parentNode = currentNode
            if currentNode.key > key:
                currentNode = currentNode.leftNode
            elif currentNode.key < key:
                currentNode = currentNode.rightNode
            # Do not add duplicate
            else:
                return

        # Add new node to tree
        if parentNode.key > key:
            parentNode.leftNode = Node(key)
        else:
            parentNode.rightNode = Node(key)
    
    def remove(self, key: Any) -> NoReturn:
        """
        Removes a key from the BST
        
        Parameters
        ----------
        key : Any
            The key to be deleted from the BST
        """
        parentNode : Node = None
        currentNode : Node = self.root
        
        # Begin cycling through nodes
        while currentNode is not None:
            if currentNode.key == key:
                # Node is a leaf; remove it
                if currentNode.leftNode is None and currentNode.rightNode is None:
                    if parentNode is None:
                        currentNode = None
                    elif parentNode.leftNode == currentNode:
                        parentNode.leftNode = None
                    else:
                        parentNode.rightNode = None
                # Node has one child; remove it and move the child up
                elif currentNode.rightNode == None:
                    if parentNode == None:
                        self.root = currentNode.leftNode
                    elif parentNode.leftNode == currentNode:
                        parentNode.leftNode = currentNode.leftNode
                    else:
                        parentNode.rightNode = currentNode.leftNode
                elif currentNode.leftNode == None:
                    if parentNode == None:
                        self.root = currentNode.rightNode
                    elif parentNode.leftNode == currentNode:
                        parentNode.leftNode = currentNode.rightNode
                    else:
                        parentNode.rightNode = currentNode.rightNode
                # Node has two children; find the minimum value in the right subtree and promote
                else:
                    successor : Node = currentNode.rightNode
                    while successor.leftNode is not None:
                        successor = successor.leftNode
                    tempSuccessor : Node = Node(1)
                    tempSuccessor.key = successor.key
                    self.remove(successor.key)
                    currentNode.key = tempSuccessor.key
                return
            # Node not found; continue searching
            elif currentNode.key < key:
                parentNode = currentNode
                currentNode = currentNode.rightNode
            else:
                parentNode = currentNode
                currentNode = currentNode.leftNode
        return
    
    def search(self, key: Any) -> Any:
        """
        Searches for a key in the BST
        
        Parameters
        ----------
        key : Any
            The key to be searched for in the BST
            
        Returns
        -------
        Any
            The full key if found, otherwise None.
            Allows for returning full key if keys are complex objects
            and search was performed with dummy key containing only
            the attributed used for comparison.
        """
        currentNode : Node = self.root
        while currentNode is not None:
            if currentNode.key == key:
                return currentNode.key
            elif currentNode.key > key:
                currentNode = currentNode.leftNode
            else:
                currentNode = currentNode.rightNode
        return None
    
    # Solution adapted from: https://www.geeksforgeeks.org/inorder-tree-traversal-without-recursion/
    def inOrderTraversal(self) -> NoReturn:
        """
        Prints the BST to the screen in order
        """
        # Stack to hold path while traversing
        stack : list = []
        currentNode : Node = self.root
        while currentNode is not None or len(stack) > 0:
            # Traverse tree and add path to stack
            while currentNode is not None:
                stack.append(currentNode)
                currentNode = currentNode.leftNode
            currentNode = stack.pop()
            print(currentNode, end='\n')
            currentNode = currentNode.rightNode
        return
