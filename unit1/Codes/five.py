print ("start Program")
print ("\n")

price= float(input("what's the price of the product?: "))
percentage = float(input("What's the % of the product's tax?: ")) 

tax=percentage/100
taxT=price*tax
total=price+taxT

print ("\n")
print ("The tax to pay is: $",taxT,"\n")
print ("The final price of the product is: $",total,"\n")


print ("End Program")