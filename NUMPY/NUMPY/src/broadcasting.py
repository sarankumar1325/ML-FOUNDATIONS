def broadcasting_example_1():
    import numpy as np

    # Example of broadcasting with a 1D array and a 2D array
    a = np.array([1, 2, 3])
    b = np.array([[10], [20], [30]])

    # Broadcasting the 1D array to the shape of the 2D array
    result = a + b
    return result

def broadcasting_example_2():
    import numpy as np

    # Example of broadcasting with two 2D arrays of different shapes
    a = np.array([[1, 2, 3], [4, 5, 6]])
    b = np.array([[10], [20]])

    # Broadcasting the second array to match the shape of the first
    result = a * b
    return result

def broadcasting_rules():
    return """
    Broadcasting Rules:
    1. If the arrays have a different number of dimensions, the shape of the smaller-dimensional array is padded with ones on the left side.
    2. If the sizes of the dimensions are different, the array with size 1 in that dimension is stretched to match the size of the other array.
    3. If the sizes of the dimensions are different and neither is 1, an error is raised.
    """

# Example usage
if __name__ == "__main__":
    print("Broadcasting Example 1 Result:\n", broadcasting_example_1())
    print("Broadcasting Example 2 Result:\n", broadcasting_example_2())
    print(broadcasting_rules())