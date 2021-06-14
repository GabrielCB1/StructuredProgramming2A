from sys import argv

lista = ["Red", "Black", "White"]

lista2 = [i for i in range (1,101) if i%2==0]
listaEvenOdd = [i for i in range (1,101) if i%2==1]

print (lista2)
print ("-------------------------")
print (listaEvenOdd)

if __name__ == "__main__":
    print( f'\nprogramName: {argv[0]} \n' )

    print (lista,  len (lista) ) #Sise ofa  list



    # print (lista [0] ) - Individual 
    # print (lista [1] )
    # print (lista [2] )

    index = 0
    while (index < len (lista) ):
        print ( f'index: {index}, value: {lista[index]}')
        index = index+1
    
    print ("-------------------------") 

    for index in range (0, len (lista)):
        print ( f'index: {index}, value: {lista[index]}')


num = int (input("Join your number:... "))

def evaluar_primo(num):
    contador=0
    resultado=True
    for i in range (1, num+1):
        if (num%i==0):
            contador  +=1
        if (contador>2):
            resultado=False 
            break
    return resultado 
if (evaluar_primo(num)==True):
    print("This number is prime")
else: 
    print ("This number isn't prime")        





    
 
    
