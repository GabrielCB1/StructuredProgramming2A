import sys

lower = int(input("Enter lower range limit:"))
upper = int(input("Enter upper range limit:"))


for i in range(lower, upper+1):
   if((i%3==0) & (i%5==0)):
      print(i)

exit(1)