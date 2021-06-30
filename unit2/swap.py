import sys
a = 10
b = 20
print (f'initial values:{a},{b}')

def swap (param1,param2):
    global a
    global b 
    temp =a 
    a=b
    b=temp



if __name__ == "__main__":
    print ("swap program ")

    temp = a
    a=b
    b=temp
    print (f'values: a:{a}, b:{b}') 