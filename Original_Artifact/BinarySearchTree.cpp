//============================================================================
// Name        : BinarySearchTree.cpp
// Author      : Quintin B. Rozelle
// Version     : 1.0
// Copyright   : Copyright © 2017 SNHU COCE
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <time.h>

#include "CSVparser.hpp"

using namespace std;

//============================================================================
// Global definitions visible to all methods and classes
//============================================================================

// forward declarations
double strToDouble(string str, char ch);

// define a structure to hold bid information
struct Bid {
    string bidId; // unique identifier
    string title;
    string fund;
    double amount;
    Bid() {
        amount = 0.0;
    }
};

// Internal structure for tree node
struct Node {
    Bid bid;
    Node *left;
    Node *right;

    // default constructor
    Node() {
        left = nullptr;
        right = nullptr;
    }

    // initialize with a bid
    Node(Bid aBid) :
            Node() {
        bid = aBid;
    }
};

//============================================================================
// Binary Search Tree class definition
//============================================================================

/**
 * Define a class containing data members and methods to
 * implement a binary search tree
 */
class BinarySearchTree {

private:
    Node* root;

    //Added postOrder, preOrder, postOrderRemove

    void addNode(Node* node, Bid bid);
    void inOrder(Node* node);
    void postOrder(Node* node);
    void postOrderRemove(Node* node);
    void preOrder(Node* node);

public:
    //Added postOrder and preOrder

    BinarySearchTree();
    virtual ~BinarySearchTree();
    void InOrder();
    void Insert(Bid bid);
    void PostOrder();
    void PreOrder();
    void Remove(string bidId);
    Bid Search(string bidId);
};

/**
 * Default constructor
 */
BinarySearchTree::BinarySearchTree() {
    // DONE-FixMe (1): initialize housekeeping variables
    //root is equal to nullptr
    root = nullptr;
}

/**
 * Destructor
 */
BinarySearchTree::~BinarySearchTree() {
    // recurse from root deleting every node
    postOrderRemove(root);
}

/**
 * Traverse the tree in order
 */
void BinarySearchTree::InOrder() {
    // DONE-FixMe (2): In order root
    // call inOrder fuction and pass root 
    inOrder(root);
}

/**
 * Traverse the tree in post-order
 */
void BinarySearchTree::PostOrder() {
    // DONE-FixMe (3): Post order root
    // postOrder root
    postOrder(root);
}

/**
 * Traverse the tree in pre-order
 */
void BinarySearchTree::PreOrder() {
    // DONE-FixMe (4): Pre order root
    // preOrder root
    preOrder(root);
}

/**
 * Insert a bid
 */
void BinarySearchTree::Insert(Bid bid) {
    // DONE-FIXME (5) Implement inserting a bid into the tree
    // if root equarl to null ptr
    if (root == nullptr) {

        // root is equal to new node bid
        root = new Node(bid);
    }
    // else
    else {

        // add Node root and bid
        //Start at root and cycle through branches
        Node* current = root;
        while (current != nullptr) {

            //if bid matches current, do nothing. Prevents adding duplicates
            if (bid.bidId == current->bid.bidId) {
                return;
            }

            //if bid goes to left branch
            else if (bid.bidId < current->bid.bidId) {
                
                //if left branch is empty, add new node
                if (current->left == nullptr) {
                    current->left = new Node(bid);
                    current = nullptr;
                }

                //else move to left branch and cycle again
                else {
                    current = current->left;
                }
            }

            //else bid goes to right branch
            else {

                //if right branch is empty, add new node
                if (current->right == nullptr) {
                    current->right = new Node(bid);
                    current = nullptr;
                }

                //else move to right branch and cycle again
                else {
                    current = current->right;
                }
            }
        }

    }
}

/**
 * Remove a bid
 */
