numdays = int(input("How many day's temperature?"))
total = 0
for i in range(1,numdays+1):
    nextday = int(input("Day " + str(i) + "s high temp"))
    total += nextday


avg = round(total//numdays,2)
print("\n Average =" + str(avg))
