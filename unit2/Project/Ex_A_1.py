import sys
 
n = len(sys.argv)
n=n-1
print("Total arguments passed:", n)


Sum = 0

for i in range(1, n):
    Sum += int(sys.argv[i])


average=0

average= Sum/n

print("\n\nResult:", average)

     


     
