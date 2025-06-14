list = [1,2,3,5,78,99,4,5,6,7,8]
list.sort()
print(list)
n = 8
index = 0
def search(list,n):
    l = 0
    u = len(list)-1
    global index
    while l<=u:
        mid = (l+u) // 2
        if(list[mid]==n):
            index = mid
            return True
        else:
            if list[mid] < n:
                l=mid+1
            else:
                u=mid-1

    return False

if search(list,n):
    print("found at index",index)
else:
    print("not found")