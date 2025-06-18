#=======================================================================================
# Name        : BinarySearchTree.py
# Author      : Quintin B. Rozelle
# Version     : 1.0
# Date        : 2025-05-16
# Description : Test of bidReview module
#=======================================================================================

import unittest
import bidReview
import binarySearchTree
import csv

class TestBid(unittest.TestCase):
    # Setup bids for tests
    def setUp(self):
        self.bid1 = bidReview.Bid(1, "Bid 1", "General Fund", 1000)
        self.bid2 = bidReview.Bid(2, "Bid 2", "Enterprise", 2000)
        self.bid3 = bidReview.Bid(3, "Bid 3", "General Fund", 1500)
        self.node1 = binarySearchTree.Node(self.bid1)
        self.node2 = binarySearchTree.Node(self.bid2)
        self.node3 = binarySearchTree.Node(self.bid3)

    # Test that bid comparison for equality works
    def test_bid_equality(self):
        self.assertEqual(self.bid1, bidReview.Bid(1, "Bid 1", "General Fund", 1000))
        self.assertEqual(self.bid1, bidReview.Bid(1, "Bid1", "Enterprise", 1400))
        self.assertNotEqual(self.bid1, self.bid2)

    # Test that bid comparison for lest than and greater than inequality works
    def test_bid_comparison(self):
        self.assertTrue(self.bid1 < self.bid2)
        self.assertTrue(self.bid3 > self.bid2)
        self.assertFalse(self.bid1 > self.bid2)
        self.assertFalse(self.bid3 < self.bid2)
        self.assertFalse(self.bid1 > 2)
        self.assertFalse(self.bid1 < 2)

    # Test that string represntation of bid class works
    def test_bid_string_representation(self):
        self.assertEqual(str(self.bid1), "1 | Bid 1 | General Fund | 1000")
        self.assertEqual(str(self.bid2), "2 | Bid 2 | Enterprise | 2000")
        self.assertEqual(str(self.bid3), "3 | Bid 3 | General Fund | 1500")
    
    # Test that comparison for equality for a bid stored in a node works
    def test_bid_in_node_equality(self):
        self.assertEqual(self.node1, binarySearchTree.Node(bidReview.Bid(1, "Bid 1", "General Fund", 1000)))
        self.assertEqual(self.node1, binarySearchTree.Node(bidReview.Bid(1, "Bid1", "Enterprise", 1400)))
        self.assertNotEqual(self.node1, self.node2)
        
    # Test that bid comparison for lest than and greater than inequality works
    def test_bid_in_node_comparison(self):
        self.assertTrue(self.node1 < self.node2)
        self.assertTrue(self.node3 > self.node2)
        self.assertFalse(self.node1 > self.node2)
        self.assertFalse(self.node3 < self.node2)
        self.assertFalse(self.node1 > self.bid2)
        self.assertFalse(self.node1 < self.bid2)

    # Test that string represntation of bid class works
    def test_bid_in_node_string_representation(self):
        self.assertEqual(str(self.node1), "1 | Bid 1 | General Fund | 1000")
        self.assertEqual(str(self.node2), "2 | Bid 2 | Enterprise | 2000")
        self.assertEqual(str(self.node3), "3 | Bid 3 | General Fund | 1500")
    
    # Test loadBids function    
    def test_load_bids(self):
        bst = binarySearchTree.BinarySearchTree()
        
        # Create and use a working CSV file
        with open('test_bidReviewGood.csv', 'w', newline='') as csvfile:
            testCsvWriter = csv.writer(csvfile)
            testCsvWriter.writerow(['Auction ID', 'Auction Title', 'Fund', 'Winning Bid'])
            testCsvWriter.writerow([2, 'Title2', 'Fund2', '$2,000.00'])
            testCsvWriter.writerow([4, 'Title4', 'Fund4', '$4'])
            testCsvWriter.writerow([3, 'Title3', 'Fund3', '$3'])
            testCsvWriter.writerow([1, 'Title1', 'Fund1', '$1'])
        # Test that bids are loaded correctly and that errors aren't thrown
        try:
            bst = bidReview.loadBids('test_bidReviewGood.csv')
            self.assertEqual(str(bst.root.key), "2 | Title2 | Fund2 | 2000.0")
        except Exception as e:
            self.fail(f"loadBids raised an exception on \"good\" CSV file: {e}")
        
if __name__ == '__main__':
    unittest.main(verbosity=2)
