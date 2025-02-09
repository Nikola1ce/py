def quick(arr):
    if len(arr)<=1:
        return arr
    temp =arr[0]
    low = [x for x in arr[1:] if x<=temp]
    high =[x for x in arr[1:] if x>temp]
    return quick(low)+[temp]+quick(high)

arr=[2,3,1,7,4,5,8]

sort = quick(arr)
print(sort)

def down(arr,n,i):
    largest = i
    left =2*i+1
    right =2*i+2
    
    if left<n and arr[left]>arr[largest]:
        largest=left
    
    if right<n and arr[right]>arr[largest]:
        largest=right
        
    if largest!=i:
        arr[i],arr[largest]=arr[largest],arr[i]
        down(arr,n,largest)

def heapsort(arr):
    n=len(arr)
    for i in range(n//2-1,-1,-1):
        down(arr,n,i)
        
    for i in range(n-1,0,-1):
        arr[i],arr[0]=arr[0],arr[i]
        down(arr,i,0)

heapsort(arr)
print(arr)     
    