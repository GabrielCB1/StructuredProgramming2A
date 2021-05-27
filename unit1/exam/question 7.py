print ("\nProgram for calculate the greatest number between 3 different numbers")
print("\n")

num1 = float(input("Join the first number:... "))
num2 = float(input("Join the second number:... "))
num3 = float(input("Join the third number:... "))

if (num1==num2==num3):
    print("\nAll numbers are same", num1," ", num2, " ", num3)
elif (num1>num2):
    if (num1>num3):
        print ("\nthe first number is the largest one:", num1)
    else: 
        print ("\nThe third number is the largest one: ",num3)    
elif (num2>num3):
    print ("\nThe second number is the largest one: ",num2)
else: 
    print ("\nThe third number is the largest one: ",num3)