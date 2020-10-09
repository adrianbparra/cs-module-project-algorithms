'''
Input: an integer
Returns: an integer
'''
cache = { }

# 2 1,1

def eating_cookies(n, default = 0):
    # Your code here
    
    # can eat either 1 ,2 or 3 cookies at a time

    # if n <= 1: return 1
    # if n == 2: return n

    # return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)

    ######################################## iterativly
    total = 1


    first = 1
    second = 2
    third = 4

    if n <= 1: return first
    if n == 2: return second
    if n == 3: return third

    total = 0

    for i in range(4, n+1):

        total = first + second + third

        first = second
        second = third
        third = total

    return total

'''
O(n) best
O(n^2)

1 cookie
    1
one way

2 cookies
    1,1
    2
2 ways

3 cookies
    1,1,1
    1,2
    2,1
    3
4 ways

4 cookies
    1,1,1,1
    1,1,2
    1,2,1
    2,1,1
    1,3
    3,1
    2,2
7 ways

5 cookies
    1,1,1,1,1
    1,1,1,2
    1,1,2,1
    1,2,1,1
    2,1,1,1
    1,2,2
    2,1,1
    1,2,1
    1,1,3
    1,3,1
    3,1,1
    2,3
    3,2
13 ways
'''

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
