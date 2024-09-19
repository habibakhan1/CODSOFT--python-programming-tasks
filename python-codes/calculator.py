num1= int(input("enter a number: "))
num2= int(input("enter another number: "))

user= input("choose an operation you wish to perform: \n 1.Addition \n 2.Subtraction \n 3.Multiplication \n 4.Division \n 5.Remainder\n").lower()
if user == "addition":
    result=num1 + num2
    print("Addition:", result)
elif user == "subtraction":
    result= num1 - num2
    print("Subtraction:", result)
elif user == "multiplication":
    result= num1 * num2
    print("Multiplication:", result)
elif user == "division":
    if num2 != 0:
        result= num1/num2
        print("Division:", divide)
    else:
        print("division by 0 is not allowed, choose another number")
elif user == "remainder":
    if num2 != 0:
        result= num1%num2
        print("Remainder:", result)
    else:
        print("division by 0 is not allowed, choose another number")

else:
    print("Incorrect input, Please try again")

