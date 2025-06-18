# Quintin B. Rozelle
## Contents
[Professional Self-Assessment](#professional-self-assessment)<br>
[Code Review](#code-review)<br>
[Enhancement One](#enhancement-one)<br>
[Enhancement Two](#enhancement-two)<br>
[Enhancement Three](#enhancement-three)<br>
[References](#references)

## Professional Self-Assessment
I have always had an interest in computers and programming, though I didn’t seriously explore these areas until starting this degree at SNHU. Prior to this, I had dabbled a bit with basic HTML and CSS and taught myself to use Excel to a highly proficient level, thinking that this would satisfy my curiosity for computers and programming. While the latter is not overly related to the field of computer science, I would argue that there are minor elements of it which are. Instead of sating my curiosity, this experience only piqued my interest and caused a desire to learn more which this computer science program has SNHU has been able to provide. I have thoroughly enjoyed each and every course of this degree and have taken it as an opportunity to learn about the various aspects of computer science while growing my skills in them. I consider myself to be a lifelong learner and SNHU has given me the knowledge necessary to enter into the field of computer science while also providing me a very solid foundation to build upon over my career. Through this degree I have gained knowledge and developed my strengths in a number of areas.
### Data Structures and Algorithms
Appropriately using data structures and algorithms is essential to creating a well-functioning product. Using the incorrect data structure or creating a less-than-optimal algorithm can severely hamper the end-user’s experience. CS-300 (Data Structures and Algorithms) gave me the knowledge necessary to apply the most commonly used data structures. Based on this, I have the ability to create classes and objects that adhere to the needs of and work well with a data structure. Enhancements one and two for this portfolio are good examples of this in which I have created a Bid class that works well with two different types of binary search trees.

Another example comes early in this degree from IT-145 (Foundations in App Development). One of the assignments in this course was to build an intake system for rescue animals. As the total number of animals to store is unknown at runtime though likely relatively small, an ArrayList is a good choice:
```java
    private static ArrayList<Dog> dogList = new ArrayList<Dog>();
```
This was easy to use to store prepopulated data and eventually to search to data on intake to prevent duplicate entries:
```java
    // Adds dogs to a list for testing
    public static void initializeDogList() {
        Dog dog1 = new Dog("Spot", "German Shepherd", "male", 1, 25.6, "05-12-2019", "United States", "intake", false, "United States");
        Dog dog2 = new Dog("Rex", "Great Dane", "male", 3, 35.2, "02-03-2020", "United States", "Phase I", false, "United States");
        Dog dog3 = new Dog("Bella", "Chihuahua", "female", 4, 25.6, "12-12-2019", "Canada", "in service", true, "Canada");
        Dog dog4 = new Dog("Lady", "Basset", "female", 6, 55.6, "01-02-2018", "United States", "in service", false, "United States");
        Dog dog5 = new Dog("Hank", "Yellow Lab", "male", 4, 70.2, "10-22-2019", "Canada", "in service", false, "Canada");

        dogList.add(dog1);
        dogList.add(dog2);
        dogList.add(dog3);
        dogList.add(dog4);
        dogList.add(dog5);
    }
```

```java
    public static void intakeNewDog(Scanner scanner) {
        String name = getUserString(scanner, "What is the dog's name?");
        // Check for dog already in system
        for(Dog dog: dogList) {
            if(dog.getName().equalsIgnoreCase(name)) {
                System.out.println("\nThis dog is already in our system\n");
                return; //returns to menu
            }
        }
```

### Software Engineering and Databases
Software engineering and database use are also essential to a well-functioning program. Without using either appropriately, the program could lose data or malfunction. My concentration for this degree is Software Engineering so many of my courses incorporated this. A great example of this comes from CS-465 (Full Stack Development) in which I built MEAN stack website. A strength of this project was the separation and encapsulation of components into their own files. This allowed for easier development as each file was focused and simple to create and debug and makes the whole project easier to understand. This project created a full functioning end-user facing website with an admin focused backend for easing the management of data displayed on the front end. Both interact with a MongoDB through the use of a custom-built API.

In addition to the use of a MongoDB for this project, I have grown my abilities to use databases through DAD-220 (Introduction to Structured Database Environments) and CS-340 (Client-Server Development) in which I learned to use relational and document-based databases respectively. An example of my ability to use and interact with databases comes from CS-340 in which I built a CRUD API to handle the management of documents within a MongoDB:
```python
    # Create new document and add to database
    # data: new document to add to database. Needs to be a Python dictionary
    # returns: boolean; true if successful, false if failure
    def create(self, data: dict) -> bool:
        try:
            if data is not None:
                insertSuccess = self.database.animals.insert_one(data)
                return insertSuccess.acknowledged
            else:
                raise Exception('Nothing to save, because data parameter is empty')
        except Exception as e:
            print(repr(e))
            return False
    
    
    # Searches for and returns list of documents from database
    # data: document to search for in database. Needs to be a Python dictionary
    # returns: list of documents found
    def read(self, data: dict) -> list:
        try:
            if data is not None:
                return list(self.database.animals.find(data))
            else:
                raise Exception('Nothing to search for, because data parameter is empty')
        except Exception as e:
            print(repr(e))
            return list()
        
    
    # Search for and update document(s) in the database
    # searchData: document to search for in database. Needs to be a Python dictionary
    # updateData: key/value pairs to update in found documents. Needs to be a Python dictionary
    # returns: the number of documents updated
    def update(self, searchData: dict, updateData: dict) -> int:
        try:
            if searchData is not None or updateData is not None:
                return self.database.animals.update_many(searchData, updateData).modified_count
            else:
                raise Exception('Nothing to search for, because searchData or updataData parameter is empty')
        except Exception as e:
            print(repr(e))
            return 0
        
        
    # Deletes document(s) in the database
    # data: document to search for in database. Needs to be a Python dictionary
    # returns: the number of documents deleted
    def delete(self, data: dict) -> int:
        try:
            if data is not None:
                return self.database.animals.delete_many(data).deleted_count
            else:
                raise Exception('Nothing to search for, because data parameter is empty')
        except Exception as e:
            print(repr(e))
            return 0
```

### Security
Similar to the above two sections, software security is paramount to software development as it prevents both unintentional software crashes and intentional breaches. My skills in this area come from CS-305 (Software Security) and CS-405 (Secure Coding). In the former, I learned to use dependency checking tools to check for known security vulnerabilities and cryptography techniques to allow for transfer of sensitive information:
```java
    @RestController
    class ServerController{
        
        /**
         * Function to convert byte array to hexadecimal.
         * <p>Found at: https://stackoverflow.com/questions/9655181/how-to-convert-a-byte-array-to-a-hex-string-in-java
         * @param bytes  The byte array to convert to hexadecimal
         * @return  String containing the converted byte array
         */
        public static String bytesToHex(byte[] bytes) {
            final char[] HEX_ARRAY = "0123456789ABCDEF".toCharArray();
            char[] hexChars = new char[bytes.length * 2];
            for (int j = 0; j < bytes.length; j++) {
                int v = bytes[j] & 0xFF;
                hexChars[j * 2] = HEX_ARRAY[v >>> 4];
                hexChars[j * 2 + 1] = HEX_ARRAY[v & 0x0F];
            }
            return new String(hexChars);
        }
        
        @RequestMapping("/hash")
        public String myHash() throws NoSuchAlgorithmException{
            String data = "Quintin B. Rozelle's unique data string";
            
            //New message digest that creates hash
            MessageDigest md = MessageDigest.getInstance("SHA-256");
            byte[] hash = md.digest(data.getBytes());
            
            //Convert the hash to hexadecimal
            String hexHash = bytesToHex(hash);
        
            return "<p>data: "+data+"<p>Name of Cipher Algorithm Used: SHA-256<p>CheckSum Value: "+hexHash;
        }
    }
```

In the latter class, I gained the ability to incorporate secure coding practices into my code to prevent security issues. Examples of this are the prevention of buffer overflow and SQL injection. In the code below, buffer overflow is prevented by using the getline function to read into an array no more than the size of that array:
```c++
    //char user_input[20];
    const std::string account_number = "CharlieBrown42";
    char user_input[20];
    std::cout << "Enter a value: ";

    // Added call to getline which terminates the character extraction once a certain number of characters are reached.
    // The second argument calculates the total number of elements assigned to the array. This prevents issues with
    // extracting the wrong number of characters from cin if the code is changed to define user_input with a different
    // number of elements in the array
    std::cin.getline(user_input, sizeof(user_input)/sizeof(*user_input));

    std::cout << "You entered: " << user_input << std::endl;
    std::cout << "Account Number = " << account_number << std::endl;
```
 
SQL injection is prevented in the following code example by using a regex to search user input for SQL injection attempts:
```c++
    bool run_query(sqlite3* db, const std::string& sql, std::vector< user_record >& records)
    {
    // clear any prior results
    records.clear();

    // Uses a regular expression to search for the presence of " or *** = ***" where *** is any valid SQL value and "or" is case insensitive
    std::regex sqlInjectionSearch(" [Oo][Rr] .*=.*");
    if (std::regex_search(sql, sqlInjectionSearch))
    {
        // SQL injection attempt found. Print notification to console and fail search
        std::cout << "Attempted SQL injection identified. Aborting search" << std::endl;
        return false;
    }

    char* error_message;
    if(sqlite3_exec(db, sql.c_str(), callback, &records, &error_message) != SQLITE_OK)
    {
        std::cout << "Data failed to be queried from USERS table. ERROR = " << error_message << std::endl;
        sqlite3_free(error_message);
        return false;
    }

    return true;
    }
```
 
### Collaborating in a team environment
In addition to the hard skills listed above, a successful developer needs to be proficient in some of the softer skills as well. Since most developers do not work alone, being able to work well on a team is vital. CS-250 (Software Development Lifecycle) gave me the skills to work with teams that use the Agile framework. In this course, I simulated working on a team like this through written assignments and a group project/discussion. I also created an Agile team charter that could be used in a theoretical team:
![Agile Team Charter](/assets/img/cs-250_agile_charter.png "Agile Team Charter")
 
### Communicating with stakeholders
In addition to collaborating with a team, a developer must also communicate and collaborate with stakeholders. CS-250 and CS-319 (UI/UX Design and Development) provided me with the opportunity to improve these skills. As an example of this, in CS-250, I created multiple User Stories for a project to put myself in the end-user’s shoes to help ensure I was creating something they needed instead of something I thought they needed:
![User Story](/assets/img/cs-250_user_story.png "User Story")
 
As another example, in CS-319 I conducted several interviews with potential users for a mobile app I was creating:
![End User Interview](/assets/img/cs-319_user_interview.png "End User Interview")
 
Both cases showcase my ability to work with stakeholders to improve the product that I provide.
### Artifact Summary
The enhancements for this portfolio are all applied to the same artifact. This artifact comes from CS-300 (Data Structures and Algorithms). In it, I built a tool for reading auction information from a CSV file, adding that information to Bid objects, and storing those Bids in a binary search tree. This tool would then be able to display all information, display a specific record or delete a record from the BST.

Enhancement One takes the original artifact and converts it from C++ to Python. This showcases my skills in software development through my ability to convert software from one language to another while understanding the nuances of both. In addition to this, I improved the documentation by adding well written comments where necessary and including docstrings for every class and function to help improve understanding for another developer who would be coming into my code blind. Security was improved though the use of data validation and exception handling. Lastly, software stability was ensured through the implementation of unit testing.

Enhancement Two takes Enhancement One a step further by improving the data structure and algorithms used. Enhancement One retained the use of a standard binary search tree from the original artifact, but this enhancement converts that to the more advanced Red-Black Tree. This ensures that the algorithms run at a guaranteed time complexity of O(log n) instead of the potential for a time complexity of O(n) that standard binary search trees can have in certain situations (e.g., presorted input data, etc.). This enhancement retains and continues to build upon the documentation, security, and stability that Enhancement One introduced.

Enhancement Three further improves upon the updates from Enhancement Two by implementing the use of a database to store the information between sessions. Since the imported data was stored in a data structure stored in memory, as soon as the program closes that information is lost. By using a database (in this case a SQLite database), that information is no longer volatile. To ease the use of and interaction with the database, a CRUD API was built which further helps to clean up the code and make it more readable. As with the other enhancements, the documentation, security, and stability improvements are maintained.

### Course Outcomes
Through the completion of this self-assessment and the code enhancements, I have successfully achieved the outcomes for this course. Each narrative provides an update to the completion of each outcome up to that point, but this serves as a summary of the status of each at the end of this course.
1. Employ strategies for building collaborative environments that enable diverse audiences to support organizational decision-making in the field of computer science.
    - I have achieved this through my documentation in the code and the creation of an API. Each enhancement includes well written comments throughout the code to describe its functionality. Additionally, each function includes a complete docstring indicating its purpose, its parameters, and its output. Lastly, the CRUD API developed for enhancement three provides an easy and consistent way to interact with the SQLite database. These help to make the code more clear while also providing the documentation needed for other developers to use and build off my code.
2. Design, develop, and deliver professional-quality oral, written, and visual communications that are coherent, technically sound, and appropriately adapted to specific audiences and contexts.
    - I have achieved this through the narratives, code review, completed ePortfolio, and this professional self-assessment. All combine to show my ability to provide written, oral, and visual communication that is professional, accurate, and adapted to the audience.
3. Design and evaluate computing solutions that solve a given problem using algorithmic principles and computer science practices and standards appropriate to its solution while managing the trade-offs involved in design choices.
    - I have completed this outcome through the implementation of a Red-Black Tree in enhancement two. Prior to this, the code used a standard binary search tree. While easy to implement and effective for many situations, these are less than optimal in certain edge cases (e.g., presorted data, etc.) in which they have a time complexity of O(n). Using a self-balancing tree, like a Red-Black Tree, guarantees a time complexity of O(log n).
4. Demonstrate an ability to use well-founded and innovative techniques, skills, and tools in computing practices for the purpose of implementing computer solutions that deliver value and accomplish industry-specific goals.
    - I have achieved this outcome through the use of prebuilt libraries to speed development while also utilizing best practices in the areas that these libraries focus. All three enhancements used Python’s CSV module to handle CSV manipulation. Additionally, enhancement three used Python’s sqlite3 module to manage interaction with the SQLite database. Both streamlined the development of the code by preventing the need to reinvent the wheel and also ensured the functionality that these performed was done in an optimal and efficient manner since I was using well vetted and bug free code.
5. Develop a security mindset that anticipates adversarial exploits in software architecture and designs to expose potential vulnerabilities, mitigate design flaws, and ensure privacy and enhanced security of data and resources.
    - I achieved this outcome through the use of data validation and exception handling throughout the enhancements. The data validation ensured that information given to the programs was reasonable and in the format intended to prevent crashes or unintended side effects (e.g., SQL injection, etc.). Additionally, the exception handling allowed the code to catch thrown errors and deal with them in a way that prevented the program from crashing.


## Code Review
{% include youtubePlayer.html %}

## Enhancement One
### Briefly describe the artifact. What is it? When was it created?
The artifact chosen for enhancement one is the binary search tree (BST) assignment from CS-300 Data Structures and Algorithms. This is a quick program that will load a CSV file into memory as a BST and perform basic insertion, search, deletion, and traversal operations on it. It was originally meant as an assignment to gain experience working with BST. I chose to use this one for enhancement one specifically for a few different reasons:
1.	I wanted to convert something from one language to another for this artifact. Upon thinking about this, I decided to convert something into Python because it has been a while since I used Python to any significant degree and this enhancement provided me with the opportunity to brush up on my Python skills. Additionally, if I do go into something involving big data, I will need to be proficient in Python.
2.	In addition to brushing up on Python, I also wanted to take the opportunity in this class to gain more experience with data structures and algorithms (DSA) since it has been a while since I specifically reviewed/studied those. While enhancement two does cover this, using something related to DSA during another enhancement would give me additional experience.
3.	Upon reviewing artifacts that fit the above goals, I realized that there were many areas that I could improve this one specifically. This gives me the chance to showcase what I have learned through this degree since I originally created the original code.

### Justify the inclusion of the artifact in your ePortfolio. Why did you select this item? What specific components of the artifact showcase your skills and abilities in software development? How was the artifact improved?
As stated above, this artifact fits the requirements I was looking for in this enhancement (i.e., conversion to Python, DSA, and opportunities to improve). Further, in planning the additional enhancements, I realized that I could use this for all three which gives me the opportunity to show how I can take code and improve it over time to produce a polished deliverable for a client.

While reviewing the original code, I discovered some significant areas of improvement. These include exception handling, input validation, and better documentation, in addition to converting it to Python. An example of added error handling is in the loadBids function. This loads a file and uses the csv module to parse that file. These options have the possibility to throw errors if something goes wrong. To fix this, the section that could throw errors is wrapped in a try/except block which prints meaningful feedback to the user of what caused the error:
```python
bst = binarySearchTree.BinarySearchTree()
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
                        bst.insert(Bid(int(row[bidIdColumn]),
                                       row[titleColumn],
                                       row[fundColumn],
                                       float((row[bidAmountColumn][1:]).replace(',','')))) #strip initial $ sign and convert to float
    except Exception as error:
        print("Error loading file")
        print(f"Error type: {type(error)}")
        print(f"Error message: {error}")
    finally:
        return bst
```

An example of input validation can be seen in the displayMainMenu function which displays the main menu and accepts input which is returned to the main function for further processing. This function will only return the entered input if it is found in a list of acceptable choices, otherwise it tells the user the input was invalid and loops back to the start of the function:
```python
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
```

Lastly, examples of the improved documentation can be seen throughout the code in the inclusion of docstrings to document what a function does to make using this code easier for another developer:
```python
    def search(self, key: Any) -> Any:
        """
        Searches for a key in the BST
        
        Parameters
        ----------
        key : Any
            The key to be searched for in the BST
            
        Returns
        -------
        Any
            The full key if found, otherwise None.
            Allows for returning full key if keys are complex objects
            and search was performed with dummy key containing only
            the attributed used for comparison.
        """
```

While making these improvements, I realized additional areas that could be improved which I worked into the final enhancement. First, the original code was all in one file which was good for the original intent, but splitting portions into separate modules adds further improvements as it better encapsulates related code, makes it easier to read and maintain, and provides for future reuse. On this last point specifically, I realized that since I will be adding a red-black tree to the second enhancement, if I split the BST and node classes into their own module, I can add the red-black tree to that and use the code for loading a file and displaying the menu almost unchanged. Next, I incorporated the use of unit testing. I created separate files which test the functionality of the main modules. This greatly speeds up the testing process.

### Did you meet the course outcomes you planned to meet with this enhancement in Module One? Do you have any updates to your outcome-coverage plans?
I planned to target outcomes 1, 4, and 5 with this enhancement and have met all three with the enhancements I made to this artifact. For outcome 1, I have included well written comments and docstrings throughout the code to convey to another developer what functions are for. For outcome 4, I have successfully implemented and used modules that others have created to create my solution. Lastly, for outcome 5, I have added increased security and reliability through data validation and exception handling.

### Reflect on the process of enhancing and modifying the artifact. What did you learn as you were creating it and improving it? What challenges did you face?
In addition to the stated learning goals above (i.e., more practice with Python and DSA), I learned a few additional things. First, I chose to better use unit testing while creating this artifact which historically is something I haven’t done much. While it did take time to learn unit testing in Python and develop those unit tests prior to coding the enhancement, it did produce better results and helped to guide my development. Next, I learned that Python has a limit to the number of recursive functions that can be added to the stack which appears to be around 1000. I originally made my BST functions use recursion, but found that when loading a 12,000-line, presorted CSV file, the code would fail due to this limit. Converting the functions to iterative versions solved this issue. Lastly, I learned that the format of a source file can have drastic changes to the functioning code. Once I fixed the issue with recursion, I decided to test my code on the same CSV file but when it was randomly sorted. The presorted file took my program about 13.5 seconds to load while the randomly sorted file took about 0.1 seconds to load. I believe this is because the presorted build an incredibly tall BST (all nodes essentially having only right children) while the randomly sorted file created a more well-balanced BST. This cut down on the iterations during the insertions which created a faster tree.

## Enhancement Two
### Briefly describe the artifact. What is it? When was it created?
The artifact chosen for this enhancement is the binary search tree (BST) assignment from CS-300 Data Structures and Algorithms. The original intent of this code was to showcase the use of a BST in storing, sorting, searching, displaying, and deleting data that was imported from a CSV file. It was one of a series of similar assignments that accomplished the same task but with different data structures so we could learn firsthand how they function and differ from one another.

### Justify the inclusion of the artifact in your ePortfolio. Why did you select this item? What specific components of the artifact showcase your skills and abilities in algorithms and data structure? How was the artifact improved?
I chose this artifact for this enhancement due to some discoveries I made while researching data structures and algorithms. I was aware that more advanced data structures existed but I didn’t know much about them, so I had assumed that BST offered what they did with minimal downsides. I quickly discovered that standard BSTs are not guaranteed to have a time complexity of O(log n) because they have no mechanism for enforcing balance to the tree. In fact, in a BST that has no balance (i.e., all nodes share the same parity in regard to their left verse right child status), operations approach a time complexity of O(n) [GeeksforGeeks, 2025](#references). I further learned that BST data structures that enforce self-balancing retain a guaranteed time complexity of O(log n). Based on this, I became interested exploring one of these.

Using this artifact seemed like the obvious choice since it is originally built with a standard BST and improving it with a self-balancing BST would provide me the opportunity to learn how these work while seeing firsthand how they improve upon a non-self-balancing BST. I settled on implementing a Red Black Tree (RBT) over other self-balancing BSTs (i.e., AVL Trees or Splay Trees) because RBTs are best for situations in which insertion speed is needed more than search speed [GeeksforGeeks, 2023](#references). Since this artifact does more insertions than searches, an RBT was chosen as the best option.

The main improvements for this artifact are the inclusion of an RBT as the data structure used while also building it in a way that the BST that was built for enhancement one didn’t break. This was done through separate classes (BST vs RBT) while also modifying the Node class to work with either data structure. In addition to this, I further improved the unit testing to test the new RBT.

In addition to the implementation of an RBT, I also retained the improved security and stability that was created during the first enhancement. This is accomplished through data validation and exception handling. Examples of data validation include the following:
- Ensuring that Bid data meets the requirements of the Bid class, specifically that the Bid ID and Bid Amount are and int and float respectively:
```python
    rbt.insert(Bid(int(row[bidIdColumn]),
                   row[titleColumn],
                   row[fundColumn],
                   float((row[bidAmountColumn][1:]).replace(',','')))) #strip initial $ sign and convert to float
```
- Ensuring that input for menus adhere to the set of possible choices. Deviations from this display an error and ask the user to try again:
```python
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
```
The main example of exception handling is seen in the loadBids function. This function has the possibility of throwing an exception due to a variety of reasons (e.g., missing file, missing headers in file, data formatted incorrectly, etc.). This function will catch those errors, display an appropriate error message to the user, then return to the main function:
```python
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
```


The skill I have shown with this enhancement is my ability to select and apply advanced algorithms and data structures to a problem when necessary. The thought process for choosing an RBT over another self-balancing BST shows that I can critically think about the best solution for the task at hand and my coding of the RBT shows that I am able to implement that solution.

### Did you meet the course outcomes you planned to meet with this enhancement in Module One? Do you have any updates to your outcome-coverage plans?
I planned to apply outcomes 1 and 3 with this enhancement. Like enhancement one, I have made significant progress toward outcome 1 with this enhancement through my inclusion of well written comments and docstrings, though I do not wish to consider it completed until finishing enhancement three since I have also applied outcome 1 to that as well. I have successfully completed outcome 3 with this enhancement though my implementation of an RBT as the data structure for this artifact.

### Reflect on the process of enhancing and modifying the artifact. What did you learn as you were creating it and improving it? What challenges did you face?
I learned two major things about advanced data structures and algorithms with this enhancement. First is how much more complex they are than the ones we learned in CS-300 Algorithms and Data Structures. I assumed RBTs to be more complex than standard BSTs, but I didn’t realize by how much until I researched them and began to code one. I ran into a few difficulties while coding this RBT which caused it to not work correctly at first. My issue was that I assumed that leaves on an RBT function the same way that they do in a BST, that is that a BSTs leaves are the end of a BST, and their left and right children are null pointers. I originally built the RBT the same without realizing that their leaves have left and right children that are not null pointers but are in fact nodes that have a null key. This seemed like a very minor distinction until my code ran into issues with finding some nodes’ sibling and uncle nodes. In my first iteration, these didn’t always exist, so my code failed. Once I realized this and fixed the issue, the code worked as intended.

The second major thing I learned is how much of an improvement an RBT is over a standard BST. While testing my code, I used two separate data sets for loading information into the data structures. Both had identical information, but one was randomly sorted while the other was sorted by key. With a BST, the randomly sorted data was inserted into the tree quickly (approximately 0.9 seconds) while the sorted data set took significantly longer (about 13.5 seconds). Using the same data sets on an RBT resulted in a load time of about 0.9 seconds for either sorting method. Enforcing balancing to a tree has a significant improvement to its functionality.

## Enhancement Three
### Briefly describe the artifact. What is it? When was it created?
The artifact chosen for this enhancement is the binary search tree assignment from CS-300 Data Structures and Algorithms. This was one assignment in a series that provided hands on experience with a variety of data structures. Each assignment accomplished the same task (i.e., loading, sorting, displaying, searching, and deleting records from a CSV file into memory) but did so using different data structures each time. This particular artifact was meant to showcase the use and benefits of a binary search tree.
### Justify the inclusion of the artifact in your ePortfolio. Why did you select this item? What specific components of the artifact showcase your skills and abilities in databases? How was the artifact improved?
I chose this artifact since it works with and manipulates a large dataset (over 12,000 data entries). The original artifact loaded these into memory only, so this seemed like the perfect opportunity to incorporate the use of a database. Doing so comes with the benefit of data persistence between sessions and the utilization of optimized data structures and algorithms that are inherent in a standard database.

To accomplish the implementation of the database, I chose to build a CRUD API to interface with the database. This comes with the benefit of standardizing the interactions and simplifying the communications with the database. A CRUD API achieves this by eliminating the need to hardcode the query strings and calls to the database cursor in the final product which helps to keep code clear and reduces the chance of bugs. In general, all API function work the same way. First, the take in the required information to perform their task. Next they build a query string from that data. Lastly, they pass that data along to a help function whose sole purpose is to run the query string and print a predefined message. As an example, the ‘createRecords’ function requires:
- The name of the table that the records will be added to
- The names of the columns that data will be added to in the form of a tuple
- The data for the records in the form a tuple of tuples. The outer tuple encapsulates all data, while each record is contained within its own tuple
- A boolean specifying whether or not to ignore duplicates
The function takes this supplied information and builds the query string. This query string is then passed to ‘_runQuery’ (the helper function that actually runs the query) along with the success message of “Records added successfully”. If ‘_runQuery’ is successful, the message will be displayed, otherwise it will display an error message.
```python
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
```

```python
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
```

While my final product utilized only a few of the necessary CRUD functions (i.e., database creation; table creation; record creation, read, and delete), I chose to create the full suite of standard CRUD functions for both tables and records. Some of these were ultimately unused, but it provided me the opportunity to practice API creation while also showing my skill and ability to do so.

In addition to the CRUD API, my other major enhancement was the implementation of the database itself. I had originally thought of using a MongoDB due to my familiarity with it, but chose to use a SQLite database instead. This allowed me to gain further experience with a database I haven’t used much. This also provided the benefit of a self-contained, local database which makes it easier to transfer the whole artifact to others to showcase my skills since another software (e.g., MySQL) isn’t necessary to install and setup. Overall, the database structure is simple as it is just one table, but that is all that was necessary to convert the original artifact into one that used a database.

Lastly, I built the code to withstand potential SQL injection attacks. This is done through two main mechanisms. First, direct communication with the SQLite database is limited as everything is passed through the CRUD API. Because of this, the only information that the user can provide that reaches the database is the CSV file and the bid ID numbers. Even then, this information is validated by converting inputs to integers (for the ID and monetary fields) or has quotations marks removed:
```python
    record: tuple[typing.Any] = (int(row[bidIdColumn]),
                                 row[titleColumn].replace("'", ''),
                                 row[fundColumn].replace("'", ''),
                                 float((row[bidAmountColumn][1:]).replace(',','')))
```
This simple functionality will prevent SQL injection attacks like ‘1=1’ because it will either throw an error because it cannot be converted to an int/float or will have the single quotes stripped prior to being used. Additionally, since each CRUD API function builds a query string that is surrounded in single quotes, an attack using double quotes (e.g., “1=1”) will either fail the conversion to an int/float or be treated as a string.

The conversion of the ID and monetary fields to integers does run the risk of throwing an error if the values aren’t numeric to begin with, but this will be caught and handled with the exception handling built into the code.
### Did you meet the course outcomes you planned to meet with this enhancement in Module One? Do you have any updates to your outcome-coverage plans?
I did meet the course outcomes (i.e., 1, 2, and 4) I had originally planned for this enhancement:
- Outcome 1 – I completed this outcome though the creation of the CRUD API and implementation of comments and docstrings. The CRUD API allowed me to easily interact with the SQLite database and would allow other developers to do so as well. Further, the comments and docstrings throughout my code made it easy to understand and interact with.
- Outcome 2 – I had originally planned to accomplish this via a GUI for displaying data from this enhancement but chose not to because I felt it moved too far away from the original intent of this milestone (i.e., the focus on the implementation of a database). I realized that the code review, the narratives created for these milestones, and the final ePortfolio showcase my ability to develop and deliver professional-quality oral, written, and visual communication. With the completion of this milestone, I am considering this outcome achieved, though I still plan to showcase it with my completed ePortfolio during week 7.
- Outcome 4 – This outcome has been achieved with the completion of this milestone through my implementation of Python’s CSV and sqlite3 modules. Using these shows my ability to incorporate code someone else has written to achieve the task at hand without reinventing the wheel.

The only update I have for the outcome-coverage plan is how I am completing Outcome Two. As stated above, my original plan was to show my visual communication skill though a GUI, but I chose to pivot due to concerns that this would detract from showcasing my ability to utilize a database. Instead, I will be accomplishing this outcome through the code review, narratives, and final ePortfolio. Overall, this isn’t a change in when these outcomes will be completed, but the means through which they are.
### Reflect on the process of enhancing and modifying the artifact. What did you learn as you were creating it and improving it? What challenges did you face?
As stated above, my experience with SQL databases is minimal and using SQLite specifically was non-existent. Through this enhancement I learned to use them better and gained more comfort using the SQL language. Gaining the experience with implementing a self-contained, local database (i.e., SQLite) was very beneficial since I can use this knowledge in the future if I am working on developing software that uses a database but is also meant to be shipped to an end user who doesn’t have the ability or desire to setup and connect to an external third party database.

The main challenge I had with this enhancement was the design of the CRUD API. I assumed it was going to be very simple and easy to create when I started but quickly came across many necessary decisions that changed the way in which I needed to build the database. I know this is part of iterative software development, but I could have streamlined this a bit more had I spent some more time prior to coding to think about the design elements of the API. As an example, I originally thought I would need only one helper function (i.e., _runQuery) that I would pass a query string to. While coding, I discovered that the ‘read’ functions are significantly different enough from the ‘creation’, ‘update’, and ‘delete’ functions that a second helper function was needed for these, so I built ‘_readQuery’ as well. Overall, this doesn’t detract from the API and it does make the underlying functionality of the API easier to understand, but is an example of a challenge I encountered while creating this enhancement.

## References
GeeksforGeeks. (2023, March 28). Self-balancing binary search trees. [https://www.geeksforgeeks.org/self-balancing-binary-search-trees/](https://www.geeksforgeeks.org/self-balancing-binary-search-trees/)<br>
GeeksforGeeks. (2025, May 16). Insertion in binary search tree (BST). [https://www.geeksforgeeks.org/insertion-in-binary-search-tree/](https://www.geeksforgeeks.org/insertion-in-binary-search-tree/)
