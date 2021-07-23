import sys


sensorInput = input("$GPGGA,134658.00,5106.9792,N,11402.3003,W,2,09,1.0,1048.47,M,-16.27,M,08,AAAA*60")
sensor_list = sensorInput.split(" ")
hourInput = input("11, 19, 34")
hour_list = hourInput.split(" ")

if __name__ == "__name__":
        print("GPS Activity!")
        print("\n")
        ##convert inputs to list ##

        print( "Header Config: $GPGGA - ", sensor_list[0] )
        for sensor in sensor_list:
          print(sensor)

        print( "hour: - ", hour_list[0] )
        for hour in hour_list:
          print(hour)



## 
number_list = []
n = int(input("Enter the list size "))

print("\n")
for i in range(0, n):
    print("Enter number at index", i, )
    item = int(input())
    number_list.append(item)
print("User list is ", number_list)