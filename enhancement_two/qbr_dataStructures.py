#=======================================================================================
# Name        : qbr_dataStructures.py
# Author      : Quintin B. Rozelle
# Version     : 2.0
# Date        : 2025-05-24
# Description : Addition of Red-Black Tree for Enhancement 2 in CS-499
#               Contains Node class, BinarySearchTree class, and RedBlackTree class
#=======================================================================================

from typing import NewType, Any, NoReturn
from enum import Enum

# New type definitions
# Prefixed with 't_' to differentiate from 
Node = NewType('Node', 'Node')

class Node:
    """
    Node class for BinarySearchTree
    
    Attributes
    ----------
    key: Any
        The key stored in the node
    leftNode: Node
        The left child node
    rightNode: Node
        The right child node
    """

    # Color enumeration to prevent typos when hardcoding node colors
    NodeColor = Enum('NodeColor', ['RED', 'BLACK'])

    def __init__(self,
                 key: Any,
                 color: NodeColor = NodeColor.RED,
                 *,
                 leftNode: Node | None = None,
                 rightNode: Node | None = None,
                 parentNode: Node | None = None
                 ) -> NoReturn:
        """
        Initialize a new node with the given key and color
        
        Parameters
        ----------
        key: Any
            The key to be stored in the node
        color: NodeColor (optional)
            The color of the node (default is "red")
        leftNode: Node | None (optional | keyword only)
            The left child node (default is None)
        rightNode: Node | None (optional | keyword only)
            The right child node (default is None)
        parentNode: Node | None (optional | keyword only)
            The parent node (default is None)
        """
        self.key: Any = key
        self.color: Node.NodeColor = color
        self.leftNode: Node | None = leftNode
        self.rightNode: Node | None = rightNode
        self.parentNode: Node | None = parentNode
        
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
    
    def getGrandparent(self) -> Node | None:
        """
        Returns the grandparent node if it exists, else None
        
        Returns
        -------
        Node | None
            The grandparent node
        """
        if self.parentNode is None:
            return None
        return self.parentNode.parentNode
    
    def getSibling(self) -> Node | None:
        """
        Returns the sibling node if it exists, else None
        
        Returns
        -------
        Node | None
            The sibling node
        """
        if self.parentNode is None:
            return None
        if self is self.parentNode.leftNode:
            return self.parentNode.rightNode
        else:
            return self.parentNode.leftNode
    
    def getUncle(self) -> Node | None:
        """
        Returns the uncle node if it exists, else None
        
        Returns
        -------
        Node | None
            The uncle node
        """
        if self.parentNode is None:
            return None
        return self.parentNode.getSibling()

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
        root: Node
            The root node of the BST (default is None)
        """
        self.root = None
    
    def insert(self, key: Any) -> NoReturn:
        """
        Insert a new key into the BST
        
        Parameters
        ----------
        key: Any
            The key to be inserted into the BST
        """        
        # Base case
        if self.root is None:
            self.root = Node(key)
            
        
        # Iteratvely traverse tree to insertion point
        parentNode: Node = None
        currentNode: Node = self.root
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
        key: Any
            The key to be deleted from the BST
        """
        parentNode: Node = None
        currentNode: Node = self.root
        
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
                    successor: Node = currentNode.rightNode
                    while successor.leftNode is not None:
                        successor = successor.leftNode
                    tempSuccessor: Node = Node(1)
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
        key: Any
            The key to be searched for in the BST
            
        Returns
        -------
        Any
            The full key if found, otherwise None.
            Allows for returning full key if keys are complex objects
            and search was performed with dummy key containing only
            the attributed used for comparison.
        """
        currentNode: Node = self.root
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
        stack: list = []
        currentNode: Node = self.root
        while currentNode is not None or len(stack) > 0:
            # Traverse tree and add path to stack
            while currentNode is not None:
                stack.append(currentNode)
                currentNode = currentNode.leftNode
            currentNode = stack.pop()
            print(currentNode, end='\n')
            currentNode = currentNode.rightNode
        return
 
# Red-Black Tree Class
# Functions adapted from https://www.geeksforgeeks.org/red-black-tree-in-python/ with modifications
class RedBlackTree:
    """
    Red Black Tree (RBT) implementation
    
    Methods
    -------
    fixInsertion(node=Node)
        Cleans up tree after node insertion to ensure balancing
    insert(key=Any)
        Inserts a new key into the RBT
    rotateLeft(node=Node)
        Rotates Node to left of Node's rightNode
    rotateRight(node=Node)
        Rotates Node to right of Node's leftNode
    fixDeletion(node=Node)
        Cleans up tree after node deletion to ensure balancing
    remove(key=Any)
        Removes a key from the RBT
    search(key=Any)
        Searches for a key in the RBT
    findSmallest(node=Node)
        Finds smallest Node under given Node
    inOrderTraversal()
        Traverses the RBT in order
    """
    def __init__(self) -> NoReturn:
        """
        Initialize a new red black tree
        
        Parameters
        ----------
        root: Node
            The root node of the RBT (default is None)
        """
        self.root = None
        
    def fixInsertion(self, node: Node) -> NoReturn:
        """
        Fixes the tree after node insertion to ensure balancing
        
        Parameters
        ----------
        node: Node
            The Node around which clean up needs to happen
        """
        while node.parentNode and node.parentNode.color == Node.NodeColor.RED:
            uncle: Node = node.getUncle()
            # Grandparent must be black so change colors and move up tree
            if uncle and uncle.color == Node.NodeColor.RED:
                node.parentNode.color = Node.NodeColor.BLACK
                uncle.color = Node.NodeColor.BLACK
                node.getGrandparent().color = Node.NodeColor.RED
                node = node.getGrandparent()
            else:
                # Left-x cases
                if node.getGrandparent().leftNode is node.parentNode:
                    # Left-Right case
                    if node.parentNode.rightNode is node:
                        node = node.parentNode
                        self.rotateLeft(node)
                    # Left-Left case
                    node.parentNode.color = Node.NodeColor.BLACK
                    node.getGrandparent().color = Node.NodeColor.RED
                    self.rotateRight(node.getGrandparent())
                # Right-x cases
                else:
                    # Right-Left case
                    if node.parentNode.leftNode is node:
                        node = node.parentNode
                        self.rotateRight(node)
                    # Right-Right case
                    node.parentNode.color = Node.NodeColor.BLACK
                    node.getGrandparent().color = Node.NodeColor.RED
                    self.rotateLeft(node.getGrandparent())
        # Ensure root is always black
        self.root.color = Node.NodeColor.BLACK
    
    def insert(self, key: Any) -> NoReturn:
        """
        Insert a new key into the RBT
        
        Parameters
        ----------
        key: Any
            The key to be inserted into the RBT
        """
        # Build new node with null leaves
        newNode: Node = Node(key)
        newNode.leftNode = Node(None, Node.NodeColor.BLACK, parentNode=newNode)
        newNode.rightNode = Node(None, Node.NodeColor.BLACK, parentNode=newNode)
        
        # Base case
        if self.root is None:
            self.root = newNode
        
        # Iteratvely traverse tree to insertion point and add
        currentNode: Node = self.root
        while True:
            if currentNode.key > key:
                if currentNode.leftNode.key is None:
                    currentNode.leftNode = newNode
                    newNode.parentNode = currentNode
                    break
                else:
                    currentNode = currentNode.leftNode
            elif currentNode.key < key:
                if currentNode.rightNode.key is None:
                    currentNode.rightNode = newNode
                    newNode.parentNode = currentNode
                    break
                else:
                    currentNode = currentNode.rightNode
            # Do not add duplicate
            else:
                break
        self.fixInsertion(newNode)
    
    def rotateLeft(self, node: Node) -> NoReturn:
        """
        Rotates Node to left of Node's rightNode
        
        Parameters
        ----------
        node: Node
            The Node around which rotation needs to happen
        """
        # Move node's rightNode's leftNode to node's rightNode
        rightChild: Node = node.rightNode
        node.rightNode = rightChild.leftNode
        # Update parent nodes
        if rightChild.leftNode is not None:
            rightChild.leftNode.parentNode = node
        rightChild.parentNode = node.parentNode
        # Move up node's rightNode
        if node.parentNode is None:
            self.root = rightChild
        elif node is node.parentNode.leftNode:
            node.parentNode.leftNode = rightChild
        else:
            node.parentNode.rightNode = rightChild
        # Move down node
        rightChild.leftNode = node
        node.parentNode = rightChild
        
    def rotateRight(self, node: Node) -> NoReturn:
        """
        Rotates Node to right of Node's leftNode
        
        Parameters
        ----------
        node: Node
            The Node around which rotation needs to happen
        """
        # Move node's leftNode's rightNode to node's leftNode
        leftChild: Node = node.leftNode
        node.leftNode = leftChild.rightNode
        # Update parent nodes
        if leftChild.rightNode is not None:
            leftChild.rightNode.parentNode = node
        leftChild.parentNode = node.parentNode
        # Move up node's leftNode
        if node.parentNode is None:
            self.root = leftChild
        elif node is node.parentNode.rightNode:
            node.parentNode.rightNode = leftChild
        else:
            node.parentNode.leftNode = leftChild
        # Move down node
        leftChild.rightNode = node
        node.parentNode = leftChild
    
    def replace(self, oldNode: Node, newNode: Node) -> NoReturn:
        """
        Replaces a node with a new one
        
        Parameters
        ----------
        oldNode: Node
            The node to be replace
        newNode: Node
            The replacement node
        """
        # oldNode is root
        if oldNode.parentNode is None:
            self.root = newNode
        else:
            if oldNode == oldNode.parentNode.leftNode:
                oldNode.parentNode.leftNode = newNode
            else:
                oldNode.parentNode.rightNode = newNode
        newNode.parentNode = oldNode.parentNode
    
    def fixDeletion(self, node: Node) -> NoReturn:
        """
        Cleans up tree after node deletion to ensure balancing
        
        Parameters
        ----------
        node: Node
            The Node around which clean up needs to happen
        """
        while node != self.root and node.color == Node.NodeColor.BLACK:
            if node.parentNode.leftNode is node:
                siblingNode: Node = node.getSibling()
                # Sibling is red so swap sibling and parent colors and rotate parent left
                if siblingNode.color == Node.NodeColor.RED:
                    siblingNode.color = Node.NodeColor.BLACK
                    node.parentNode.color = Node.NodeColor.RED
                    self.rotateLeft(node.parentNode)
                    siblingNode = node.getSibling()
                # Sibling is red but children are not red so color sibling red
                if (siblingNode.leftNode is None or siblingNode.leftNode.color == Node.NodeColor.BLACK) and \
                   (siblingNode.rightNode is None or siblingNode.rightNode.color == Node.NodeColor.BLACK):
                       siblingNode.color = Node.NodeColor.RED
                       node = node.parentNode
                else:
                    # Sibling is not red and sibling's right child is not red so swap colors and rotate right
                    if siblingNode.rightNode is None or siblingNode.rightNode.color == Node.NodeColor.BLACK:
                        siblingNode.leftNode.color = Node.NodeColor.BLACK
                        siblingNode.color = Node.NodeColor.RED
                        self.rotateRight(siblingNode)
                        siblingNode = node.getSibling()
                    siblingNode.color = node.parentNode.color
                    node.parentNode.color = Node.NodeColor.BLACK
                    if siblingNode.rightNode:
                        siblingNode.rightNode.color = Node.NodeColor.BLACK
                    self.rotateLeft(node.parentNode)
                    node = self.root
            # Same as above but mirrored
            else:
                siblingNode: Node = node.getSibling()
                if siblingNode.color == Node.NodeColor.RED:
                    siblingNode.color = Node.NodeColor.BLACK
                    node.parentNode.color = Node.NodeColor.RED
                    self.rotateRight(node.parentNode)
                    siblingNode = node.getSibling()
                if (siblingNode.leftNode is None or siblingNode.leftNode.color == Node.NodeColor.BLACK) and \
                   (siblingNode.rightNode is None or siblingNode.rightNode.color == Node.NodeColor.BLACK):
                       siblingNode.color = Node.NodeColor.RED
                       node = node.parentNode
                else:
                    if siblingNode.leftNode is None or siblingNode.leftNode.color == Node.NodeColor.BLACK:
                        siblingNode.rightNode.color = Node.NodeColor.BLACK
                        siblingNode.color = Node.NodeColor.RED
                        self.rotateLeft(siblingNode)
                        siblingNode = node.getSibling()
                    siblingNode.color = node.parentNode.color
                    node.parentNode.color = Node.NodeColor.BLACK
                    if siblingNode.leftNode:
                        siblingNode.leftNode.color = Node.NodeColor.BLACK
                    self.rotateRight(node.parentNode)
                    node = self.root
        node.color = Node.NodeColor.BLACK
    
    def remove(self, key: Any) -> NoReturn:
        """
        Removes a key from the RBT
        
        Parameters
        ----------
        key: Any
            The key to be deleted from the RBT
        """
        foundNode: Node | None = self.search(key)
        if foundNode is None:
            return
        # Node is a leaf
        if foundNode.leftNode.key is None and foundNode.rightNode.key is None:
            replacementNode = Node(None, Node.NodeColor.BLACK)
            self.replace(foundNode, replacementNode)
        # Node has no left child
        elif foundNode.leftNode.key is None:
            replacementNode = foundNode.rightNode
            self.replace(foundNode, replacementNode)
        # Node has no right child
        elif foundNode.rightNode.key is None:
            replacementNode = foundNode.leftNode
            self.replace(foundNode, replacementNode)
        # Node has two children
        else:
            replacementNode: Node = self.findSmallest(foundNode.rightNode)
            foundNode.key = replacementNode.key
            self.replace(replacementNode, replacementNode.rightNode)
        self.fixDeletion(replacementNode)
        
    
    def search(self, key: Any) -> Node | None:
        """
        Searches for a key in the RBT
        
        Parameters
        ----------
        key: Any
            The key to be searched for in the RBT
            
        Returns
        -------
        Node | None
            The full key if found, otherwise None.
            Allows for returning full key if keys are complex objects
            and search was performed with dummy key containing only
            the attributed used for comparison.
        """
        currentNode: Node = self.root
        while currentNode.key is not None:
            if key == currentNode.key:
                return currentNode
            elif key < currentNode.key:
                currentNode = currentNode.leftNode
            else:
                currentNode = currentNode.rightNode
    
    def findSmallest(self, node: Node) -> Node:
        """
        Finds smallest Node under given Node
        
        Parameters
        ----------
        node: Node
            The Node under which to search for the smallest node
            
        Returns
        -------
        node: Node
            The smallest Node found
        """
        while node.leftNode.key is not None:
            node = node.leftNode
        return node
    
    # Solution adapted from: https://www.geeksforgeeks.org/inorder-tree-traversal-without-recursion/
    def inOrderTraversal(self) -> NoReturn:
        """
        Prints the RBT to the screen in order
        """
        # Stack to hold path while traversing
        stack: list = []
        currentNode: Node = self.root
        while currentNode is not None or len(stack) > 0:
            # Traverse tree and add path to stack
            while currentNode is not None:
                stack.append(currentNode)
                currentNode = currentNode.leftNode
            currentNode = stack.pop()
            if currentNode.key is not None:
                print(currentNode, end='\n')
            currentNode = currentNode.rightNode
        return