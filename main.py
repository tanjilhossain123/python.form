# =========================================================
# Cafe Ordering and Sales Tracker
# BISY1003 - Assessment 2 - Option 2
# Beginner level Python program
# =========================================================
# This program lets a cafe add orders and view them. It can
# search orders and calculate totals with discount and GST.
# It can show unpaid orders and a daily sales summary. It can
# also save the orders to a text file and load them back.
# =========================================================


# ---------- Settings and lookup data ----------

# A dictionary that stores each discount type and its rate.
# "None" means 0%. "Student" means 10%. "Staff" means 15%.
# "Member" means 20%.
discount_rates = {
    "None": 0.0,
    "Student": 0.10,
    "Staff": 0.15,
    "Member": 0.20
}

GST_RATE = 0.10                 # GST is 10%
DATA_FILE = "sample_data.txt"   # the file used to save and load orders

# A list that holds all the Order objects while the program runs.
orders = []


# ---------- The Order class ----------
# One Order object stores all details for a single order.
class Order:
    def __init__(self, order_id, customer_name, item_name, quantity, item_price, discount_type, payment_status):
        self.order_id = order_id
        self.customer_name = customer_name
        self.item_name = item_name
        self.quantity = quantity
        self.item_price = item_price
        self.discount_type = discount_type
        self.payment_status = payment_status

    # subtotal = quantity x item price
    def get_subtotal(self):
        return self.quantity * self.item_price

    # discount amount = subtotal x discount rate
    def get_discount_amount(self):
        rate = discount_rates.get(self.discount_type, 0.0)
        return self.get_subtotal() * rate

    # discounted subtotal = subtotal - discount amount
    # This value is used for both GST and the final total.
    def get_discounted_subtotal(self):
        return self.get_subtotal() - self.get_discount_amount()

    # GST = 10% of the discounted subtotal
    def get_gst(self):
        return self.get_discounted_subtotal() * GST_RATE

    # final total = discounted subtotal + GST
    def get_final_total(self):
        return self.get_discounted_subtotal() + self.get_gst()


# ---------- Input helper functions ----------
# These keep asking the user until they type something valid.

def get_required_text(message):
    # Keep asking until the user types some text that is not blank.
    # Any "|" is replaced with a space because the save file uses
    # "|" to separate the fields on each line.
    while True:
        text = input(message).strip().replace("|", " ")
        if text != "":
            return text
        print("This field cannot be empty. Please type something.")


def get_valid_number(message):
    # Keep asking until the user types a whole number that is 0 or more.
    while True:
        try:
            value = int(input(message))
            if value < 0:
                print("Please enter a number that is 0 or more.")
            else:
                return value
        except ValueError:
            print("That is not a valid number. Please try again.")


def get_valid_price(message):
    # Keep asking until the user types a price that is 0 or more.
    while True:
        try:
            value = float(input(message))
            if value < 0:
                print("Please enter a price that is 0 or more.")
            else:
                return value
        except ValueError:
            print("That is not a valid price. Please try again.")


def get_discount_type():
    # Keep asking until the user types a valid discount type.
    print("Discount types: None, Student, Staff, Member")
    while True:
        choice = input("Enter discount type: ").strip().title()
        if choice in discount_rates:
            return choice
        print("Please enter None, Student, Staff or Member.")


def get_payment_status():
    # Keep asking until the user types Paid or Unpaid.
    while True:
        choice = input("Enter payment status (Paid or Unpaid): ").strip().title()
        if choice == "Paid" or choice == "Unpaid":
            return choice
        print("Please enter Paid or Unpaid.")


def find_order(order_id):
    # Look through the list and return the matching order. Return None
    # when no order has that ID.
    for order in orders:
        if order.order_id == order_id:
            return order
    return None


def print_order(order):
    # Print one order in a tidy way.
    print("-" * 40)
    print("Order ID      :", order.order_id)
    print("Customer      :", order.customer_name)
    print("Item          :", order.item_name)
    print("Quantity      :", order.quantity)
    print("Item price    : $" + format(order.item_price, ".2f"))
    print("Discount type :", order.discount_type)
    print("Payment status:", order.payment_status)
    print("Final total   : $" + format(order.get_final_total(), ".2f"))


# ---------- Menu feature functions ----------

def add_order():
    print("\n--- Add a new order ---")
    order_id = get_required_text("Enter order ID: ")

    # Stop if an order with this ID already exists.
    if find_order(order_id) is not None:
        print("An order with that ID already exists.")
        return

    customer_name = get_required_text("Enter customer name: ")
    item_name = get_required_text("Enter item name: ")
    quantity = get_valid_number("Enter quantity: ")
    item_price = get_valid_price("Enter item price: ")
    discount_type = get_discount_type()
    payment_status = get_payment_status()

    new_order = Order(order_id, customer_name, item_name, quantity, item_price, discount_type, payment_status)
    orders.append(new_order)
    print("Order added successfully.")


