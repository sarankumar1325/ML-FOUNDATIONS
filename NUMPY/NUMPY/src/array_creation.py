def create_array_from_list(data):
    import numpy as np
    return np.array(data)

def create_zeros_array(shape):
    import numpy as np
    return np.zeros(shape)

def create_ones_array(shape):
    import numpy as np
    return np.ones(shape)

def create_identity_matrix(size):
    import numpy as np
    return np.eye(size)

def create_arange_array(start, stop, step):
    import numpy as np
    return np.arange(start, stop, step)

def index_array(arr, index):
    return arr[index]

def slice_array(arr, start, end):
    return arr[start:end]

# Example usage
if __name__ == "__main__":
    sample_array = create_array_from_list([1, 2, 3, 4, 5])
    print("Sample Array:", sample_array)
    
    zeros_array = create_zeros_array((2, 3))
    print("Zeros Array:\n", zeros_array)
    
    ones_array = create_ones_array((2, 3))
    print("Ones Array:\n", ones_array)
    
    identity_matrix = create_identity_matrix(3)
    print("Identity Matrix:\n", identity_matrix)
    
    arange_array = create_arange_array(0, 10, 2)
    print("Arange Array:", arange_array)
    
    indexed_value = index_array(sample_array, 2)
    print("Indexed Value:", indexed_value)
    
    sliced_array = slice_array(sample_array, 1, 4)
    print("Sliced Array:", sliced_array)