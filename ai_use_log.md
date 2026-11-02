# AI-Use Log

AI tools were allowed in this assessment. The group used an AI assistant for help but checked and tested every suggestion. The group wrote the final code and understands it. Each entry below records one AI interaction.

**Please edit these entries so they match the exact prompts your group actually used. The log must be honest.**

---

### Entry 1
| Item | Detail |
|------|--------|
| AI tool used | ChatGPT |
| Purpose | Explanation |
| Prompt used | "How does a menu loop work in Python that keeps showing options until the user chooses exit?" |
| AI response summary | The AI explained a `while True` loop with `if` and `elif` for each choice and a `break` for exit. |
| Accepted or rejected | Accepted the idea |
| Verification | The group built the loop and ran every menu option to check each one worked. |
| Changes made | The group renamed the functions to match the cafe project and added option numbers 1 to 10. |
| Learning | We learned how a `while True` loop keeps the menu running until `break` is reached. |

---

### Entry 2
| Item | Detail |
|------|--------|
| AI tool used | ChatGPT |
| Purpose | Debugging |
| Prompt used | "Why is my Python program not saving records to the file?" |
| AI response summary | The AI suggested the file was opened in read mode instead of write mode. |
| Accepted or rejected | Accepted the suggestion |
| Verification | The group saved three orders and opened the text file to confirm the data was there. |
| Changes made | Changed `open(filename, "r")` to `open(filename, "w")` in the save function. |
| Learning | We learned the difference between read mode and write mode. |

---

### Entry 3
| Item | Detail |
|------|--------|
| AI tool used | ChatGPT |
| Purpose | Coding support |
| Prompt used | "How do I stop my Python program from crashing when the user types text instead of a number?" |
| AI response summary | The AI explained a `try` and `except ValueError` block around `int(input(...))`. |
| Accepted or rejected | Accepted the idea |
| Verification | The group typed "abc" for a quantity and checked the program asked again instead of crashing. |
| Changes made | The group put the try and except inside a loop so the question repeats until the input is valid. |
| Learning | We learned how exception handling keeps a program running after a bad input. |

---

### Entry 4
| Item | Detail |
|------|--------|
| AI tool used | ChatGPT |
| Purpose | Coding support |
| Prompt used | "What is a safe character to separate fields when I save records to a text file?" |
| AI response summary | The AI suggested using a character that users rarely type and removing it from any input. It gave the "|" symbol as one example. |
| Accepted or rejected | Accepted with a change |
| Verification | The group saved and loaded orders with commas in the names and confirmed the file still loaded. |
| Changes made | The group used "|" as the separator and replaced any "|" typed by the user with a space. |
| Learning | We learned why the separator character must not appear inside the data. |

---

### Entry 5
| Item | Detail |
|------|--------|
| AI tool used | ChatGPT |
| Purpose | Conversion |
| Prompt used | "Convert this Python order total function into JavaScript and keep the same logic." |
| AI response summary | The AI returned a JavaScript function with an object for the discount rates and `toFixed(2)` for rounding. |
| Accepted or rejected | Accepted with a change |
| Verification | The group ran the JavaScript in Node.js and compared the output with the Python output. Both gave 8.91. |
| Changes made | The group added an `if` check for `undefined` because a JavaScript object has no `.get` default. |
| Learning | We learned that a Python dictionary and a JavaScript object handle a missing key in a different way. |

---

### Entry 6
| Item | Detail |
|------|--------|
| AI tool used | ChatGPT |
| Purpose | Testing |
| Prompt used | "Suggest good test cases for a cafe ordering program with add, search, calculate and file features." |
| AI response summary | The AI suggested testing valid input, invalid input, a missing record and a missing file. |
| Accepted or rejected | Accepted the ideas |
| Verification | The group ran each suggested test on the real program and recorded the actual output. |
| Changes made | The group added extra tests for a duplicate order ID and a negative price. |
| Learning | We learned to test both correct input and wrong input, not only the cases that work. |
