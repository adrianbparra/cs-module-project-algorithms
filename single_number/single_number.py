'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here

    # loop over the array
    for i in range(len(arr)): 
        # assign value that 
        j = 0
        # while j value is less than len of array
        while(j < len(arr)):
            
            # check if index is not same as j and index value is same as j value
            if (i != j and arr[i] == arr[j]): 
                # exit while loop to go to next for loop index
                break
            # update the j point
            j += 1

        # if j is equal to len of arr since the no item was found
        #   return the arr index value 

        if (j == len(arr)): 
            return arr[i] 
      

    

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")