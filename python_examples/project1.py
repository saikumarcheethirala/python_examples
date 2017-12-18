from random import randint

def number():
  return randint(1,6)


#a=raw_input("do you want to continue:y/n ")

while True:
  print number()
  a=raw_input("do you want to continue:y/n ")
  if(a!="y"):
    break

