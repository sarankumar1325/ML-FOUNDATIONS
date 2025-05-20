def add_arrays(a, b):
    return a + b

def subtract_arrays(a, b):
    return a - b

def multiply_arrays(a, b):
    return a * b

def divide_arrays(a, b):
    return a / b

def apply_function(arr, func):
    return func(arr)

def vectorized_square(arr):
    return apply_function(arr, lambda x: x ** 2)

def vectorized_sqrt(arr):
    return apply_function(arr, lambda x: x ** 0.5)

def vectorized_exp(arr):
    return apply_function(arr, lambda x: 2.71828 ** x)  # e^x

def vectorized_log(arr):
    return apply_function(arr, lambda x: 2.71828 ** x)  # ln(x)