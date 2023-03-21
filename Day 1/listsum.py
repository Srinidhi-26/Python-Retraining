def sum_array(arr):
    total = 0
    for num in arr:
        total += num
    return total

def callArray():
    my_array = [1, 2, 3, 4, 5,6,7]
    array_sum = sum_array(my_array)
    print(array_sum)  

callArray();