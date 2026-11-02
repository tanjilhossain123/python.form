// =========================================================
// Cafe Ordering and Sales Tracker
// JavaScript version of the order total calculation
// Converted from the Python Order class calculation methods
// BISY1003 - Assessment 2 - Option 2
// =========================================================

// The discount rates stored in an object.
// This works like the Python dictionary.
const discountRates = {
  "None": 0.0,
  "Student": 0.10,
  "Staff": 0.15,
  "Member": 0.20
};

const GST_RATE = 0.10; // GST is 10%

// This function does the same job as the Python calculation methods.
// It returns the subtotal, discount, GST and final total.
function calculateOrderTotal(quantity, itemPrice, discountType) {
  // subtotal = quantity x item price
  let subtotal = quantity * itemPrice;

  // Look up the discount rate. Use 0 when the type is not found.
  let rate = discountRates[discountType];
  if (rate === undefined) {
    rate = 0.0;
  }

  let discountAmount = subtotal * rate;
  let discountedSubtotal = subtotal - discountAmount;
  let gst = discountedSubtotal * GST_RATE;
  let finalTotal = discountedSubtotal + gst;

  return {
    subtotal: subtotal,
    discountAmount: discountAmount,
    gst: gst,
    finalTotal: finalTotal
  };
}

// Example use with the same values as order 101 in the Python version.
let result = calculateOrderTotal(2, 4.50, "Student");

console.log("Subtotal        : $" + result.subtotal.toFixed(2));
console.log("Discount amount : $" + result.discountAmount.toFixed(2));
console.log("GST (10%)       : $" + result.gst.toFixed(2));
console.log("Final total     : $" + result.finalTotal.toFixed(2));

// Expected output:
// Subtotal        : $9.00
// Discount amount : $0.90
// GST (10%)       : $0.81
// Final total     : $8.91
