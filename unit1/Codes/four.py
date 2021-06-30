print ("start Program")
print("\n")
num= float(input("Insert temperature in Fahrenheit:... "))

rest=num-32
div= 5/9
Cel=rest*div

print ("\n")
print (num,"°F is equal to:","{:.3f}".format(Cel),"°C\n")

print ("End Program")