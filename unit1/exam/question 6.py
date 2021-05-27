print ("Program for calculate the area of a rectangle")

L = float(input("Join the length of the rectangle:... "))
W = float(input("Join the width of the rectangle:... "))
Area=0
if(L>0 and W>0):

    if (L==W):
        Area=L*W
        print("\nThis isn't a rectangle, it's a square.")
        print("\n The area is equal to:", Area)
     
    else: 
        if(L!=W):
            Area=L*W
            print ("\nThis is a rectangle")
            print ("\n The area of the rectangle is equal to:", Area)
else:
    print("\n 0 or less, cannot be a length or width, try with another number.")
