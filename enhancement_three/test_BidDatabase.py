#=======================================================================================
# Name        : test_bidDatabase.py
# Author      : Quintin B. Rozelle
# Version     : 1.0
# Date        : 2025-06-01
# Description : Test of bidDatabase module
#=======================================================================================

import unittest
import bidDatabase
import os
import io
import sys
import sqlite3

class TestBidDatabase(unittest.TestCase):
    databaseName: str = 'test_bidDatabase.sqlite'
    tableName: str = 'testTable'
    updatedTableName: str = 'updatedTable'

    testDatabase: bidDatabase.BidDatabase = None
    databaseCreationMessage: io.StringIO = io.StringIO()
    expectedOutput: io.StringIO = None
    cursor: sqlite3.Cursor = None
    
    @classmethod
    def setUpClass(cls):
        
        # Remove test database from prior testing to start fresh
        if os.path.exists(cls.databaseName):
            os.remove(cls.databaseName)

        # Redirect output for database creation
        sys.stdout = cls.databaseCreationMessage
        
        #create fresh database for testing
        cls.testDatabase = bidDatabase.BidDatabase(cls.databaseName)
        cls.cursor = cls.testDatabase.connection.cursor()
        
    def setUp(self):
        # Create new StringIO output for all tests
        self.expectedOutput = io.StringIO()
        sys.stdout = self.expectedOutput
    
    @classmethod    
    def tearDownClass(cls):
        # Redirect output to default
        sys.stdout = sys.__stdout__
    
    # Test database creation
    def test_create_database(self):
        self.assertEqual(self.databaseCreationMessage.getvalue().strip(), 'Connected to database successfully')
        
    # Test table creation
    def test_create_table(self):
        tableCols: dict[str, str] = {'id': 'INTEGER PRIMARY KEY AUTOINCREMENT',
                                     'col1': 'TEXT',
                                     'col2': 'INTEGER'}        
        self.testDatabase.createTable(self.tableName, tableCols)
        
        # Check that table created successfully
        self.assertEqual(self.expectedOutput.getvalue().strip(), 'Table created successfully')
        queryString = f"SELECT EXISTS(SELECT 1 FROM sqlite_master WHERE type='table' AND name='{self.tableName}');"
        self.cursor.execute(queryString)
        self.assertEqual(self.cursor.fetchone()[0], 1)
        
        # Check that columns are correct
        self.cursor.execute(f'PRAGMA table_info({self.tableName})')
        columns: dict[str, str] = {row[1]: row[2] for row in self.cursor.fetchall()}
        for columnName, columnType in columns.items():
            self.assertTrue(columnName in ('id', 'col1', 'col2'))
            self.assertEqual(columnType, {'id': 'INTEGER', 'col1': 'TEXT', 'col2': 'INTEGER'}[columnName])
            
    # Test table name update
    def test_update_table_name(self):
        self.testDatabase.updateTableName(self.tableName, self.updatedTableName)
        self.assertEqual(self.expectedOutput.getvalue().strip(), 'Table renamed successfully')
        queryString = f"SELECT EXISTS(SELECT 1 FROM sqlite_master WHERE type='table' AND name='{self.updatedTableName}');"
        self.cursor.execute(queryString)
        self.assertEqual(self.cursor.fetchone()[0], 1)
        # Rename table back to original for other tests
        self.testDatabase.updateTableName(self.updatedTableName, self.tableName)
        
    # Test adding column to table
    def test_add_table_column(self):
        self.testDatabase.addTableColumn(self.tableName, 'colC', 'TEXT')
        self.assertEqual(self.expectedOutput.getvalue().strip(), 'New column added successfully')
         # Check that columns are correct
        self.cursor.execute(f'PRAGMA table_info({self.tableName})')
        columns: dict[str, str] = {row[1]: row[2] for row in self.cursor.fetchall()}
        for columnName, columnType in columns.items():
            self.assertTrue(columnName in ('id', 'col1', 'col2', 'colC'))
            self.assertEqual(columnType, {'id': 'INTEGER', 'col1': 'TEXT', 'col2': 'INTEGER', 'colC': 'TEXT'}[columnName])

    # Test updating a column name
    def test_update_table_column_name(self):
        self.testDatabase.updateTableColumnName(self.tableName, 'colC', 'col3')
        self.assertEqual(self.expectedOutput.getvalue().strip(), 'Column renamed successfully')
         # Check that columns are correct
        self.cursor.execute(f'PRAGMA table_info({self.tableName})')
        columns: dict[str, str] = {row[1]: row[2] for row in self.cursor.fetchall()}
        for columnName, columnType in columns.items():
            self.assertTrue(columnName in ('id', 'col1', 'col2', 'col3'))
            self.assertEqual(columnType, {'id': 'INTEGER', 'col1': 'TEXT', 'col2': 'INTEGER', 'col3': 'TEXT'}[columnName])
            
    # Test deleting a table
    def test_delete_table(self):
        self.testDatabase.deleteTable(self.tableName)
        self.assertEqual(self.expectedOutput.getvalue().strip(), 'Table deleted successfully')
        queryString = f"SELECT EXISTS(SELECT 1 FROM sqlite_master WHERE type='table' AND name='{self.tableName}');"
        self.cursor.execute(queryString)
        self.assertEqual(self.cursor.fetchone()[0], 0)
        
    # Test singular record creation
    def test_create_record(self):
        self.testDatabase.createRecord(self.tableName, ('col1', 'col2', 'col3'), ('test1.1', 1, 'test1.3'))
        self.assertEqual(self.expectedOutput.getvalue().strip(), 'Record added successfully')
        
    # Test singular record creation with duplicates found
    def test_create_record_duplicates(self):
        self.testDatabase.createRecord(self.tableName, ('id', 'col1', 'col2', 'col3'), (1, '1000', 1, 'test1.3'), True)
        self.testDatabase.createRecord(self.tableName, ('id', 'col1', 'col2', 'col3'), (1, 'test1.1', 1000, 'test1.3'), False)
        self.assertEqual(self.expectedOutput.getvalue().strip(), 'Record added successfully\nRecord added successfully')
    
    # Test multiple record creation    
    def test_create_records(self):
        self.testDatabase.createRecords(self.tableName, ('col1', 'col2', 'col3'), (('test2.1', 2, 'test2.3'),('test3.1', 3, 'test3.3')))
        self.assertEqual(self.expectedOutput.getvalue().strip(), 'Records added successfully')
        
    # Test multiple record creation with duplicates found
    def test_create_records_duplicates(self):
        self.testDatabase.createRecords(self.tableName, ('id', 'col1', 'col2', 'col3'), ((3, '3000', 3, 'test3.3'),(4, 'test4.1', 4, 'test4.3')), True)
        self.testDatabase.createRecords(self.tableName, ('id', 'col1', 'col2', 'col3'), ((3, 'test3.1', 3000, 'test3.3'),(5, 'test5.1', 5, 'test5.3')), False)
        self.assertEqual(self.expectedOutput.getvalue().strip(), 'Records added successfully\nRecords added successfully')
        
    # Test reading all records
    def test_read_records(self):
        self.testDatabase.readRecords(self.tableName)
        self.assertEqual(self.expectedOutput.getvalue().strip(), f"Records found\n(1, 'test1.1', 1000, 'test1.3')\n(2, 'test2.1', 2, 'test2.3')\n(3, 'test3.1', 3000, 'test3.3')\n(4, 'test4.1', 4, 'test4.3')\n(5, 'test5.1', 5, 'test5.3')")
        
    # Test reading one record
    def test_read_record(self):
        self.testDatabase.readRecord(self.tableName, 'id', 3)
        self.assertEqual(self.expectedOutput.getvalue().strip(), f"Record found\n(3, 'test3.1', 3000, 'test3.3')")
        
    # Test updating a record
    def test_update_record(self):
        self.testDatabase.updateRecord(self.tableName, 'id', 4, {'col1': 'updatedValue', 'col2': 4000})
        self.testDatabase.readRecord(self.tableName, 'id', 4)
        self.assertEqual(self.expectedOutput.getvalue().strip(), f"Record updated\nRecord found\n(4, 'updatedValue', 4000, 'test4.3')")

    # Test deleting a record        
    def test_delete_record(self):
        self.testDatabase.deleteRecord(self.tableName, 'id', 4)
        self.testDatabase.readRecords(self.tableName)
        self.assertEqual(self.expectedOutput.getvalue().strip(), f"Record deleted\nRecords found\n(1, 'test1.1', 1000, 'test1.3')\n(2, 'test2.1', 2, 'test2.3')\n(3, 'test3.1', 3000, 'test3.3')\n(5, 'test5.1', 5, 'test5.3')")

def bidDatabase_test_suite():
    return unittest.TestSuite(tests=[
        TestBidDatabase('test_create_database'),
        TestBidDatabase('test_create_table'),
        TestBidDatabase('test_update_table_name'),
        TestBidDatabase('test_add_table_column'),
        TestBidDatabase('test_update_table_column_name'),
        TestBidDatabase('test_create_record'),
        TestBidDatabase('test_create_record_duplicates'),
        TestBidDatabase('test_create_records'),
        TestBidDatabase('test_create_records_duplicates'),
        TestBidDatabase('test_read_records'),
        TestBidDatabase('test_read_record'),
        TestBidDatabase('test_update_record'),
        TestBidDatabase('test_delete_record'),
        TestBidDatabase('test_delete_table')
    ])        
        
if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(bidDatabase_test_suite())