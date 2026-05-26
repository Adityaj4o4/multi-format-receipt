item = input("What is your order? ")
item = item.title().strip()
qty = float(input(f"How many of {item}s did you order? "))
cost1 = input(f"How much does one {item} cost? (in your unit U) ")
cost2 = float(cost1.strip("$"))
z = qty * cost2
print("--- RECEIPT ---")
print(f"Item: {item}")
print("QTY:", qty)
#Learned about using multiple format strings with this.
print(f"Total: U {z:,.2f}")
print("---------------")
