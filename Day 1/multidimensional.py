def sum_2d_array(arr):
   
    total = 0
    for row in arr:
        for element in row:
            total += element
    return total

def call():
    arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result = sum_2d_array(arr)
    print("The sum of all elements in the array is:", result)

call();
