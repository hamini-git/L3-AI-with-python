customer_name = "Hamini"    # Using the STRING data type
customer_age = 32           # Using the INTEGER data type
account_balance = 5000.75   # Using the FLOAT data type
is_account_active = True    # Using the BOOLEAN data type
print("*****Customer Account_details*****")
print("Customer Name:", customer_name)
print("Customer Age:", customer_age)
print("Account Balance: £", account_balance)
print("Account Active:",is_account_active)
transactions = ["Deposit", "Withdrawal", "Payment","Transfer"]
# Using the data structure List
account_details = ("Savings", "UK", "GBP")
# Using a TUPLE data structure
services = {"Online Banking", "ATM", "Mobile App"}
# Using a SET data structure
customer = {  # Using a DICTIONARY data structure
    "name": customer_name,
    "age": customer_age,
    "balance": account_balance,
    "active": is_account_active
}
customer["balance"] = customer["balance"] + 500 #using arithmetic '+'operator
print("Transactions:", transactions)
print("Account Details:", account_details)
print("Banking Services:", services)
print("Customer:", customer)
deposited = 600
withdrawn= 250
new_balance = account_balance  # using Assignment operator'='
#Arithmetic operators
new_balance = new_balance + deposited
new_balance = new_balance - withdrawn
double_deposit = deposited * 2
half_balance = new_balance / 2
remaining_balance = new_balance % 100
print("Double Deposit: £", double_deposit)
print("Half Balance: £", half_balance)
print("Remainder after dividing by 100: £", remaining_balance)
# Comparison operators
if new_balance > 3000:
    print("Balance is greater than £3000.")
elif new_balance < 5000:
    print("Balance is less than £5000.")
elif new_balance >= 3000:
    print("Balance is at least £3000.")
elif new_balance <= 4000:
    print("Balance is £4000 or less.")
elif new_balance == 3550.50:
    print("Balance is exactly £3550.50.")
elif new_balance != 1000:
    print("Balance is not £1000.")
else:
    print("Balance below the limit")

card_active = True
online_banking = True
if card_active and online_banking: # Logical operator AND
    print("All banking services are active.")
if new_balance < 1000 or not card_active: # Logical operators OR, NOT
    print("Account needs attention.")
if "Mobile Banking" in services: #using Membership operators
 print("Mobile Banking is available.")
else:
 print("Mobile Banking is not available.")
account_status = card_active
if account_status is card_active:    #using identity operator
    print("Account status is active.")
print("Available Balance:", new_balance)
