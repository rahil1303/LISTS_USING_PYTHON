shoppingList = ["Milk", "Cheese", "Butter"]
print(shoppingList[1])

## Acessing using IN operator
print("Milk" in shoppingList)
print("Bread" in shoppingList)

print(shoppingList[-1])
print(shoppingList[-2])


## Traversing the List
for i in shoppingList:
    print(i)

### Method 2 ## Range function always follows upto n - 1
for i in range(len(shoppingList)):
    shoppingList[i] = shoppingList[i]+"+"
    print(shoppingList[i])
