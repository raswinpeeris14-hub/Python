name1 = input("Enter item 1 name: ")
qty1 = int(input("Enter quantity: "))
price1 = float(input("Enter price: ₹"))

item1_total=qty1*price1
print(f"total\t{item1_total}")

name2 = input("Enter item 2 name: ")
qty2 = int(input("Enter quantity: "))
price2 = float(input("Enter price: ₹"))

item2_total=qty2*price2
print(f"total\t{item2_total}")

name3 = input("Enter item 3 name: ")
qty3 = int(input("Enter quantity: "))
price3 = float(input("Enter price: ₹"))

item3_total=qty1*price1
print(f"total\t{item3_total}")

print("==============Recepit=================")
print(f"name1\t{name1}")
print(f"quantity\t{qty1}")
print(f"price\t{price1}")
print("\n")
print(f"name2\t{name2}")
print(f"quantity\t{qty2}")
print(f"price\t{price2}")
print("\n")
print(f"name3\t{name3}")
print(f"quantity\t{qty3}")
print(f"price\t{price3}")

total_amount=item1_total+item2_total+item3_total;
print(f"Total amount:{total_amount}");
discount_rate = total_amount - (total_amount * 0.10)
print(f"Discount:{discount_rate}");
