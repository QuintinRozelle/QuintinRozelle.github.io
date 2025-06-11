#=======================================================================================
# Name        : test_qbr_dataStructures.py
# Author      : Quintin B. Rozelle
# Version     : 2.0
# Date        : 2025-05-24
# Description : Test of qbr_dataStructures module
#=======================================================================================

import unittest
import qbr_dataStructures
from io import StringIO
import sys

# keys to build BST tree with
# 3 added twice to test that duplicates are not added
keys = [5, 12, 3, 10, 15, 7, 18, 9, 3]
invalidKeys = [20, 25, 30, 35, -10, -20, 0, 0.5, 0.25, -0.5, -0.25]

# Utility function to check that BST is valic
def isBinarySearchTree(node, leftNode=None, rightNode=None):
    # base case, node is a leaf
    if node is None or node.key is None:
        return True
    # test if child nodes are valid
    if leftNode is not None and node <= leftNode:
        return False
    if rightNode is not None and node >= rightNode:
        return False
    # recursively check left and right nodes
    return isBinarySearchTree(node.leftNode, leftNode, node) and isBinarySearchTree(node.rightNode, node, rightNode)

def isRedBlackTree(node, parentColor=qbr_dataStructures.Node.NodeColor.RED):
    # base case, node is black leaf
    if node.key is None and node.color == qbr_dataStructures.Node.NodeColor.BLACK:
        return True
    # test if root is red
    if node.parentNode == None and node.color == qbr_dataStructures.Node.NodeColor.RED:
        return False
    # test if child node and parent node are both red
    if parentColor == qbr_dataStructures.Node.NodeColor.RED and node.color == qbr_dataStructures.Node.NodeColor.RED:
        return False
    return isRedBlackTree(node.leftNode, node.color) and isRedBlackTree(node.rightNode, node.color)

# Solution adapted from: https://www.geeksforgeeks.org/level-order-tree-traversal/    
def levelOrderTraversal(node):
    # multi dimensional array to store nodes in level order traversal
    result = []
    
    def _levelOrderTraversal(node, level, result):
        # base case, node is a leaf
        if node is None:
            return
        # add new level to result if not already added
        if len(result) <= level:
            result.append([])
        # add node to result
        result[level].append(node.key)
        # look at child nodes
        _levelOrderTraversal(node.leftNode, level + 1, result)
        _levelOrderTraversal(node.rightNode, level + 1, result)
    
    _levelOrderTraversal(node, 0, result)
    return result
    
    

