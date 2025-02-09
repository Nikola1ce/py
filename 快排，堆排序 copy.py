def quick(arr):
    n =len(arr)
    if n<=1:
        return arr
    temp = arr[0]
    
    less =[x for x in arr[1:] if x<=temp ]
    more =[x for x in arr[1:] if x>temp ]
    
    return quick(less)+[temp]+quick(more)

arr=[3,2,6,4,1,7,9,2]

print(quick(arr))    

def down(arr,n,i):
    largest =i
    left =2*i+1
    right =2*i+2
    
    if left<n and arr[left]>arr[largest]:
        largest=left
    if right<n and arr[right]>arr[largest]:
        largest=right
    if largest!=i:
        arr[largest],arr[i]=arr[i],arr[largest]
        down(arr,n,largest)
        
def heapsort(arr):
    n =len(arr)
    for i in range(n//2-1,-1,-1):
        down(arr,n,i)
        
    for i in range(n-1,0,-1):
        arr[i],arr[0]=arr[0],arr[i]
        down(arr,i,0)
        
heapsort(arr)
print(arr)