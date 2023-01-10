#Program to perform Conditional statements and for loop in python

x = input("Enter an alphabet in range of a,b,c: ")  #input alphabet from user
if x == "a":                                        #nested elif to check whether alphabet is a,b or c
	print("Alphabet is a")
elif x == "b":
	print("Alphabet is b")
else:
	print("Alphabet is c")

x = input("Enter a number: ")                       #input a number from user
if x > "5":                                         #check whether number is greater than or less than 5 
	print("Number is greater than 5")
else:
	print("Number is smaller than 5")

for i in range(1,6):                                #for loop to print numbers from 1 to 5
	print(i)