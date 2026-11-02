# Testing Table

The group tested the program after each main feature was built. The table below shows ten test cases. The actual output matched the expected output in every case so every test passed.

| Test number | Feature tested | Input | Expected output | Actual output | Result |
|-------------|----------------|-------|-----------------|---------------|--------|
| 1 | Add order | Valid order details (ID 201, qty 2, price 4.00, Student, Paid) | Order added successfully | Order added successfully | Pass |
| 2 | Add order (duplicate ID) | Order ID 201 again | Message that the ID already exists | Message that the ID already exists | Pass |
| 3 | Empty field check | Order ID left blank | Message to type something and ask again | Message to type something and ask again | Pass |
| 4 | Invalid quantity | Quantity typed as "abc" | Message that it is not a valid number and ask again | Message that it is not a valid number and ask again | Pass |
| 5 | Negative price | Price typed as -5 | Message that the price must be 0 or more and ask again | Message that the price must be 0 or more and ask again | Pass |
| 6 | Calculate order total | Order 101 (qty 2, price 4.50, Student) | Subtotal 9.00, Discount 0.90, GST 0.81, Final 8.91 | Subtotal 9.00, Discount 0.90, GST 0.81, Final 8.91 | Pass |
| 7 | Search (existing ID) | Order ID 103 | Correct order displayed | Correct order displayed | Pass |
| 8 | Search (missing ID) | Order ID 999 | Message that no order was found | Message that no order was found | Pass |
| 9 | Show unpaid orders | Sample data loaded | Orders 102 and 104 listed as unpaid | Orders 102 and 104 listed as unpaid | Pass |
| 10 | Load missing file | Delete the data file then choose Load | Helpful message that no saved file was found | Helpful message that no saved file was found | Pass |

## Notes on debugging
During testing the group found two problems and fixed them.

First, an early version of the save function opened the file in read mode by mistake so nothing was saved. The group changed the mode to write mode and the data was then saved correctly. This matches the AI debugging entry in the AI-use log.

Second, an early version let the user add an order with a blank order ID. The group added a `get_required_text` function that asks again until the field is filled. Test number 3 checks this fix.

The calculation test (number 6) was confirmed by hand. The subtotal is 2 x 4.50 = 9.00. The Student discount is 10% so the discount is 0.90. The discounted subtotal is 8.10. The GST is 10% of 8.10 which is 0.81. The final total is 8.10 + 0.81 = 8.91.
