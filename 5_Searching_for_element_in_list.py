### Using Linear Search
myList6 = [10,20,30,40,50,60,70,80,90]
def searchinList(list,value):
    for i in list:
        if i == value:
            return list.index(value)
    return 'The value does not exist'

print(searchinList(myList6,20))

### Search Method
myList5 = [10,20,30,40,50,60,70,80,90]
if 20 in myList5:
    print(myList5.index(20))
else:
    print("The value is not in the list")
