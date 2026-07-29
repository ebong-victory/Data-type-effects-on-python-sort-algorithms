# **********************************************************
# DATA TYPE RESEARCH PROJECT
# SORTING AND SEARCHING APPLICATION
# ***********************************************************

# IMPORT LIBRARIES
import pandas as pd
import time
from Algorithms import sorting_algorithm as st, Bubble_Sort as bs, Merge_Sort as ms, Quick_sort as qs

#load data set

data = pd.read_csv("Global Superstore.csv", encoding= 'latin1')
print("\n Data loaded successfully!\n Number of records", len(data))

#Display

while True:

    print("\n************************************************")
    print("SORTING ALGORITHM TEST APPLICATION")
    print("*************************************************")
    

        
    print("Welcome to the test algorithm and save data menu")
            

    try: 
        test_value = int(input("Enter the number of times you would like to test the sorting algorithms:  "))
        if test_value < 1:
            raise ValueError(f"{test_value} can not be less than 1!")
        
    except ValueError as e:
        print(f"{e} Try again")
    else:
        print(f"You have entered {test_value}\n")

            
             
    dataColumns = ["Sales", "Shipping Cost", "Customer Name"]

                
    ### Merge Sort  ###
    print("Merge Sort Started....")

    ### Integer ###
    mergeSortIntegerExecTime = []

    for i in range (test_value):

        data_list = data[dataColumns[0]].dropna().tolist()
        sorted_data, exec_time = st(ms, data_list)
        mergeSortIntegerExecTime.append(exec_time)

    print(f"Interger Sort completed {test_value} times")

    with open ("MergeSortIntergerValues.txt", "w") as file:
        for items in mergeSortIntegerExecTime:
            file.write(f"{items}\n")

                
    ### Float ###
    mergeSortFloatExecTime = []

    for i in range (test_value):

        data_list = data[dataColumns[1]].dropna().tolist()
        sorted_data, exec_time = st(ms, data_list)
        mergeSortFloatExecTime.append(exec_time)

    print(f"Float Sort completed {test_value} times")

    with open ("MergeSortFloatValues.txt", "w") as file:
        for items in mergeSortFloatExecTime:
            file.write(f"{items}\n")

                
    ### String ###
    mergeSortStringExecTime = []

    for i in range (test_value):

        data_list = data[dataColumns[2]].dropna().tolist()
        sorted_data, exec_time = st(ms, data_list)
        mergeSortStringExecTime.append(exec_time)

    print(f"String Sort completed {test_value} times")

    with open ("MergeSortStringValues.txt", "w") as file:
        for items in mergeSortStringExecTime:
            file.write(f"{items}\n")

                

    ### Quick Sort  ###
    print("\nQuick Sort Started....")

    ### Integer ###
    quickSortIntegerExecTime = []

    for i in range (test_value):

        data_list = data[dataColumns[0]].dropna().tolist()
        sorted_data, exec_time = st(qs, data_list)
        quickSortIntegerExecTime.append(exec_time)

    print(f"Interger Sort completed {test_value} times")

    with open ("QuickSortIntergerValues.txt", "w") as file:
        for items in quickSortIntegerExecTime:
            file.write(f"{items}\n")


    ### Float ###
    quickSortFloatExecTime = []

    for i in range (test_value):

        data_list = data[dataColumns[1]].dropna().tolist()
        sorted_data, exec_time = st(qs, data_list)
        quickSortFloatExecTime.append(exec_time)

    print(f"Float Sort completed {test_value} times")

    with open ("QuickSortFloatValues.txt", "w") as file:
        for items in quickSortFloatExecTime:
            file.write(f"{items}\n")

                
    ### String ###
    quickSortStringExecTime = []

    for i in range (test_value):

        data_list = data[dataColumns[2]].dropna().tolist()
        sorted_data, exec_time = st(qs, data_list)
        quickSortStringExecTime.append(exec_time)

    print(f"String Sort completed {test_value} times")

    with open ("QuickSortStringValues.txt", "w") as file:
        for items in quickSortStringExecTime:
            file.write(f"{items}\n")

            
    #### Bubble Sort #####
    print("\nBubble Sort Started.....")

    #### Integer ####
    BubbleSortIntegerExecTime = []
                
    for i in range(test_value):
                
        data_list = data[dataColumns[0]].dropna().tolist()
        sorted_data, exec_time,  = st(bs, data_list)
        BubbleSortIntegerExecTime.append(exec_time)
                
    print(f"Integer Sort completed {test_value} times")

    with open("BubbleSortIntegerValues.txt", "w") as file:
        for items in BubbleSortIntegerExecTime:
            file.write(f"{items}\n")

    ### Float ###
    BubbleSortFloatExecTime = []

    for i in range(test_value):
                    
        data_list = data[dataColumns[1]].dropna().tolist()
        sorted_data, exec_time = st(bs, data_list)
        BubbleSortFloatExecTime.append(exec_time)

    print(f"Float Sort completed {test_value} times")

    with open("BubbleSortFloatValues.txt", "w") as file:
        for items in BubbleSortFloatExecTime:
            file.write(f"{items}\n")

    ### String ###
    BubbleSortStringExecTime = []

    for i in range(test_value):
                
        data_list = data[dataColumns[2]].dropna().tolist()
        sorted_data, exec_time = st(bs, data_list)
        BubbleSortStringExecTime.append(exec_time)

    print(f"String Sort Completed {test_value} times")

    with open("BubbleSortStringValues.txt", "w") as file:
        for items in BubbleSortStringExecTime:
            file.write(f"{items}\n")


                
    print("\nTest Completed. Values have been saved to their respective text files")
    print("\nProgram Exited Successfully!")

    break
    

    
