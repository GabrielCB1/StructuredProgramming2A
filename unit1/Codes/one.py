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