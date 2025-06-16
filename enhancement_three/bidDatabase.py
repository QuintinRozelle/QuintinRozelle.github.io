#=======================================================================================
# Name        : bidDatabase.py
# Author      : Quintin B. Rozelle
# Version     : 1.0
# Date        : 2025-06-02
# Description : SQLite CRUD API used with bidReview.py
#=======================================================================================

import sqlite3
import typing

class BidDatabase:
    """
    Class for interacting with the SQLite database
    
    Attributes
    ----------
    connection: sqlite3.Connection
        The connection to the database
    cursor: sqlite3.Cursor
        A cursor used to interact with the database
    """
    def __init__(self, fileName: str) -> None:
        """
        Initializer for the BidDatabase class. Creates a connection to the database
        
        Parameters
        ----------
        fileName: str
            The relative path to the SQLite database to connect to
        """
        try:
            self.connection: sqlite3.Connection = sqlite3.connect(fileName)
            self.cursor: sqlite3.Cursor = self.connection.cursor()
            print(f'Connected to database successfully')
        except sqlite3.Error as error:
            print(f'Error encountered: {error}')
        
    def _runQuery(self, query: str, message: str | None = None) -> None:
        """
        A helper function to run query strings. Not meant to be called on it's own
        
        Parameters
        ----------
        query: str
            The query string to run
        message: str | None (optional)
            Custom message to display upon successfully running the query string.
            If None, will not display a message (default is None)
        """
        try:
            self.cursor.execute(query)
            self.connection.commit()
            if message:
                print(message)
        except sqlite3.Error as error:
            print(f'Error encountered: {error}')
            print(f'    Encounted while performing: {query}')

            
    def _readQuery(self, query: str, message: str | None = None) -> list[tuple]:
        """
        A helper function to run read query strings. Not meant to be called on it's own
        
        Parameters
        ----------
        query: str
            The query string to run
        message: str | None (optional)
            Custom message to display upon successfully running the query string.
            If None, will not display a message (default is None)
            
        Returns
        -------
        list[tuple]
            The found records after running the read query string
        """
        records: list[tuple] = None
        try:
            self.cursor.execute(query)
            records: list[any] = self.cursor.fetchall()
            if message:
                print(message)
            return records
        except sqlite3.Error as error:
            print(f'Error encountered: {error}')
            print(f'    Encounted while performing: {query}')
    
    ############################
    # Table based CRUD functions
    ############################        
    def createTable(self, tableName: str, tableCols: dict[str, str]) -> None:
        """
        Creates a table in the database if it doesn't already exist
        
        Parameters
        ----------
        tableName: str
            Name of the table to create
        tableCols: dict[str, str]
            The names and attributes of the table to add. Must be a dictionary where the
            keys are the column names and the values are the respective column attributes
                E.g., {'ID': 'INTERGER PRIMARY KEY AUTOINCREMENT',
                    'First Name': 'TEXT NOT NULL',
                    'Last Name': 'TEXT NOT NULL'}
        """
        # Build the query string
        queryHeader: str = f'CREATE TABLE IF NOT EXISTS {tableName} ('
        queryBody: str = None
        queryFooter: str = f');'
        for colName, colProperty in tableCols.items():
            queryBody = f'{queryBody}, {colName} {colProperty}'
        # Remove the initial 'None ,' from queryBody
        queryBody = queryBody[6:]
        queryString: str = queryHeader + queryBody + queryFooter
        self._runQuery(queryString, 'Table created successfully')
        
    def updateTableName(self, oldTableName: str, newTableName: str) -> None:
        """
        Updates a table's name
        
        Parameters
        ----------
        oldTableName: str
            The name of the table to rename
        newTableName: str
            The table's new name
        """
        queryString: str = f'ALTER TABLE {oldTableName} RENAME TO {newTableName}'
        self._runQuery(queryString, 'Table renamed successfully')
    
    def addTableColumn(self, tableName: str, newColName: str, newColType: str) -> None:
        """
        Adds a column to the table
        
        Parameters
        ----------
        tableName: str
            The name of the table to add a column to
        newColName: str
            The name of the column to add
        newColType: str
            The attributes of the new column
        """
        queryString: str = f'ALTER TABLE {tableName} ADD COLUMN {newColName} {newColType}'
        self._runQuery(queryString, 'New column added successfully')
        
    def updateTableColumnName(self, tableName: str, oldColName: str, newColName: str) -> None:
        """
        Updates a column name
        
        Parameters
        ----------
        tableName: str
            The name of the tabel that contains the column to update
        oldColName: str
            The name of the columnt to rename
        newColName: str
            The column's new name
        """
        queryString: str = f'ALTER TABLE {tableName} RENAME COLUMN {oldColName} TO {newColName}'
        self._runQuery(queryString, 'Column renamed successfully')
        
    def deleteTable(self, tableName: str) -> None:
        """
        Deletes a table from the database
        
        Parameters
        ----------
        tableName: str
            The name of the table to delete
        """
        queryString: str = f'DROP TABLE IF EXISTS {tableName}'
        self._runQuery(queryString, 'Table deleted successfully')
    
    #############################
    # Record based CRUD functions
    #############################    
    def createRecord(self, tableName: str, tableCols: tuple[str], record: tuple[typing.Any], ignoreDuplicates: bool = True) -> None:
        """
        Creates a singular record
        
        Parameters
        ----------
        tableName: str
            The name of the table to add a record to
        tableCols: tuple[str]
            The columns to add values to
        record: tuple[Any]
            The values of the record to add. Must line up with the values in tableCols
        ignoreDuplicates: bool (optional)
            Defines what to do if duplicates are found (default is True):
                True: Don't add record when the key is already in the table
                False: Update the record if the key is already in the table
        """
        queryString: str = f'INSERT OR {"IGNORE" if ignoreDuplicates else "REPLACE"} INTO {tableName} {tableCols} VALUES {record};'
        self._runQuery(queryString, 'Record added successfully')
        
    def createRecords(self,
                      tableName: str,
                      tableCols: tuple[str],
                      records: tuple[tuple[typing.Any]] | list[tuple[typing.Any]],
                      ignoreDuplicates: bool = True) -> None:
        """
        Creates multiple records
        
        Parameters
        ----------
        tableName: str
            The name of the table to add records to
        tableCols: tuple[str]
            The columns to add values to
        record: tuple[tuple[Any]] | list[tuples[Any]]
            The values of the records to add. Must line up with the values in tableCols
        ignoreDuplicates: bool (optional)
            Defines what to do if duplicates are found (default is True):
                True: Don't add record when the key is already in the table
                False: Update the record if the key is already in the table
        """
        # Build the query string
        queryHeader: str = f'INSERT OR {"IGNORE" if ignoreDuplicates else "REPLACE"} INTO {tableName} {tableCols} VALUES'
        queryBody: str = None
        for record in records:
            queryBody = f'{queryBody}, {record}'
        # Remove the initial 'None ,' from queryBody
        queryBody = queryBody[6:]
        queryString: str = queryHeader + queryBody
        self._runQuery(queryString, 'Records added successfully')
        
    def readRecords(self, tableName: str) -> None:
        """
        Reads and displays all the records in a specific table
        
        Parameters
        ----------
        tableName: str
            The table whose records will be displayed
        """
        queryString: str = f'SELECT * FROM {tableName};'
        records = self._readQuery(queryString, 'Records found')
        for record in records:
            print(record)
        
    def readRecord(self, tableName: str, keyName: str, id: typing.Any) -> None:
        """
        Reads and displays a singular record
        
        Parameters
        ----------
        tableName: str
            The name of the table to search
        keyName: str
            The name of the column containing the keys
        id: Any
            The key to find and display
        """
        queryString: str = f'SELECT * FROM {tableName} WHERE {keyName} = {id}'
        record = self._readQuery(queryString, 'Record found')
        # Display the first record in the tuple. Removes the brackets from the display
        print(record[0])
        
    def updateRecord(self, tableName: str, keyName: str, id: int, updates: dict[str, typing.Any]) -> None:
        """
        Update a specific record
        
        Parameters
        ----------
        tableName:
            The name of the table that contains the record to update
        keyName: str
            The name of the column containing the keys
        id: Any
            The key to find and update
        updates: dict[str, Any]
            The updated values. Must be a dictionary where the keys are the column names
            and the values are the respective updates
        """
        # Build the query string
        queryHeader: str = f'UPDATE {tableName} SET '
        queryBody: str = None
        queryFooter: str = f' WHERE {keyName} = {id}'
        for colName, value in updates.items():
            queryBody = f'{queryBody}, {colName} = "{value}"'
        # Remove the initial 'None ,' from queryBody
        queryBody = queryBody[6:]
        queryString: str = queryHeader + queryBody + queryFooter
        self._runQuery(queryString, 'Record updated')
        
    def deleteRecord(self, tableName: str, keyName: str, id: int) -> None:
        """
        Deletes a record from a table
        
        Parameters
        ----------
        tableName: str
            The name of the table that contains the record to delete
        keyName: str
            The name of the column containing the keys
        id: Any
            The key to find and delete
        """
        queryString: str = f'DELETE FROM {tableName} WHERE {keyName} = {id}'
        self._runQuery(queryString, 'Record deleted')