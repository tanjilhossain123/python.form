# Individual Reflections

Each member wrote a short reflection of about 250 to 300 words.

---

## Maisha Akter (243507) - Menu and user interaction lead

I mainly worked on the menu and the user interaction for our Cafe Ordering and Sales Tracker. I built the main menu, the menu loop and the input helper functions that check what the user types. I also connected each menu number to the correct function.

The Python concepts I applied were input and output, loops, decisions and strings. I used a while loop to keep the menu running until the user chose exit. I used if and elif to send each choice to the right function. I used string methods like strip, title and lower to clean up the input.

I used AI to help me understand how a menu loop works. I asked it how to keep showing a menu until the user picks exit. AI helped by explaining a while True loop with a break at the end. This saved me time and made the idea clear.

AI got one thing wrong for my part. Its first example did not check for empty input so a blank order ID could still be added. I added a get_required_text function that asks again until the box is filled.

I checked my part by running every menu option in order. I typed wrong values on purpose to see if the program asked again instead of crashing.

I learned that loops and functions work together to keep a program organised. Small helper functions made the menu much cleaner.

From comparing Python with JavaScript I learned that both languages use loops and conditions in a similar way. The main difference is the braces and the semicolons in JavaScript.

Next time I would add a search by customer name as well as by order ID.

---

## Tanjil Hossain Badol (243562) - Logic and calculation lead

I mainly worked on the logic and the calculations for our Cafe Ordering and Sales Tracker. I wrote the methods that work out the subtotal, the discount amount, the GST and the final total. I also wrote the check for unpaid orders and the daily sales summary.

The Python concepts I applied were functions, arithmetic, Boolean logic, decisions and dictionaries. I used a dictionary to store the discount rates for None, Student, Staff and Member. I used multiplication and subtraction for the money maths. I used if and else to decide if an order was paid or unpaid.

I used AI to check my formula order. I asked whether GST should be worked out before or after the discount. AI helped by confirming that GST is taken on the discounted subtotal. This matched the brief.

AI did get one thing wrong. In an early answer it put the discount maths in two different places so the value was repeated. I fixed this by adding a get_discounted_subtotal method and using it in both the GST and the final total.

I checked my part by testing orders with known answers. For a Student order of 2 drinks at 4.50 I expected 8.91 and the program gave 8.91.

I learned that breaking the maths into small methods makes the code easier to read and to fix. I also learned how a dictionary is a fast way to look up a rate.

From comparing Python with JavaScript I learned that a dictionary and an object do the same job. The difference is that an object returns undefined for a missing key.

Next time I would add more discount types and let a manager edit the rates.

---

## Apon Debnath (243666) - Data storage and exception handling lead

I mainly worked on the data storage and the exception handling for our Cafe Ordering and Sales Tracker. I wrote the save function and the load function. I also added the error handling so the program does not crash when a file is missing or when the data is wrong.

The Python concepts I applied were files, exceptions, lists and strings. I opened a file in write mode to save and in read mode to load. I used a try and except block to catch a missing file. I used the split method to break each line into fields and I joined the fields with a separator when I saved.

I used AI to debug my save function. My first version did not save anything. AI told me the file was opened in read mode instead of write mode.

AI was mostly right but I still had to adapt the code. The AI example used commas as the separator. A customer name can contain a comma so I changed the separator to the "|" character and removed any "|" from the input.

I checked my part by saving a few orders and opening the text file to look at the lines. I also deleted the file and chose Load to confirm the program showed a helpful message instead of crashing.

I learned how file modes work and why exception handling matters. A program that handles errors is much safer to use.

From comparing Python with JavaScript I learned that both languages read and write files but the exact commands are different.

Next time I would save the data in a cleaner format such as CSV or JSON.

---

## Monirul Islam (260257) - Class design, testing and language comparison lead

I mainly worked on the class design, the testing and the language comparison for our Cafe Ordering and Sales Tracker. I designed the Order class that stores all the details for one order. I built the testing table and I converted the order total into JavaScript.

The Python concepts I applied were classes and objects, testing and debugging. I wrote the Order class with an __init__ method and several calculation methods. I used objects in a list so the program can hold many orders at once.

I used AI to help convert the Python calculation into JavaScript. I asked it to keep the same logic. AI gave me a working function with an object and toFixed for rounding.

AI got one part wrong for my work. The JavaScript it gave did not handle a missing discount type. A Python dictionary has a get method with a default but a JavaScript object does not. I added an if check for undefined so a missing type gives a rate of 0.

I checked my part by running the JavaScript in Node.js and comparing the result with Python. Both gave a final total of 8.91 so I knew the conversion was correct. I also ran all ten test cases on the program.

I learned how a class keeps related data and methods together. This made the whole program tidy.

From comparing Python with JavaScript I learned that the logic moves across easily but the syntax changes. Python uses indentation while JavaScript uses curly braces.

Next time I would convert more of the program such as the save function into JavaScript.
