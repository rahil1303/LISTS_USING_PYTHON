myList = list(map(int,input("\n Enter the lis input values").strip().split()))
def firstsecond(list1):
  a = list1
  a.sort(reverse = True)
  print(a)
  first = a[0]
  second = None
  for element in list1:
    if element != first:
      second = element
      return first,second
 
firstsecond(myList)
