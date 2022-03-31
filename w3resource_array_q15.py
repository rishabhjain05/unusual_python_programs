# Write a Python program to find the first duplicate element in a given array of integers. Return -1 If there are no such elements.

def new_sol(main_arr):
    arr_new = []
    
    list.sort(main_arr)
    i = 0
    for x in main_arr:
        if(main_arr[i]!= main_arr[i+1]):
            print("No duplicates")
    
    for x in main_arr:
        if x not in arr_new:
            arr_new.append(x)
        elif x in arr_new:
            print("first duplicate element is: ",x)
            break

new_sol([1,2,3,4,4,1])
print(arr_new)