def update_order():
    print("\n--- Update an order ---")
    order_id = input("Enter the order ID to update: ").strip()
    order = find_order(order_id)

    if order is None:
        print("No order found with that ID.")
        return

    print("Leave a text box blank and press Enter to keep the old value.")

    new_name = input("New customer name: ").strip().replace("|", " ")
    if new_name != "":
        order.customer_name = new_name

    new_item = input("New item name: ").strip().replace("|", " ")
    if new_item != "":
        order.item_name = new_item

    # For numbers we ask yes or no first to keep it simple.
    change_qty = input("Change quantity? (yes/no): ").strip().lower()
    if change_qty == "yes":
        order.quantity = get_valid_number("Enter new quantity: ")

    change_price = input("Change item price? (yes/no): ").strip().lower()
    if change_price == "yes":
        order.item_price = get_valid_price("Enter new item price: ")

    change_discount = input("Change discount type? (yes/no): ").strip().lower()
    if change_discount == "yes":
        order.discount_type = get_discount_type()

    change_payment = input("Change payment status? (yes/no): ").strip().lower()
    if change_payment == "yes":
        order.payment_status = get_payment_status()

    print("Order updated successfully.")


def view_all_orders():
    print("\n--- All orders ---")
    if len(orders) == 0:
        print("There are no orders yet.")
        return
    for order in orders:
        print_order(order)


def search_order():
    print("\n--- Search for an order ---")
    order_id = input("Enter the order ID to search: ").strip()
    order = find_order(order_id)
    if order is None:
        print("No order found with that ID.")
    else:
        print_order(order)


def calculate_order_total():
    print("\n--- Calculate order total ---")
    order_id = input("Enter the order ID: ").strip()
    order = find_order(order_id)
    if order is None:
        print("No order found with that ID.")
        return
    print("Subtotal        : $" + format(order.get_subtotal(), ".2f"))
    print("Discount amount : $" + format(order.get_discount_amount(), ".2f"))
    print("GST (10%)       : $" + format(order.get_gst(), ".2f"))
    print("Final total     : $" + format(order.get_final_total(), ".2f"))


def show_unpaid_orders():
    print("\n--- Unpaid orders ---")
    found = False
    for order in orders:
        if order.payment_status == "Unpaid":
            print_order(order)
            found = True
    if not found:
        print("There are no unpaid orders.")


def show_daily_sales_summary():
    print("\n--- Daily sales summary ---")
    if len(orders) == 0:
        print("There are no orders yet.")
        return

    total_orders = len(orders)
    total_sales = 0.0
    total_paid = 0.0
    total_unpaid = 0.0
    total_discount = 0.0
    total_gst = 0.0

    # Add up the values from every order.
    for order in orders:
        total_sales += order.get_final_total()
        total_discount += order.get_discount_amount()
        total_gst += order.get_gst()
        if order.payment_status == "Paid":
            total_paid += order.get_final_total()
        else:
            total_unpaid += order.get_final_total()

    print("Total number of orders :", total_orders)
    print("Total discount given   : $" + format(total_discount, ".2f"))
    print("Total GST collected    : $" + format(total_gst, ".2f"))
    print("Total sales value      : $" + format(total_sales, ".2f"))
    print("Total paid sales       : $" + format(total_paid, ".2f"))
    print("Total unpaid sales     : $" + format(total_unpaid, ".2f"))


def save_data_to_file():
    # Save each order as one line of text. Fields are separated by "|".
    try:
        with open(DATA_FILE, "w") as file:
            for order in orders:
                line = (
                    order.order_id + "|" +
                    order.customer_name + "|" +
                    order.item_name + "|" +
                    str(order.quantity) + "|" +
                    str(order.item_price) + "|" +
                    order.discount_type + "|" +
                    order.payment_status
                )
                file.write(line + "\n")
        print("Data saved to", DATA_FILE)
    except OSError:
        print("Something went wrong while saving the file.")


def load_data_from_file():
    # Read the file and turn each line back into an Order object.
    try:
        with open(DATA_FILE, "r") as file:
            orders.clear()
            for line in file:
                line = line.strip()
                if line == "":
                    continue
                parts = line.split("|")
                if len(parts) != 7:
                    print("Skipped a line that did not have 7 fields.")
                    continue
                order_id = parts[0]
                customer_name = parts[1]
                item_name = parts[2]
                quantity = int(parts[3])
                item_price = float(parts[4])
                discount_type = parts[5]
                payment_status = parts[6]
                order = Order(order_id, customer_name, item_name, quantity, item_price, discount_type, payment_status)
                orders.append(order)
        print("Data loaded from", DATA_FILE)
    except FileNotFoundError:
        print("No saved file found yet. Please save data first.")
    except ValueError:
        print("The file has some invalid data that could not be read.")


# ---------- Menu and main loop ----------

def display_menu():
    print("\n===== Cafe Ordering and Sales Tracker =====")
    print("1. Add a new order")
    print("2. Update an order")
    print("3. View all orders")
    print("4. Search for an order")
    print("5. Calculate order total")
    print("6. Show unpaid orders")
    print("7. Show daily sales summary")
    print("8. Save data to file")
    print("9. Load data from file")
    print("10. Exit")


def main():
    # This loop keeps showing the menu until the user picks Exit.
    while True:
        display_menu()
        choice = input("Enter your choice (1-10): ").strip()

        if choice == "1":
            add_order()
        elif choice == "2":
            update_order()
        elif choice == "3":
            view_all_orders()
        elif choice == "4":
            search_order()
        elif choice == "5":
            calculate_order_total()
        elif choice == "6":
            show_unpaid_orders()
        elif choice == "7":
            show_daily_sales_summary()
        elif choice == "8":
            save_data_to_file()
        elif choice == "9":
            load_data_from_file()
        elif choice == "10":
            print("Thank you for using the program. Goodbye.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 10.")


# This guard means main() only runs when the file is run directly.
if __name__ == "__main__":
    main()
