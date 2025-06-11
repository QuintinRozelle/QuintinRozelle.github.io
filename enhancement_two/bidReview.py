#=======================================================================================
# Name        : bidReview.py
# Author      : Quintin B. Rozelle
# Version     : 2.0
# Date        : 2025-05-24
# Description : Conversion of BinarySearchTree.cpp to Python for Enhancement 2 in CS-499
#               Contains Bid class and implementation of user interaction
#=======================================================================================

from typing import NoReturn, NewType
import qbr_dataStructures
import csv
import datetime

RedBlackTree = NewType('RedBlackTree', qbr_dataStructures.RedBlackTree)
Bid = NewType('Bid', 'Bid')
Node = NewType('Node', 'qbr_dataStructures.Node')

class Bid:
    """
    Bid class for storing imported bid data
    
    Attributes
    ----------
    bidId: int
        Unique identifier for Bid
    title: str
        Name of item bid upon
    fund: str
        Name of fund that the money from the sale goes to (e.g., 'General Fund', 'Enterprise', etc.)
    bidAmount: float
        Amount of winning bid
    """
    
    def __init__(self, bidId: int, title: str, fund: str, bidAmount: float) -> NoReturn:
        """
        Initialize a new bid with the given attributes
        
        Parameters
        ----------
        bidId: int
            Unique identifier for Bid
        title: str
            Name of item bid upon
        fund: str
            Name of fund that the money from the sale goes to (e.g., 'General Fund', 'Enterprise', etc.)
        bidAmount: float
            Amount of winning bid
        """
        self.bidId : int = bidId
        self.title : str = title
        self.fund : str = fund
        self.bidAmount : float = bidAmount
    
    # Comparitor methods for Bid class    
    def __eq__(self, other: Bid):
        """
        Compares two bids for equality based on their bidIds
        
        Parameters
        ----------
        other: Bid
            Second bid to compare with
        
        Returns
        -------
        bool
            True if the bidIds are equal, False otherwise        
        """
        if isinstance(other, Bid):
            return self.bidId == other.bidId
        return False
    
    def __lt__(self, other: Bid):
        """
        Compares two bids for less than inequality based on their bidIds
        
        Parameters
        ----------
        other: Bid
            Second bid to compare with
            
        Returns
        -------
        bool
            True if the first bid's bidId is less than the second bid's bidId, False otherwise
        """
        if isinstance(other, Bid):
            return self.bidId < other.bidId
        return False
    
    def __gt__(self, other):
        """
        Compares two bids for greater than inequality based on their bidIds
        
        Parameters
        ----------
        other: bid
            Second bid to compare with
            
        Returns
        -------
        bool
            True if the first bid's bidId is greater than the second bid's bidId, False otherwise
        """
        if isinstance(other, Bid):
            return self.bidId > other.bidId
        return False
    
    def __str__(self):
        """
        Returns a string representation of the bid
        
        Returns
        -------
        str
            A string representation of the bid
        """
        return f"{self.bidId} | {self.title} | {self.fund} | {self.bidAmount}"

class FileFormatError(Exception):
    """
    Custom exception for handling incorrectly formatted file
    """
   
def loadBids(csvPath: str) -> RedBlackTree:
    """
    Loads bid data from a csv to the red black tree in memory
    
    Parameters
    ----------
    csvPath : str
        Relative path of CSV file to load
        
    Returns
    -------
    RedBlackTree
        A red black tree loaded with the data from the csv file
    """
    print('Loading CSV file:', csvPath)
    rbt = qbr_dataStructures.RedBlackTree()
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
                rowNumber = 1
                for row in csvReader:
                    if rowNumber == 1:
                        bidIdColumn = row.index('Auction ID')
                        titleColumn = row.index('Auction Title')
                        fundColumn = row.index('Fund')
                        bidAmountColumn = row.index('Winning Bid')
                        rowNumber = rowNumber + 1
                    else:
                        rbt.insert(Bid(int(row[bidIdColumn]),
                                       row[titleColumn],
                                       row[fundColumn],
                                       float((row[bidAmountColumn][1:]).replace(',','')))) #strip initial $ sign and convert to float
    except Exception as error:
        print("Error loading file")
        print(f"Error type: {type(error)}")
        print(f"Error message: {error}")
    finally:
        return rbt
    
def displayMainMenu() -> int:
    """
    Displays the main menu and returns the user's choice
    
    Returns
    -------
    int
        The user's choice
    """
    choice : str = "0"
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

def displayLoadMenu(rbtRoot : Node) -> int:
    """
    Displays the load file menu and returns the user's choice
    
    Parameters
    ----------
    Node
        The root of the RBT. Used to check if RBT is already laoded with data
    
    Returns
    -------
    int
        The user's choice
    """
    if rbtRoot is not None:
        choice : str = "0"
        while choice == "0":
            print("A file has already been loaded. What would you like to do?")
            print("  1. Clear red black tree and load new file")
            print("  2. Add contents of new file to current red black tree")
            print("  3. Cancel and return to main menu")
            choice = input("Enter choice: ")
            
            if choice in ["1", "2", "3"]:
                return int(choice)
            else:
                print("Invalid choice. Please try again")
                choice = "0"
    else:
        return 2
    
if __name__ == '__main__':
    rbt : qbr_dataStructures = qbr_dataStructures.RedBlackTree()
    choice : int = 0
    while (choice != 9):
        choice = displayMainMenu()
    
        match choice:
            # Load file
            case 1:
                loadChoice : int = displayLoadMenu(rbt.root)
                # load file
                if loadChoice in [1,2]:
                    # clear bst then load file
                    if loadChoice == 1:
                        rbt.root = None
                    csvFile : str = input("Enter name of file to load: ")
                    time1 = datetime.datetime.now()
                    rbt = loadBids(csvFile)
                    time2 = datetime.datetime.now()
                    print (f'Total load time: {time2 - time1}')
                elif loadChoice == 3:
                    pass
            # Display all bids
            case 2:
                time1 = datetime.datetime.now()
                rbt.inOrderTraversal()
                time2 = datetime.datetime.now()
                print (f'Total print time: {time2 - time1}')
            # Search for bid
            case 3:
                searchedBidId : str = input("Please enter ID to search for: ")
                searchedBid = Bid(int(searchedBidId), None, None, None)
                time1 = datetime.datetime.now()
                print(rbt.search(searchedBid))
                time2 = datetime.datetime.now()
                print (f'Total search time: {time2 - time1}')
            # Remove a bid
            case 4:
                searchedBidId : str = input("Please enter ID to remove: ")
                searchedBid = Bid(int(searchedBidId), None, None, None)
                time1 = datetime.datetime.now()
                rbt.remove(searchedBid)
                time2 = datetime.datetime.now()
                print (f'Total removal time: {time2 - time1}')
    print("Good bye")
            