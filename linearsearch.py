from time import sleep
arr = [1,2,3,4,5,6,7,8]

for i in arr:
    if i%2==0:
        print(i)
    i+=1
    sleep(1)