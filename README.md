#Cafe Agastain – Restaurant Management System#

Description:
Cafe Agastain is a Python-based restaurant management system that allows a café or restaurant to manage its menu, orders, billing, and customer reviews. The project uses JSON files for data storage and provides a console-based interactive interface for customers and restaurant owners.


Features:
Show Menu: Displays the current menu with item prices and average customer reviews.
Order Items: Customers can order multiple items and choose quantities for each.
Update Menu: Password-protected functionality for the restaurant owner to update prices or add new items.
Show Cart: Displays current items in the customer's cart with total price and applied discounts.
Generate Bill & Add Review:Customers can optionally give ratings (1-5) for ordered items.
                           Reviews are merged with previous reviews to maintain an average rating.
                           Generates the final bill with automatic discounts:
                           10% off for orders above ₹1000
                           Exit: Close the application safely.
                           

Technologies Used:
Python 3.x
JSON for data storage

Key Highlights:
Console-based interactive interface with easy-to-use menu.
Secure owner authentication for menu updates.
Dynamic calculation of total price and automatic application of discounts.
Persistent storage of menu items and reviews using JSON files.

How to Run: 
1. Clone the repository:

          git clone <repository-url>

2.Ensure Python 3.x is installed on your system.

3.Run the main program:

           python Restaurant.py

Interact with the program using the options displayed in the console.

Use Case:
This project can be used by small cafés or restaurants to manage their menu, take orders, generate bills, and track customer feedback efficiently in a lightweight Python application.
