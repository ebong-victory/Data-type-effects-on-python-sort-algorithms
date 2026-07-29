import time

#Sorting algorithms

#Bubble sort algorithm

def Bubble_Sort(arr):
    for i in range(len(arr)):
        
        for j in range(0, len(arr) - i - 1):

            if arr[j] > arr[j+1]:

                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return arr

#Merge Sort

def Merge_Sort(arr):

    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2

    left = Merge_Sort(arr[:mid])
    right = Merge_Sort(arr[mid:])


    def Merge(left, right):
        result = []

        i,j = 0,0

        while(i < len(left) and j < len(right)):
            if left[i] < right [j]:
                result.append(left[i])
                i += 1

            else:
                result.append(right[j])
                j += 1
        
        result.extend(left[i:])
        result.extend(right[j:])

        return result


    return Merge(left, right)


# Quick Sort

def Quick_sort(arr):

    if len(arr) <= 1:
        return arr
    

    pivot = arr[len(arr) // 2]

    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return Quick_sort(left) + mid + Quick_sort(right)


# Sorting algorithm choice

def sorting_algorithm(sort_function, data_list):

    copied_list = data_list.copy()
    
    start_time = time.process_time()

    sorted_list = sort_function(copied_list)
    
    end_time = time.process_time()

    execution_time = end_time - start_time

    return sorted_list, execution_time
        




