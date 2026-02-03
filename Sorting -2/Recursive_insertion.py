def rinsertion(arr,i,n):
    if n==i:
        return
    j=i
    while j>0 and arr[j-1]>arr[j]:
        arr[j-1],arr[j]=arr[j],arr[j-1]
        j-=1
    rinsertion(arr,i+1,n)

arr = [13, 46, 24, 52, 20, 9]
n = len(arr)

print("Before Using Insertion Sort:")
print(arr)

rinsertion(arr, 0, n)

print("After Using Insertion Sort:")
print(arr)
