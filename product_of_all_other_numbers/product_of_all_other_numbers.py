import math

'''
Input: a List of integers
Returns: a List of integers
'''

def product_of_all_other_numbers(arr):
    # Your code here

    # multiply the current number by all the other numbers
    # update current index as product
        

    # prod = 1
    # # loop over arr
    # for i in arr:
    # # get the product of all values
    #     prod *= i

    # # loop agian to update
    # for i in range(len(arr)):
    #     # divide the prod by the current index to remove
    #     arr[i] = prod / arr[i]

    # # return the arr
    # return arr
    ###################################

    newArr = []

    for i in range(len(arr)):
        product = math.prod(arr[:i] + arr[i+1:])
        newArr.append(product)
    return newArr
      
    # this is O(2n) can be done as O(n) without division

if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
