from sys import argv as ag

def addToNumbers (number1, number2):
    print('StartProgram: addTonymbers executed...\n')
    result = number1+number2

    return result
answer = False
def isEven (aNumber):
    if (aNumber%2==0 ):
        return True
        #print ("It's even")
    else: 
        return False
        #print ("It's odd")

if __name__ == "__main__":
   # print ( f' Sum is equal to = {adToNumbers (int(ag[1])),int(ag[2]))}')
   n1 = int (input ('Join first number:\t'))
   n2 = int (input ('Join second number:\t'))

    # print (f'Sum is equal to = {addToNumbers (n1,n2) }')
    # answer = isEven ( addToNumbers (n1,n2))

    #isPrime (n1)
    #isPrime (n2)
  

    #if( isEven (addToNumbers (n1,n2) ) ):
       # print (f'N!: {n1} and N2: {n2} are your lucky numbers!')
    #else:
      #  print (f'N!: "{n1}" and N2: "{n2}"" are your lucky numbers!')

    #if(isPrime (n4 )):
       # print ("n4 is prime")    
    #else: 
        #print ("n4 is not prime")