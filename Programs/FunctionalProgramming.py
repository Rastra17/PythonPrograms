# The left half of the colon is for the argument and the right half is for the function body
# nFactorial = lambda n : 1 if n == 0 else n * nFactorial(n - 1)

# The lambda function above can also be written as a normal function

def nFactorial(n):
    if(n == 0):
        return 1
    else:
        return n * nFactorial(n - 1)

# import time
# def timer(input_func, func_arg):
#     start = time.time()
#     input_func(func_arg)
#     end = time.time()
#     return end - start

# The normal function above converted to a lambda function

import time
timer = lambda input_func, func_arg : (time.time(), input_func(func_arg), time.time()) # This returns the start time, return value of the function and the end time in a tuple
TimeDifference = lambda start, end : end - start
tupleResult = timer(nFactorial, 900)
print("Took: %.5f s" %TimeDifference(tupleResult[0], tupleResult[2]))