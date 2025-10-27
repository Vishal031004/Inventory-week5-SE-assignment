"""
Final clean version of the Inventory Management System for Lab 5.
This code adheres to PEP 8, includes documentation, and fixes all
security, logic, and style issues reported by Pylint, Bandit, and Flake8.
"""

import json
from datetime import datetime


# The global stock_data variable is now removed and encapsulated in the class.


class InventorySystem:
    """
    Manages inventory data and operations.
    Encapsulates stock_data to eliminate the use of the global statement (Fixes W0603).
    """

    def __init__(self):
        """Initializes the inventory data dictionary."""
        self.stock_data = {}

    def add_item(self, item="default", qty=0, logs=None):
        """
        Adds a specified quantity of an item to the stock.
        Handles mutable default arguments and performs type validation.
        """
        if logs is None:
            logs = []

        # Added type validation to prevent runtime TypeError (Fixes E501 and logic)
        if not isinstance(item, str) or not isinstance(qty, int):
            print(f"Warning: Invalid type for item ({item}) or quantity ({qty}). "
                  "Skipping add.")
            return

        if not item:
            return

        self.stock_data[item] = self.stock_data.get(item, 0) + qty

        # Fix: Use f-string for cleaner formatting (C0209)
        logs.append(f"{datetime.now()}: Added {qty} of {item}")

    def remove_item(self, item, qty):
        """
        Removes a specified quantity of an item from the stock.
        Uses specific exception handling (Fixes W0702).
        """
        try:
            self.stock_data[item] -= qty
            if self.stock_data[item] <= 0:
                del self.stock_data[item]
        # Fix: Use specific exception (KeyError).
        except KeyError:
            print(f"Warning: Tried to remove {item} but it is not in stock.")

    def get_qty(self, item):
        """
        Gets the current quantity of a specific item.
        Uses .get() to prevent KeyError.
        """
        return self.stock_data.get(item, 0)

    def load_data(self, file="inventory.json"):
        """
        Loads inventory data from the specified JSON file.
        Uses the 'with' statement for safe resource handling (Fixes R1732).
        """
        try:
            # Fix: Use 'with' statement and specify encoding (R1732, W1514)
            with open(file, "r", encoding="utf-8") as f:
                self.stock_data = json.load(f)
        except FileNotFoundError:
            print(f"Warning: {file} not found. Starting with empty inventory.")
        except json.JSONDecodeError:
            print(f"Error: Could not decode JSON from {file}.")

    def save_data(self, file="inventory.json"):
        """
        Saves the current inventory data to the specified JSON file.
        Uses the 'with' statement for safe resource handling (Fixes R1732).
        """
        try:
            # Fix: Use 'with' statement and specify encoding (R1732, W1514)
            with open(file, "w", encoding="utf-8") as f:
                json.dump(self.stock_data, f, indent=4)
        except IOError as e:
            print(f"Error saving data: {e}")

    def print_data(self):
        """Prints a formatted report of all items and their quantities."""
        print("\n--- Items Report ---")
        for item, qty in self.stock_data.items():
            print(f"{item} -> {qty}")
        print("--------------------")

    def check_low_items(self, threshold=5):
        """Returns a list of items with stock below the given threshold."""
        result = []
        for item in self.stock_data:
            if self.stock_data[item] < threshold:
                result.append(item)
        return result


def main():
    """Main function to demonstrate inventory operations."""
    # FIX: Initialize the InventorySystem class
    inventory = InventorySystem()
    # All function calls now use the 'inventory' object
    inventory.add_item("apple", 10)
    inventory.add_item("banana", -2)
    inventory.add_item(123, "ten")  # Handled safely by type validation
    inventory.remove_item("apple", 3)
    inventory.remove_item("orange", 1)
    print("Apple stock:", inventory.get_qty("apple"))
    print("Low items:", inventory.check_low_items())
    inventory.save_data()
    inventory.load_data()
    inventory.print_data()
    # Fix: Removed dangerous eval() call (W0123)
    print("eval used")


if __name__ == "__main__":
    main()
