num = int (input("Join your number:... "))


if num % 2 == 0:
    result="This number is pair" 
    
else:
    result="This number is unpair"  

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
    print("\nThis number is prime")
    print ("\n",result)
else: 
    print ("\nThis number isn't prime")
    print ("\n",result)