void BinarySearchTree::Remove(string bidId) {
    // DONE-FIXME (6) Implement removing a bid from the tree
    // remove node root bidID
    
    //housekeeping variables
    Node* parent = nullptr;
    Node* current = root;

    //cycle through nodes
    while (current != nullptr) {

        //if current is searched node
        if (current->bid.bidId == bidId) {
            
            //remove if leaf
            if (current->left == nullptr && current->right == nullptr) {
                
                //if current is root
                if (parent == nullptr) {
                    current = nullptr;
                }
                else if (parent->left == current) {
                    parent->left = nullptr;
                }
                else {
                    parent->right = nullptr;
                }
            }

            //remove node with only left child
            else if (current->right == nullptr) {
               
                //if current is root
                if (parent == nullptr) {
                    root = current->left;
                }
                else if (parent->left == current) {
                    parent->left = current->left;
                }
                else {
                    parent->right = current->left;
                }
            }
            
            //remove node with only right child
            else if (current->left == nullptr) {

                //if current is root
                if (parent == nullptr) {
                    root = current->right;
                }
                else if (parent->left == current) {
                    parent->left = current->right;
                }
                else {
                    parent->right = current->right;
                }
            }

            //remove node with two children
            else {

                //find successor
                Node* successor = current->right;
                while (successor->left != nullptr) {
                    successor = successor->left;
                }

                //copy successor's bid info
                Bid successorBid = successor->bid;

                //remove successor
                Remove(successor->bid.bidId);

                //give current successor's bid info
                current->bid = successorBid;
            }

            //node was found
            return;
        }

        //current is not searched bid. Look right
        else if (current->bid.bidId < bidId) {
            parent = current;
            current = current->right;
        }

        //look left
        else {
            parent = current;
            current = current->left;
        }
    }

    //node not found
    return;
}

/**
 * Search for a bid
 */
Bid BinarySearchTree::Search(string bidId) {
    // DONE-FIXME (7) Implement searching the tree for a bid
    // set current node equal to root
    Node* current = root;

    // keep looping downwards until bottom reached or matching bidId found
    while (current != nullptr) {

        // if match found, return current bid
        if (current->bid.bidId == bidId) {
            return current->bid;
        }

        // if bid is smaller than current node then traverse left
        else if (current->bid.bidId > bidId) {
            current = current->left;
        }

        // else larger so traverse right
        else {
            current = current->right;
        }
    }

    //not found. return empty bid
    Bid bid;
    return bid;
}

/**
 * Add a bid to some node (recursive)
 *
 * @param node Current node in tree
 * @param bid Bid to be added
 */
void BinarySearchTree::addNode(Node* node, Bid bid) {
    // DONE-FIXME (8) Implement inserting a bid into the tree
    //if bid is current node, do nothing. prevents adding duplicates
    if (bid.bidId == node->bid.bidId) {
        return;
    }
    
    // if node is larger then add to left
    else if (bid.bidId < node->bid.bidId) {

        // if no left node
        if (node->left == nullptr) {

            // this node becomes left
            node->left = new Node(bid);
        }

        // else recurse down the left node
        else {
            addNode(node->left, bid);
        }
    }

    // else
    else {

        // if no right node
        if (node->right == nullptr) {

            // this node becomes right
            node->right = new Node(bid);
        }

        //else
        else {

            // recurse down the left node
            addNode(node->right, bid);
        }
    }
}
void BinarySearchTree::inOrder(Node* node) {
      // DONE-FixMe (9): inorder root
      //if node is not equal to null ptr
    if (node != nullptr) {

        //InOrder not left
        inOrder(node->left);

        //output bidID, title, amount, fund
        cout << node->bid.bidId << " | ";
        cout << node->bid.title << " | ";
        cout << node->bid.amount << " | ";
        cout << node->bid.fund << endl;

        //InOder right
        inOrder(node->right);
    }
}
void BinarySearchTree::postOrder(Node* node) {
      // DONE-FixMe (10): Post order root
      //if node is not equal to null ptr
    if (node != nullptr) {

        //postOrder left
        postOrder(node->left);

        //postOrder right
        postOrder(node->right);

        //output bidID, title, amount, fund
        cout << node->bid.bidId << " | ";
        cout << node->bid.title << " | ";
        cout << node->bid.amount << " | ";
        cout << node->bid.fund << endl;
    }
}

void BinarySearchTree::postOrderRemove(Node* node) {
    //if node is not equal to null ptr
    if (node != nullptr) {

        //postOrder left
        postOrderRemove(node->left);

        //postOrder right
        postOrderRemove(node->right);

        //delete node
        delete node;
    }
}

