import sys
 
n = len(sys.argv)

sum=0
for i in range(1, n):
    sum += int(sys.argv[i])

n=n-1
average= sum/n

print("\nResult:", average)

     


     
