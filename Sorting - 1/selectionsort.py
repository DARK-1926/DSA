def selectionsort(arr):
    n = len(arr)
    for i in range(n-1):
        a = i
        for j in range(i+1,n):
            if arr[j]<arr[a]:
                a = j
        arr[i],arr[a] = arr[a],arr[i]
    print("After selection sort:")
    print(*arr)


# Driver code
arr = [13, 46, 24, 52, 20, 9]

# Print array before sorting
print("Before selection sort:")
print(*arr)

# Call selection sort
selectionsort(arr)