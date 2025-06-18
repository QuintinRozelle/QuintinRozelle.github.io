#=======================================================================================
# Name        : BinarySearchTree.py
# Author      : Quintin B. Rozelle
# Version     : 1.0
# Date        : 2025-05-16
# Description : Test of BinarySearchTree module
#=======================================================================================

import unittest
import binarySearchTree
from io import StringIO
import sys

# keys to build BST tree with
# 3 added twice to test that duplicates are not added
keys = [10, 5, 15, 3, 7, 12, 18, 3]
invalidKeys = [20, 25, 30, 35, -10, -20, 0, 0.5, 0.25, -0.5, -0.25]

# Utility function to check that BST is valic
def isBinarySearchTree(node, leftNode=None, rightNode=None):
        # base case, node is a leaf
        if node is None:
            return True
        # test if child nodes are valid
        if leftNode is not None and node <= leftNode:
            return False
        if rightNode is not None and node >= rightNode:
            return False
        # recursively check left and right nodes
        return isBinarySearchTree(node.leftNode, leftNode, node) and isBinarySearchTree(node.rightNode, node, rightNode)


class TestBinarySearchTree(unittest.TestCase):
    # Build test BST
    def setUp(self):
        self.node1 = binarySearchTree.Node(1)
        self.node2 = binarySearchTree.Node(2)
        self.node3 = binarySearchTree.Node(3)
        self.bst = binarySearchTree.BinarySearchTree()
        for key in keys:
            self.bst.insert(key)
        
    # Test that node comparison for equality works
    def test_node_equality(self):
        self.assertEqual(self.node1, self.node1)
        self.assertNotEqual(self.node1, self.node2)

    # Test that node comparison for inequality works
    def test_node_comparison(self):
        self.assertTrue(self.node1 < self.node2)
        self.assertTrue(self.node1 <= self.node2)
        self.assertTrue(self.node1 <= self.node1)
        self.assertTrue(self.node3 > self.node2)
        self.assertTrue(self.node3 >= self.node2)
        self.assertTrue(self.node3 >= self.node3)
        self.assertFalse(self.node1 > self.node2)
        self.assertFalse(self.node1 >= self.node2)
        self.assertFalse(self.node3 < self.node2)
        self.assertFalse(self.node3 <= self.node2)

    # Test that string represntation of node class works
    def test_node_string_representation(self):
        self.assertEqual(str(self.node1), "1")
        self.assertEqual(str(self.node2), "2")
        self.assertEqual(str(self.node3), "3")

    # Test that keys were inserted correctly during build
    def test_insert(self):
        self.assertTrue(self.bst.root.key == keys[0])
        self.assertTrue(isBinarySearchTree(self.bst.root))
        
    # Test that search works correctly
    def test_search(self):
        for key in keys:
            self.assertTrue(self.bst.search(key))
        for key in invalidKeys:
            self.assertFalse(self.bst.search(key))
        
    # Test that key removal works correctly
    def test_delete(self):
        for key in invalidKeys:
            self.bst.remove(key)
            self.assertTrue(isBinarySearchTree(self.bst.root))
            self.assertFalse(self.bst.search(key))
        
        # remove leaf
        self.bst.remove(3)
        self.assertTrue(isBinarySearchTree(self.bst.root))
        self.assertFalse(self.bst.search(3))
        
        # remove node with one child
        self.bst.remove(5)
        self.assertTrue(isBinarySearchTree(self.bst.root))
        self.assertFalse(self.bst.search(5))
        
        # remove node with two children
        self.bst.remove(15)
        self.assertTrue(isBinarySearchTree(self.bst.root))
        self.assertFalse(self.bst.search(15))
        
        # remove root
        self.bst.remove(10)
        self.assertTrue(isBinarySearchTree(self.bst.root))
        self.assertFalse(self.bst.search(10))
    
    # Test in-order traversal    
    def test_in_order_traversal(self):
        expected = '\n'.join(f'{key}' for key in sorted(set(keys)))
        # redirect output to 'result' object
        result = StringIO()
        sys.stdout = result
        self.bst.inOrderTraversal()
        # directs output back to console for future use
        sys.stdout = sys.__stdout__
        self.assertEqual(result.getvalue().strip(), expected)
    
if __name__ == '__main__':
    unittest.main(verbosity=2)
