food_items = ["Pizza", "Burger", "Pasta", "Sandwich", "Burger King"]

for item in food_items:
    if item == "Burger King":
        print("Found Burger King, stopping search.")
        break
    print(item)
