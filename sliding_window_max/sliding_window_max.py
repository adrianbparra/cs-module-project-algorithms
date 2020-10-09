'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here

    # while going over nums we start at 0 and only access nums are nums k length
    # nums[cur:k]
    # it will not loop over all of them since curindex + k would be out of index
    
    newArr = []
    for x in range(len(nums) + 1 - k):
        
        newArr.append(max(nums[x:x+k]))

    return newArr


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