class TestNode(unittest.TestCase):
    def setUp(self):        
        self.testNode1 = qbr_dataStructures.Node(1)
        self.testNode2 = qbr_dataStructures.Node(2, qbr_dataStructures.Node.NodeColor.RED)
        self.testNode3 = qbr_dataStructures.Node(3, qbr_dataStructures.Node.NodeColor.BLACK)
        
        # Set nodes with parents and children
        # Final "structure" looks like:
        #           testNode4
        #           /       \
        #       testNode5     testNode8
        #       /   \             /    \
        # testNode6  testNode7  None   None
        self.testNode4 = qbr_dataStructures.Node(4)
        self.testNode5 = qbr_dataStructures.Node(5)
        self.testNode6 = qbr_dataStructures.Node(6)
        self.testNode7 = qbr_dataStructures.Node(7)
        self.testNode8 = qbr_dataStructures.Node(8)
        self.testNode4.leftNode = self.testNode5
        self.testNode4.rightNode = self.testNode8
        self.testNode5.parentNode = self.testNode4
        self.testNode5.leftNode = self.testNode6
        self.testNode5.rightNode = self.testNode7
        self.testNode6.parentNode = self.testNode5    
        self.testNode7.parentNode = self.testNode5
        self.testNode8.parentNode = self.testNode4
        
    # Test Node constructor
    def test_node_constructor(self):       
        self.assertEqual(self.testNode1.key, 1)
        self.assertEqual(self.testNode1.color, qbr_dataStructures.Node.NodeColor.RED)
        self.assertEqual(self.testNode1.leftNode, None)
        self.assertEqual(self.testNode1.rightNode, None)
        self.assertEqual(self.testNode1.parentNode, None)
        
        self.assertEqual(self.testNode2.key, 2)
        self.assertEqual(self.testNode2.color, qbr_dataStructures.Node.NodeColor.RED)
        self.assertEqual(self.testNode2.leftNode, None)
        self.assertEqual(self.testNode2.rightNode, None)
        self.assertEqual(self.testNode2.parentNode, None)
        
        self.assertEqual(self.testNode3.key, 3)
        self.assertEqual(self.testNode3.color, qbr_dataStructures.Node.NodeColor.BLACK)
        self.assertEqual(self.testNode3.leftNode, None)
        self.assertEqual(self.testNode3.rightNode, None)
        self.assertEqual(self.testNode3.parentNode, None)
        
    # Test that node comparison for equality works
    def test_node_equality(self):
        self.assertEqual(self.testNode1, self.testNode1)
        self.assertNotEqual(self.testNode1, self.testNode2)

    # Test that node comparison for inequality works
    def test_node_comparison(self):
        self.assertTrue(self.testNode1 < self.testNode2)
        self.assertTrue(self.testNode1 <= self.testNode2)
        self.assertTrue(self.testNode1 <= self.testNode1)
        self.assertTrue(self.testNode3 > self.testNode2)
        self.assertTrue(self.testNode3 >= self.testNode2)
        self.assertTrue(self.testNode3 >= self.testNode3)
        self.assertFalse(self.testNode1 > self.testNode2)
        self.assertFalse(self.testNode1 >= self.testNode2)
        self.assertFalse(self.testNode3 < self.testNode2)
        self.assertFalse(self.testNode3 <= self.testNode2)

    # Test that string represntation of node class works
    def test_node_string_representation(self):
        self.assertEqual(str(self.testNode1), "1")
        self.assertEqual(str(self.testNode2), "2")
        self.assertEqual(str(self.testNode3), "3")
    
    # test Node's getGrandparent()    
    def test_node_get_grandparent(self):
        self.assertEqual(self.testNode4.getGrandparent(), None)
        self.assertEqual(self.testNode5.getGrandparent(), None)
        self.assertEqual(self.testNode6.getGrandparent(), self.testNode4)
        self.assertEqual(self.testNode7.getGrandparent(), self.testNode4)
        self.assertEqual(self.testNode8.getGrandparent(), None)
     
    # test Node's getSibling()   
    def test_node_get_sibling(self):
        self.assertEqual(self.testNode4.getSibling(), None)
        self.assertEqual(self.testNode5.getSibling(), self.testNode8)
        self.assertEqual(self.testNode8.getSibling(), self.testNode5)
        self.assertEqual(self.testNode6.getSibling(), self.testNode7)
        self.assertEqual(self.testNode7.getSibling(), self.testNode6)
        
    def test_node_get_uncle(self):
        self.assertEqual(self.testNode4.getUncle(), None)
        self.assertEqual(self.testNode5.getUncle(), None)
        self.assertEqual(self.testNode6.getUncle(), self.testNode8)
        self.assertEqual(self.testNode7.getUncle(), self.testNode8)
        self.assertEqual(self.testNode8.getUncle(), None)

class TestBinarySearchTree(unittest.TestCase):
    # Build test BST
    # Final tree will look like the following:
    #                   5
    #                 /   \
    #               3       12
    #                     /    \
    #                   10      15
    #                 /           \
    #                7            18
    #                 \
    #                  9
    def setUp(self):
        self.bst = qbr_dataStructures.BinarySearchTree()
        for key in keys:
            self.bst.insert(key)

    # Test that keys were inserted correctly during build
    def test_insert(self):
        self.assertTrue(self.bst.root.key == keys[0])
        self.assertTrue(isBinarySearchTree(self.bst.root))
        self.assertEqual(levelOrderTraversal(self.bst.root), [[5],[3, 12],[10, 15],[7, 18],[9]])
        
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
        self.assertEqual(levelOrderTraversal(self.bst.root), [[5],[12],[10, 15],[7, 18],[9]])
        
        # remove node with two children
        self.bst.remove(10)
        self.assertTrue(isBinarySearchTree(self.bst.root))
        self.assertFalse(self.bst.search(10))
        self.assertEqual(levelOrderTraversal(self.bst.root), [[5],[12],[7, 15],[9, 18]])
        
        # remove node with one child
        self.bst.remove(7)
        self.assertTrue(isBinarySearchTree(self.bst.root))
        self.assertFalse(self.bst.search(7))
        self.assertEqual(levelOrderTraversal(self.bst.root), [[5],[12],[9, 15],[18]])
        
        # remove root
        self.bst.remove(5)
        self.assertTrue(isBinarySearchTree(self.bst.root))
        self.assertFalse(self.bst.search(5))
        self.assertEqual(levelOrderTraversal(self.bst.root), [[12],[9, 15],[18]])
    
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

