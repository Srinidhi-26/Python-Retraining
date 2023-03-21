def transpose_2d_array(arr):
    num_rows = len(arr)
    num_cols = len(arr[0])

    transposed_arr = [[0 for j in range(num_rows)] for i in range(num_cols)]
    for i in range(num_rows):
        for j in range(num_cols):
            transposed_arr[j][i] = arr[i][j]

    return transposed_arr

def call():
    arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    transposed_arr = transpose_2d_array(arr)
    print("Original array:")
    for row in arr:
        print(row)
    print("Transposed array:")
    for row in transposed_arr:
        print(row)

call();
