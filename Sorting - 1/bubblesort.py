def bubblesort(arr):
    n = len(arr)
    for i in range(n-1,-1,-1):
        swapp = False
        for j in range(i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapp = True
        if not(swapp):
            break
    return arr

if __name__ == "__main__":
    arr = [13, 46, 24, 52, 20, 9]
    print("Before Using Bubble Sort:")
    print(" ".join(map(str, arr)))
    print(bubblesort(arr))
