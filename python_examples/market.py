price={"apple":3,
 "mango":2,
"banana":4,
"cucumber":1
}

stock={
"apple":10,
"banana":5,
"mango":5,
"cucumber":10
}
itemslist={}
print "items list and stock of items"
for key in stock:
  print key+","
n=input("enter no of items want to purchase: ")

count=1
while count<=n:
  count=count+1
  addingitem=input("enter item you want to add: ")
  no_of_items=input("enter no of things: ")
  itemslist[addingitem]=no_of_items
  



#print itemslist  
total=0
for item in itemslist:
  if(stock[item]>0):
    total=total+price[item]*itemslist[item]
  else:
    print "item is not available %s" % item

print "the total cost of the purchasing items is %s" % total
