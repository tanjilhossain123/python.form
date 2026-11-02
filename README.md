# Cafe Ordering and Sales Tracker

## 1. Project title
Cafe Ordering and Sales Tracker

## 2. Group number
Group 02

## 3. Group members
| Name | Student ID |
|------|------------|
| Maisha Akter | 243507 |
| Tanjil Hossain Badol | 243562 |
| Apon Debnath | 243666 |
| Monirul Islam | 260257 |

## 4. Selected project option
Option 2 - Cafe Ordering and Sales Tracker

## 5. Brief description of the program
This is a text based Python program that helps a small cafe record customer orders and work out sales totals. The user picks options from a menu. The program can add an order and update an order. It can view every order and search for one order by its ID. It can calculate the total for one order using the discount and GST rules. It can list unpaid orders and show a daily sales summary. The orders can be saved to a text file and loaded back later so the data is not lost when the program closes.

## 6. List of features
1. Add a new order
2. Update an order
3. View all orders
4. Search for an order by order ID
5. Calculate order total (subtotal, discount, GST and final total)
6. Show unpaid orders
7. Show daily sales summary
8. Save data to file
9. Load data from file
10. Exit
11. Input validation for numbers, prices, discount type and payment status
12. Exception handling for a missing file and for invalid file data

## 7. How to run the program
1. Keep `main.py` and `sample_data.txt` in the same folder.
2. Open `main.py` in VS Code, IDLE or another Python environment. You can also upload it to Google Colab.
3. Run the program.
4. Choose option 9 first to load the sample orders. Then try the other menu options.
5. Choose option 8 to save your changes. Choose option 10 to exit.

The program needs Python 3. It uses only the standard library so nothing extra has to be installed.

## 8. Explanation of each file
| File | Purpose |
|------|---------|
| main.py | The full Python program. It holds the Order class, the menu and every feature function. |
| sample_data.txt | A sample data file with five orders. It lets you test the Load feature straight away. |
| README.md | This file. It explains the project and how to run it. |
| ai_use_log.md | Records how the group used AI during the project. |
| testing_table.md | Shows the test cases the group ran and the results. |
| order_total.js | The order total calculation converted into JavaScript. |
| language_comparison.md | Compares the Python code with the JavaScript version. |
| contribution_table.md | Shows the role and contribution of each member. |
| individual_reflections.md | Holds the reflection written by each member. |

The group chose one organised Python file instead of several files. The brief allows this. The file is split into clear sections with comments so each part is easy to find.

## 9. Known limitations
1. The data is stored in a plain text file so it is not protected and anyone can open it.
2. The save file uses "|" to separate fields. The program replaces any "|" that a user types with a space so the file is not broken.
3. There is no login screen so anyone who runs the program can see every order.
4. There is no delete feature because it was not required.
5. The daily sales summary counts every order in the file. It does not filter by a real date because the brief did not require date handling.

## 10. Summary of AI use
The group used an AI assistant for help during the project. The main uses were understanding the menu loop, debugging the file save function, improving the exception handling and converting the order total function into JavaScript. The group also used AI to help design test cases. Every AI suggestion was tested and checked by the group before it was kept. Full details are in `ai_use_log.md`.

## 11. Second language selected for comparison
JavaScript. The group converted the order total calculation. The converted code is in `order_total.js`. The comparison is in `language_comparison.md`.