class TestRedBlackTree(unittest.TestCase):
    # Build test RBT
    # Final tree will look like the following:
    #                   5
    #                 /   \
    #               3       12
    #                      /  \
    #                     9    15
    #                   /  \     \
    #                  7    10    18
    def setUp(self):
        self.rbt = qbr_dataStructures.RedBlackTree()
        for key in keys:
            self.rbt.insert(key)

    # Test that keys were inserted correctly during build
    def test_insert(self):
        self.assertTrue(self.rbt.root.key == keys[0])
        self.assertTrue(isBinarySearchTree(self.rbt.root))
        self.assertTrue(isRedBlackTree(self.rbt.root))
        self.assertEqual(levelOrderTraversal(self.rbt.root), [[5], 
                                                              [3, 12], 
                                                              [None, None, 9, 15], 
                                                              [7, 10, None, 18], 
                                                              [None, None, None, None, None, None]])
        
    # Test that search works correctly
    def test_search(self):
        for key in keys:
            self.assertTrue(self.rbt.search(key))
        for key in invalidKeys:
            self.assertFalse(self.rbt.search(key))
        
    # Test that key removal works correctly
    def test_delete(self):
        for key in invalidKeys:
            self.rbt.remove(key)
            self.assertTrue(isBinarySearchTree(self.rbt.root))
            self.assertFalse(self.rbt.search(key))
        
        # remove leaf
        self.rbt.remove(3)
        self.assertTrue(isBinarySearchTree(self.rbt.root))
        self.assertFalse(self.rbt.search(3))
        self.assertEqual(levelOrderTraversal(self.rbt.root), [[12],
                                                              [9, 15],
                                                              [5, 10, None, 18],
                                                              [None, 7, None, None, None, None],
                                                              [None, None]])
        
        # remove node with one child
        self.rbt.remove(5)
        self.assertTrue(isBinarySearchTree(self.rbt.root))
        self.assertFalse(self.rbt.search(5))
        self.assertEqual(levelOrderTraversal(self.rbt.root), [[12],
                                                              [9, 15],
                                                              [7, 10, None, 18],
                                                              [None, None, None, None, None, None]])
        
        # remove node with two children
        self.rbt.remove(9)
        self.assertTrue(isBinarySearchTree(self.rbt.root))
        self.assertFalse(self.rbt.search(9))
        self.assertEqual(levelOrderTraversal(self.rbt.root), [[12],
                                                              [10, 15],
                                                              [7, None, None, 18],
                                                              [None, None, None, None]])
        
        # remove root
        self.rbt.remove(12)
        self.assertTrue(isBinarySearchTree(self.rbt.root))
        self.assertFalse(self.rbt.search(12))
        self.assertEqual(levelOrderTraversal(self.rbt.root), [[15],
                                                              [10, 18],
                                                              [7, None, None, None],
                                                              [None, None]])
    
    # Test in-order traversal    
    def test_in_order_traversal(self):
        expected = '\n'.join(f'{key}' for key in sorted(set(keys)))
        # redirect output to 'result' object
        result = StringIO()
        sys.stdout = result
        self.rbt.inOrderTraversal()
        # directs output back to console for future use
        sys.stdout = sys.__stdout__
        self.assertEqual(result.getvalue().strip(), expected)

def node_test_suite():
    return unittest.TestSuite(tests=[
        TestNode("test_node_constructor"),
        TestNode("test_node_equality"),
        TestNode("test_node_comparison"),
        TestNode("test_node_string_representation"),
        TestNode("test_node_get_grandparent"),
        TestNode("test_node_get_sibling"),
        TestNode("test_node_get_uncle")
    ])
    
def binarySearchTree_test_suite():
    return unittest.TestSuite(tests=[
        TestBinarySearchTree("test_insert"),
        TestBinarySearchTree("test_search"),
        TestBinarySearchTree("test_delete"),
        TestBinarySearchTree("test_in_order_traversal")
    ])
    
def redBlackTree_test_suite():
    return unittest.TestSuite(tests=[
        TestRedBlackTree("test_insert"),
        TestRedBlackTree("test_search"),
        TestRedBlackTree("test_delete"),
        TestRedBlackTree("test_in_order_traversal")
    ])
    
if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    print(f"\nNode tests")
    runner.run(node_test_suite())
    print(f"\nBinary Search Tree tests")
    runner.run(binarySearchTree_test_suite())
    print(f"\nRed Black Tree tests")
    runner.run(redBlackTree_test_suite())