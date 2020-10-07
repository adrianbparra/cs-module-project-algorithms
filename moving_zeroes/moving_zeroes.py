'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here

    # loop over arr
        # if it encounter a zero move it the right

    # set a variable to start
    i = 0
    checked = 0
    while i < len(arr):
        # print(arr[i])

        # if checked values are equal or > than (array end - spot of loop)
        if checked >= ((len(arr) - 1) - i):
            # return arr since the rest are already accounted for zeros
            return arr

            # if found pop it and then append at the front
        if arr[i] == 0:
            zero = arr.pop(i)
            arr.append(zero)
            # update checked on that zero
            checked += 1
        else:
            # update spot to look
            i+= 1


# [3,1,0,-2,0]

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")