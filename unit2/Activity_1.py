import sys

num1 = 9

def isPrime ( ):

    #def message():
        #print ("It is function")
    global num1
    num1=3
    def localFunction():
            print ("This is a local function")

    localFunction() ##
    message() ##

    print ("prime program")
    num_div=1
    count = 2 ##dos cuentas
    

    if(num1 == 1):
        print  ("It isn't a prime")
        exit()

    while (count <= num1) :

        if (num1 %count ==0):
            num_div +=1
        count +=1 

    if (num_div>2):

        return False
    else:
        return True

def message ( ):##GLOBAL
    print ("Global Var")


def powTwoNumbers (num1,num2):
    pownum1 = pow(num1,2)
    pownum2 = pow(num2,2)
    return pownum1

(a,b ) = ("hola", "gabriel")

if __name__ == "__main__":

    print (a,b)

    print(f' num1:{num1} ')

    print (isPrime( ))

    print(f'num1: {num1} ')

    print ( powTwoNumbers (2,3))
