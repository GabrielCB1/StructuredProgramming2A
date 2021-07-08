import sys
import random as rd

myList = list()
otherList = [] ## otherList[100] = {};
myInt = 3

if __name__ == "__main__":
    print("DataStructures!") 
    print (type(myList))
    print (type(otherList)) 
    myList.append("Data1")
    myList.append("Data2")
    myList.append("Data3")
    myList.append("Data4")
    myList.append("Data5")

    #print(myList [0])

    

    for index in range (0,len(myList)):
        print (f'myList[{index}]:',myList[index], "Current Index: ",index)

    for it in range (0, 11):
         otherList.append(rd.randint(0,100) )


    myList.extend(otherList)

           



    print (myList)
    #myList.pop()
    myList.reverse()
    print (myList)

    newList = myList [0::5]

    usersAdmin = [
        "Luis",
        "Rafa",
        "Jorge",
        "Jesus"
    ]
    print (usersAdmin)

    print (usersAdmin[0].lower())
    usersAdmin[0] = usersAdmin[0].lower()


    for usuario in usersAdmin:
        print(usuario, type(usuario))
        
    for element in range (0, len(usersAdmin)):
        if (usersAdmin [element].isupper()):
            print(f'usersAdmin[{element}] modificated')
            usersAdmin [element] = usersAdmin[element].lower()


            print (usersAdmin[element], type (usuario))

      

    print(usersAdmin)
   
    
