#Program to perform arithmetic operation by accepting values from user

m = int(input("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Remainder\n6.Exponent\n"))   #Ask user which operation should be performed
match m:                                                                                               #Execute operation by matching the number corresponding to operation
	case 1:
 		a = input("Enter 1st number: ")
 		b = input("Enter 2nd number: ")
 		print("Addition of numbers", int(a) + int(b))
	case 2:
 		a = input("Enter 1st number: ")
 		b = input("Enter 2nd number: ")
 		print("Difference of numbers: ", int(a) - int(b))
	case 3:
 		a = input("Enter 1st number: ")
 		b = input("Enter 2nd number: ")
 		print("Product of numbers: ", int(a) * int(b))
	case 4:
 		a = input("Enter 1st number: ")
 		b = input("Enter 2nd number: ")
 		print("Division of numbers: ", int(a) / int(b))
	case 5:
 		a = input("Enter 1st number: ")
 		b = input("Enter 2nd number: ")
 		print("Remainder of numbers: ", int(a) % int(b))
	case 6:
 		a = input("Enter Base: ")
 		b = input("Enter Power: ")
 		print("Result", int(a) ** int(b))