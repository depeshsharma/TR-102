grocery = ["Milk", "Eggs", "Bread"]

while True:
    new = input("Enter a grocery item: ")
    if new in grocery:
        print(" Done.")
        break
    else:
        grocery.append(new)
        print(f"{new}")
print("\nFinal Grocery List:")
for item in grocery:
    print("-", item)
