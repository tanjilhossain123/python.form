# Programming Language Comparison: Python and JavaScript

## 1. What was converted
The group converted the order total calculation from the Cafe Ordering and Sales Tracker. This part works out the subtotal, the discount amount, the GST and the final total for one order. It is a good part to convert because it uses variables, a lookup table, arithmetic and a return value. These features exist in both languages so the comparison is clear.

## 2. Original Python code
```python
discount_rates = {
    "None": 0.0,
    "Student": 0.10,
    "Staff": 0.15,
    "Member": 0.20
}

GST_RATE = 0.10

def get_subtotal(quantity, item_price):
    return quantity * item_price

def get_order_total(quantity, item_price, discount_type):
    subtotal = quantity * item_price
    rate = discount_rates.get(discount_type, 0.0)
    discount_amount = subtotal * rate
    discounted_subtotal = subtotal - discount_amount
    gst = discounted_subtotal * GST_RATE
    final_total = discounted_subtotal + gst
    return final_total
```

## 3. Converted JavaScript code
```javascript
const discountRates = {
  "None": 0.0,
  "Student": 0.10,
  "Staff": 0.15,
  "Member": 0.20
};

const GST_RATE = 0.10;

function calculateOrderTotal(quantity, itemPrice, discountType) {
  let subtotal = quantity * itemPrice;
  let rate = discountRates[discountType];
  if (rate === undefined) {
    rate = 0.0;
  }
  let discountAmount = subtotal * rate;
  let discountedSubtotal = subtotal - discountAmount;
  let gst = discountedSubtotal * GST_RATE;
  let finalTotal = discountedSubtotal + gst;
  return finalTotal;
}
```

Both versions were run with the same input (quantity 2, price 4.50, discount type "Student"). Both returned a final total of 8.91 so the logic matches.

## 4. Comparison table
| Point | Python | JavaScript |
|-------|--------|------------|
| Define a function | uses `def` | uses the `function` keyword |
| Variables | created by name with no keyword | created with `let` or `const` |
| Lookup table | a dictionary with `{ }` | an object with `{ }` |
| Missing key | `.get(key, 0.0)` gives a default | returns `undefined` so a check is needed |
| End of a line | a new line ends a statement | a semicolon ends a statement |
| Code blocks | shown by indentation | shown by curly braces `{ }` |
| Round a number | `format(x, ".2f")` | `x.toFixed(2)` |

## 5. Similarities
The overall logic is the same in both languages. The maths is written in the same order and each step gives the same result. Both languages store the discount rates in a key and value structure. Python calls it a dictionary and JavaScript calls it an object (Python Software Foundation, 2025; Mozilla, 2025). Both use simple arithmetic operators such as `*`, `-` and `+`. Both put the work inside a function that takes inputs and returns one answer. A function in both languages helps the group reuse the code and keep it tidy.

## 6. Differences
The clearest difference is how each language shows code blocks. Python uses indentation while JavaScript uses curly braces (Mozilla, 2025). Variables are also handled in a different way. JavaScript asks for `let` or `const` in front of a new variable while Python does not need a keyword. Another difference is how a missing key is handled. The Python dictionary has a `.get` method that can return a default value. The JavaScript object returns `undefined` for a missing key so the group added an `if` check to set the rate to 0. Ending a line is different too. JavaScript normally ends a statement with a semicolon while Python ends a statement at the end of the line (Python Software Foundation, 2025). Rounding also uses different built in tools in each language.

## 7. What the group learned
The group learned that the thinking behind a program moves easily from one language to another even when the exact words change. The group also learned to read the rules of a new language with care. Small differences such as `undefined` and the need for `let` can cause bugs if they are missed. Running the JavaScript code in Node.js (OpenJS Foundation, 2025) helped the group check the output against the Python result and confirm the two versions agree.

## References
Mozilla. (2025). JavaScript reference. MDN Web Docs. https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference

OpenJS Foundation. (2025). Node.js documentation. https://nodejs.org/en/docs

Python Software Foundation. (2025). The Python standard library. https://docs.python.org/3/library/
