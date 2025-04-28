import time
import hashlib
import streamlit as st

# Define a Sales Ledger entry
class SalesEntry:
    def __init__(self, item, quantity, price_per_unit):
        self.item = item
        self.quantity = quantity
        self.price_per_unit = price_per_unit
        self.total = self.calculate_total()
        self.timestamp = time.ctime()

    # Calculate total sales for this entry
    def calculate_total(self):
        return self.quantity * self.price_per_unit

# Define the Sales Ledger
class SalesLedger:
    def __init__(self):
        self.ledger = []

    # Add new sale entry to the ledger
    def add_sale(self, item, quantity, price_per_unit):
        sale = SalesEntry(item, quantity, price_per_unit)
        self.ledger.append(sale)

    # Calculate hash of the ledger
    def calculate_hash(self):
        ledger_str = str(self.ledger)  # Convert ledger to string
        sha256_hash = hashlib.sha256(ledger_str.encode()).hexdigest()
        return sha256_hash

    # Display all sales in the ledger
    def display_ledger(self):
        ledger_data = []
        for entry in self.ledger:
            ledger_data.append({
                "Item": entry.item,
                "Quantity": entry.quantity,
                "Price per Unit": f"${entry.price_per_unit:.2f}",
                "Total": f"${entry.total:.2f}",
                "Timestamp": entry.timestamp
            })
        return ledger_data

# Create a Sales Ledger instance
store_ledger = SalesLedger()

# Streamlit UI to add sales entries
st.title("Sales Ledger Application")

# Input fields to add a new sale
st.header("Add a Sale")
item = st.text_input("Item Name")
quantity = st.number_input("Quantity", min_value=1, step=1)
price_per_unit = st.number_input("Price per Unit", min_value=0.01, step=0.01)

# Button to add the sale to the ledger
if st.button("Add Sale"):
    if item and quantity and price_per_unit:
        store_ledger.add_sale(item, quantity, price_per_unit)
        st.success(f"Sale of {item} added successfully!")
    else:
        st.error("Please fill in all the fields.")

# Display the ledger
if st.button("Show Ledger"):
    ledger_data = store_ledger.display_ledger()
    if ledger_data:
        st.subheader("Sales Ledger")
        st.write(ledger_data)
    else:
        st.warning("The ledger is empty.")

# Calculate and display the ledger hash
if st.button("Calculate Ledger Hash"):
    ledger_hash = store_ledger.calculate_hash()
    st.subheader("Ledger Hash")
    st.write(ledger_hash)
