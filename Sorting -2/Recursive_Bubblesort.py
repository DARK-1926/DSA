def rbubble(arr,n):
    if n==1:
        return
    swapped = False
    for i in range(n-1):
        if arr[i]>arr[i+1]:
            arr[i],arr[i+1]=arr[i+1],arr[i]
            swapped =True
    if not(swapped):
        return
    rbubble(arr,n-1)
arr = [13, 46, 24, 52, 20, 9]
print("Before Using Bubble Sort:")
print(arr)

rbubble(arr, len(arr))

print("After Using Bubble Sort:")
print(arr)
