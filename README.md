# AllBooks

AllBooks is a Python CLI application for managing bookstore chains!

It uses a SQLite database to store three tables: bookstores, customers, and books. The database contains two one-to-many relationships:
a bookstore has many books, and a customer has many books. The application contains CRUD (Create, Read, Update, and Delete) methods implemented
in Python for each database table. The CLI makes interaction with the database simple and straightforward.

## Main Files

**lib/models:**

- *\_\_init\_\_.py* - connects to company.db and provides cursor for interacting with database
- *book.py* - contains Book class (models books table) and associated CRUD methods
- *bookstore.py* - contains Bookstore class (models bookstores table) and associated CRUD methods
- *customer.py* - contains Customer class (models customers table) and associated CRUD methods

**lib:**

- *cli.py* - main CLI program
- *debug.py* - used for debugging any part of program
- *helpers.py* - contains helper methods for *cli.py*
- *seed.py* - clears the database, then seeds it with sample data
- *company.db* - the SQLite database used

## Operation

This application uses Python 3.8. It has dependencies that require a virtual environment. If the virtual environment is not already set up, use the following command:
```bash
pipenv --python 3.8
```

If pipenv is not installed, use this command:
```bash
pip install pipenv
```

Otherwise, install dependencies and run the virtual environment:

```bash
pipenv install
pipenv shell
```

Then, seed the database:
```bash
python lib/seed.py
```

Finally, run the app:
```bash
python lib/cli.py
```

## Usage

Upon startup, the user will see the following screen:

```plaintext
Welcome to AllBooks, the book business management system!

Please select an option:

0. Exit the program
1. Manage bookstores
2. Manage customers
3. Manage books

> 
```

Selecting '0' will exit the program; selecting anything else will take the user to a menu for interacting with a specific database table. For example, if '2' is selected by typing '2' and pressing 'enter', the customers menu will be displayed:

```plaintext
Customer Manager - please select an option:

0. Return to main menu
1. List all customers
2. Find customer by last name
3: Create a customer
4: Update a customer
5: Delete a customer
6: List all books for a given customer

> 
```
Select '0' to return to main menu, '1' to list all customers in the database, '2' to find a customer by last name, '3' to create a new customer, '4' to update a specific customer, '5' to delete a specific customer, or '6' to list all books owned by a specific customer:

*1. List all customers*
```plaintext
> 1

last_name    first_name  
--------------------------
Jameson      James       
Dickens      Dick        
Johnson      John        
Williams     Wendy       
Summers      Sarah       
Emsworth     Emma 
```

*2. Find a customer by last name*
```plaintext
> 2

Enter the customer's last name: Summers

last_name    first_name  
--------------------------
Summers      Sarah  
```

*3. Create a customer*
```plaintext
> 3

Create a customer
--------------------
Enter the customer's first name: Bob
Enter the customer's last name: Roberts

Success: customer 'Bob Roberts' created
```
The new customer is displayed in the customers table:
```plaintext
> 1

last_name    first_name  
--------------------------
Jameson      James       
Dickens      Dick        
Johnson      John        
Williams     Wendy       
Summers      Sarah       
Emsworth     Emma        
Roberts      Bob  
```

*4. Update a customer*
```plaintext
> 4

Update a customer
-------------------
Enter the customer's last name: Roberts

Enter the customer's new first name: Phillip
Enter the customers's new last name: Roberts

Success: customer 'Phillip Roberts' updated
```
The updated name is displayed in the customers table:
```plaintext
> 1

last_name    first_name  
--------------------------
Jameson      James       
Dickens      Dick        
Johnson      John        
Williams     Wendy       
Summers      Sarah       
Emsworth     Emma        
Roberts      Phillip  
```

*5. Delete a customer*
```plaintext
> 5

Enter the customer's last name: Roberts

Customer 'Phillip Roberts' deleted
```
The deleted customer is removed from the customers table:
```plaintext
> 1

last_name    first_name  
--------------------------
Jameson      James       
Dickens      Dick        
Johnson      John        
Williams     Wendy       
Summers      Sarah       
Emsworth     Emma   
```

*6. List all books for a given customer*
```plaintext
> 6

Enter the customer's last name: Summers

title                       author                   bookstore   
------------------------------------------------------------------------
The Wind in the Willows     Kenneth Grahame          Read Queen          
The Grapes of Wrath         John Steinbeck           Read Queen          
Fahrenheit 451              Ray Bradbury             Read Queen    
```

**Note**: Both the Bookstore Manager menu and Book Manager menu have nearly identical options, just for bookstores or books instead of customers.

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

## Authors and Acknowledgement

The original application was designed and built by Connor D. Brown in 2023.
