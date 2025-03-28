print("Welcome to this Program by LeadwithPius")
print("This program will enable you perform an arithmetic operation of your choice from the list between two integers")
operation= ["1.Add","2.Subtract","3.Divide","4.Multiply"]
print(operation)
num1= int(input("Enter first integer"))
num2= int(input("Enter second integer"))
mode= input("Please type in the number of your preferred operation to be performed")
if mode == "1":
    result= num1+num2
    print(result )
elif mode== "2":
    result= num1- num2
    print(result)
elif mode== "3":
    if num2 != 0:
        result= num1/num2
        print(result)
    else:
        print("Error: Division by zero is undefined")
elif mode== "4":
    result= num1*num2
    print(result)
else:
    print("Choice is out of scope")
