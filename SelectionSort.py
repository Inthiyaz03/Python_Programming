def sort():
    for i in range(len(list)-1):
        minpos = i
        for j in range(i,len(list)):
            if(list[j] < list[minpos]):
                minpos = j
        temp = list[i]
        list[i] = list[minpos]
        list[minpos] = temp

list = [1,3,4,2,6,7,5,8,53,53,2]
sort()
print(list)