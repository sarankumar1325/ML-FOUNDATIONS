def add_arrays(arr1, arr2):
    return arr1 + arr2

def subtract_arrays(arr1, arr2):
    return arr1 - arr2

def multiply_arrays(arr1, arr2):
    return arr1 * arr2

def divide_arrays(arr1, arr2):
    if np.any(arr2 == 0):
        raise ValueError("Cannot divide by zero.")
    return arr1 / arr2

def main():
    print("Welcome to the NumPy Array Calculator!")
    print("Please enter two arrays in the format: [1, 2, 3]")

    arr1 = eval(input("Enter the first array: "))
    arr2 = eval(input("Enter the second array: "))

    arr1 = np.array(arr1)
    arr2 = np.array(arr2)

    print("\nSelect an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    if choice == '1':
        print("Result:", add_arrays(arr1, arr2))
    elif choice == '2':
        print("Result:", subtract_arrays(arr1, arr2))
    elif choice == '3':
        print("Result:", multiply_arrays(arr1, arr2))
    elif choice == '4':
        try:
            print("Result:", divide_arrays(arr1, arr2))
        except ValueError as e:
            print(e)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    import numpy as np
    main()