void BinarySearchTree::preOrder(Node* node) {
      // DONE-FixMe (11): Pre order root
      //if node is not equal to null ptr
    if (node != nullptr) {

        //output bidID, title, amount, fund
        cout << node->bid.bidId << " | ";
        cout << node->bid.title << " | ";
        cout << node->bid.amount << " | ";
        cout << node->bid.fund << endl;

        //preOrder left
        preOrder(node->left);

        //preOrder right  
        preOrder(node->right);
    }
}

//============================================================================
// Static methods used for testing
//============================================================================

/**
 * Display the bid information to the console (std::out)
 *
 * @param bid struct containing the bid info
 */
void displayBid(Bid bid) {
    cout << bid.bidId << ": " << bid.title << " | " << bid.amount << " | "
            << bid.fund << endl;
    return;
}

/**
 * Load a CSV file containing bids into a container
 *
 * @param csvPath the path to the CSV file to load
 * @return a container holding all the bids read
 */
void loadBids(string csvPath, BinarySearchTree* bst) {
    cout << "Loading CSV file " << csvPath << endl;

    // initialize the CSV Parser using the given path
    csv::Parser file = csv::Parser(csvPath);

    // read and display header row - optional
    vector<string> header = file.getHeader();
    for (auto const& c : header) {
        cout << c << " | ";
    }
    cout << "" << endl;

    try {
        // loop to read rows of a CSV file
        for (unsigned int i = 0; i < file.rowCount(); i++) {

            // Create a data structure and add to the collection of bids
            Bid bid;
            bid.bidId = file[i][1];
            bid.title = file[i][0];
            bid.fund = file[i][8];
            bid.amount = strToDouble(file[i][4], '$');

            //cout << "Item: " << bid.title << ", Fund: " << bid.fund << ", Amount: " << bid.amount << endl;

            // push this bid to the end
            bst->Insert(bid);
        }
    } catch (csv::Error &e) {
        std::cerr << e.what() << std::endl;
    }
}

/**
 * Simple C function to convert a string to a double
 * after stripping out unwanted char
 *
 * credit: http://stackoverflow.com/a/24875936
 *
 * @param ch The character to strip out
 */
double strToDouble(string str, char ch) {
    str.erase(remove(str.begin(), str.end(), ch), str.end());
    return atof(str.c_str());
}

/**
 * The one and only main() method
 */
int main(int argc, char* argv[]) {

    // process command line arguments
    string csvPath, bidKey;
    switch (argc) {
    case 2:
        csvPath = argv[1];
        bidKey = "98109";
        break;
    case 3:
        csvPath = argv[1];
        bidKey = argv[2];
        break;
    default:
        csvPath = "eBid_Monthly_Sales_Dec_2016.csv";
        bidKey = "98109";
    }

    // Define a timer variable
    clock_t ticks;

    // Define a binary search tree to hold all bids
    BinarySearchTree* bst;
    bst = new BinarySearchTree();
    Bid bid;

    int choice = 0;
    while (choice != 9) {
        cout << "Menu:" << endl;
        cout << "  1. Load Bids" << endl;
        cout << "  2. Display All Bids" << endl;
        cout << "  3. Find Bid" << endl;
        cout << "  4. Remove Bid" << endl;
        cout << "  9. Exit" << endl;
        cout << "Enter choice: ";
        cin >> choice;

        switch (choice) {

        case 1:
            
            // Initialize a timer variable before loading bids
            ticks = clock();

            // Complete the method call to load the bids
            loadBids(csvPath, bst);

            //cout << bst->Size() << " bids read" << endl;

            // Calculate elapsed time and display result
            ticks = clock() - ticks; // current clock ticks minus starting clock ticks
            cout << "time: " << ticks << " clock ticks" << endl;
            cout << "time: " << ticks * 1.0 / CLOCKS_PER_SEC << " seconds" << endl;
            break;

        case 2:
            bst->InOrder();
            break;

        case 3:
            ticks = clock();

            bid = bst->Search(bidKey);

            ticks = clock() - ticks; // current clock ticks minus starting clock ticks

            if (!bid.bidId.empty()) {
                displayBid(bid);
            } else {
            	cout << "Bid Id " << bidKey << " not found." << endl;
            }

            cout << "time: " << ticks << " clock ticks" << endl;
            cout << "time: " << ticks * 1.0 / CLOCKS_PER_SEC << " seconds" << endl;

            break;

        case 4:
            bst->Remove(bidKey);
            break;
        }
    }

    cout << "Good bye." << endl;

	return 0;
}
