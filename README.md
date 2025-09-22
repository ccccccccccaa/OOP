# **Python Book Rental Management System**

This project is a comprehensive command-line application for managing a book rental store, developed entirely in Python. It utilizes Object-Oriented Programming (OOP) principles to handle customers, books, categories, and rental transactions through a robust, interactive menu.

The system supports different tiers of customers (Standard, Member, Gold Member) with unique discount and reward structures, making it a flexible solution for a small-scale rental business.

## **Project Overview**

The application is built around a set of core classes that model the real-world entities of a rental store:

* **Customer Management:** Defines Customer, Member, and GoldMember classes using inheritance. Each class has distinct attributes for managing discounts and rewards.  
* **Inventory Management:** Organizes books using Book, BookSeries, and BookCategory classes, allowing for a structured and easily updatable inventory.  
* **Transaction Handling:** The Rental class records every transaction, linking customers to the books they've rented.  
* **Main Controller:** The BookRentalSystem class serves as the main engine, presenting a user-friendly command-line interface (CLI) to interact with the system's features.

## **Key Features**

* **Interactive CLI Menu:** A simple, numbered menu for easy navigation and operation.  
* **Tiered Customer System:**  
  * Standard Customers (no benefits).  
  * Members (receive a flat discount on rentals).  
  * Gold Members (earn rewards points and receive discounts).  
* **Dynamic Rate Adjustment:** Ability for the administrator to update the discount rate for Members and the reward rate for Gold Members globally.  
* **Comprehensive Listings:** View lists of all registered customers, book categories, and available books (including series).  
* **Inventory Updates:** Modify the details of a book category and update the list of books associated with it.  
* **Bulk Processing:** Rent multiple books for various customers at once by processing a rentals.csv file.  
* **Reporting:** Display a complete history of all rental transactions and generate a list of VIP customers based on their rental activity.

## **How to Run**

### **Prerequisites**

* Python 3.6 or higher.

### **Instructions**

1. **Clone or download the repository.**  
2. **Navigate to the project directory** in your terminal.  
3. **Run the application** with the following command:  
   python ProgFunA2\_s3825008.py

4. The interactive menu will appear. Follow the on-screen prompts to use the system.

## **Usage Example**

Once the program is running, you will see a menu like this:

\======================  
Book Rental System Menu  
\======================  
1\. Rent a book  
2\. List all customers  
3\. List all book categories  
4\. List all books and book series  
5\. Update info of a category  
6\. Update books of a category  
7\. Adjust discount rate for members  
8\. Adjust reward rate for gold members  
9\. Rent books via a file  
10\. Display all rentals  
11\. Display VIP customers  
00\. Exit

Simply enter the number corresponding to your desired action and press Enter. The program will guide you through the required inputs.