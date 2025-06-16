#=======================================================================================
# Name        : bidReview.py
# Author      : Quintin B. Rozelle
# Version     : 3.0
# Date        : 2025-06-02
# Description : Conversion of BinarySearchTree.cpp to Python for Enhancement 3 in CS-499
#               Contains Bid class, implementation of user interaction, and utilization
#               of sqlite database
#=======================================================================================

import typing
import bidDatabase
import csv
import datetime

class FileFormatError(Exception):
    """
    Custom exception for handling incorrectly formatted file
    """
   
def loadBids(csvPath: str, database: bidDatabase.BidDatabase, ignoreDuplicates: bool = True) -> None:
    """
    Loads bid data from a csv to the SQLite database
    
    Parameters
    ----------
    csvPath: str
        Relative path of CSV file to load
    ignoreDuplicates: bool
        Flag to ignore duplicates in database if True (default is True)
    """
    print('Loading CSV file:', csvPath)
    try:
        with open(csvPath) as csvFile:
            # detects csv dialect and presence of header
            dialect = csv.Sniffer().sniff(csvFile.read(1024))
            csvFile.seek(0)
            headerPresent = csv.Sniffer().has_header(csvFile.read(1024))
            csvFile.seek(0)
            csvReader = csv.reader(csvFile, dialect)
            # check for presence of header
            if not headerPresent:
                raise FileFormatError("No header found in CSV file")
            else:
                records: list[tuple[typing.Any]] = list()
                for rowNumber, row in enumerate(csvReader):
                    # Find important columns
                    if rowNumber == 0:
                        bidIdColumn = row.index('Auction ID')
                        titleColumn = row.index('Auction Title')
                        fundColumn = row.index('Fund')
                        bidAmountColumn = row.index('Winning Bid')
                    else:
                        # Create list of records to add. Strip entries of "'" and strip initial $ sign from currency and convert to float to prevent errors
                        record: tuple[typing.Any] = (int(row[bidIdColumn]),
                                                     row[titleColumn].replace("'", ''),
                                                     row[fundColumn].replace("'", ''),
                                                     float((row[bidAmountColumn][1:]).replace(',','')))
                        records.append(record)
                database.createRecords('bids', ('auctionID', 'auctionTitle', 'fund', 'winningBid'), records, ignoreDuplicates)
    except Exception as error:
        print("Error loading file")
        print(f"Error type: {type(error)}")
        print(f"Error message: {error}")
    
def displayMainMenu() -> int:
    """
    Displays the main menu and returns the user's choice
    
    Returns
    -------
    int
        The user's choice
    """
    choice: str = "0"
    while choice == "0":
        print("Menu:")
        print("  1. Load Bids")
        print("  2. Display All Bids")
        print("  3. Find Bid")
        print("  4. Remove Bid")
        print("  9. Exit")
        choice = input("Enter choice: ")
        
        if choice in ["1", "2", "3", "4", "9"]:
            return int(choice)
        else:
            print("Invalid choice. Please try again")
            choice = "0"

def displayLoadMenu() -> int:
    """
    Displays the load file menu and returns the user's choice
    
    Returns
    -------
    int
        The user's choice
    """
    choice: str = "0"
    while choice == "0":
        print("How would you like to handle any duplicate entries?")
        print("  1. Ignore potential duplicates in load file")
        print("  2. Replace duplicates in database with records from load file")
        print("  3. Neither. Cancel and return to main menu")
        choice = input("Enter choice: ")
        
        if choice in ["1", "2", "3"]:
            return int(choice)
        else:
            print("Invalid choice. Please try again")
            choice = "0"
    
if __name__ == '__main__':
    database: bidDatabase.BidDatabase = bidDatabase.BidDatabase('bidDatabase.sqlite')
    database.createTable('bids',
                         {   'auctionID': 'INTEGER PRIMARY KEY NOT NULL',
                             'auctionTitle': 'TEXT NOT NULL',
                             'fund': 'TEXT NOT NULL',
                             'winningBid': 'FLOAT NOT NULL'})
    choice: int = 0
    time1: datetime.datetime = None
    time2: datetime.datetime = None
    while (choice != 9):
        try:
            choice = displayMainMenu()
        
            match choice:
                # Load file
                case 1:
                    loadChoice: int = displayLoadMenu()
                    if loadChoice in [1, 2]:
                        csvFile: str = input("Enter name of file to load: ")
                        time1 = datetime.datetime.now()
                        loadBids(csvFile, database, True if loadChoice == 1 else False)
                        time2 = datetime.datetime.now()
                        print (f'Total load time: {time2 - time1}')
                    # Choice 3: Cancel and return to main
                    else:
                        pass
                # Display all bids
                case 2:
                    time1 = datetime.datetime.now()
                    database.readRecords('bids')
                    time2 = datetime.datetime.now()
                    print (f'Total print time: {time2 - time1}')
                # Search for bid
                case 3:
                    searchedBid: int = int(input("Please enter ID to search for: "))
                    time1 = datetime.datetime.now()
                    database.readRecord('bids', 'auctionID', searchedBid)
                    time2 = datetime.datetime.now()
                    print (f'Total search time: {time2 - time1}')
                # Remove a bid
                case 4:
                    searchedBid: int = int(input("Please enter ID to remove: "))
                    time1 = datetime.datetime.now()
                    database.deleteRecord('bids', 'auctionID', searchedBid)
                    time2 = datetime.datetime.now()
                    print (f'Total removal time: {time2 - time1}')
        except Exception as error:
            print(f'Error encountered: {error}')
    print("Good bye")
            