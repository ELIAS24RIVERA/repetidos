def shell_sort (arr):
    n = len(arr)
    gap = n // 2
    #reduce el valor de gap hasta 1
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            # desplasa los elementos a la deracha
            while j >= gap and arr[j - gap] > temp: 
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
arr = [23, 12, 1, 8, 34, 54, 2, 3]
print("antes de ordenar:", arr)
shell_sort(arr)
print("despues de ordenar:", arr)