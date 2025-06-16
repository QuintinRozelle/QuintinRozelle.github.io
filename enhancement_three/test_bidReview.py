#=======================================================================================
# Name        : test_bidReview.py
# Author      : Quintin B. Rozelle
# Version     : 3.0
# Date        : 2025-06-02
# Description : Test of bidReview module
#=======================================================================================

import unittest
import bidReview
import bidDatabase
import csv
import sys
import io
import os

class TestBid(unittest.TestCase):
    # Setup database for tests
    def setUp(self):
        self.testDatabaseName: str = 'test_bidDatabase.sqlite'
        if os.path.exists(self.testDatabaseName):
            os.remove(self.testDatabaseName)
            
        self.testDatabase: bidDatabase.BidDatabase = bidDatabase.BidDatabase(self.testDatabaseName)
        self.testTable: str = 'bids'
        self.testDatabase.createTable(self.testTable,
                                      {
                                          'auctionID': 'INTEGER PRIMARY KEY NOT NULL',
                                          'auctionTitle': 'TEXT NOT NULL',
                                          'fund': 'TEXT NOT NULL',
                                          'winningBid': 'FLOAT NOT NULL'
                                      })
        
        self.expectedOutput = io.StringIO()
        sys.stdout = self.expectedOutput
    
    # Test loadBids function    
    def test_load_bids(self):
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
            bidReview.loadBids('test_bidReviewGood.csv', self.testDatabase)
            self.testDatabase.readRecords(self.testTable)
            self.assertEqual(self.expectedOutput.getvalue().strip(), "Loading CSV file: test_bidReviewGood.csv\nRecords added successfully\nRecords found\n(1, 'Title1', 'Fund1', 1.0)\n(2, 'Title2', 'Fund2', 2000.0)\n(3, 'Title3', 'Fund3', 3.0)\n(4, 'Title4', 'Fund4', 4.0)")
        except Exception as e:
            self.fail(f"loadBids raised an exception on \"good\" CSV file: {e}")
        
if __name__ == '__main__':
    unittest.main(verbosity=2)