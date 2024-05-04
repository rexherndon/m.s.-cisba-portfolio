import numpy as np

# Convert list to an Numpy array
simple_list = [1, 2, 3]
array = np.array(simple_list)
print(array)
print(type(array))


# Convert multidimensional list to a numpy array
print(f"\n-----Multidimensional array")
multidimensional_list = [
    [1,2,3],
    [4,5,6]
]
array = np.array(multidimensional_list)
print(array)
print(type(array))
print(f"Dimensions are {array.shape}")


# Initializing arrays with default values
# specify the dimensions and data type
print(f"\n-----Initializing arrays")
array = np.zeros((2,4), dtype=int)
print(array)
array = np.ones((2,4), dtype=int)
print(array)
array = np.full((2,4), 99, dtype=int)
print(array)
# array of random numbers
# Pylint may complain about the method np.random.random
# ignore Pylint's complaint and run your code anyway.
# Search google for an explanation of the bug
# in Pylint if interested
array = np.random.random((2,4))
print(array)

# Accessing elements in the array
print(f"\n-----Accessing elements in the arrray")
print(array[0,0])
print(array[0,1])
print(array[1,0])
print(array[1,1])

# loop through every element in the array
print(f"\n-----Loop through elements in array")
for element in array:
    # Note: Each element is a list inside the array
    print(element)

print("\n")
print("-"*30)
# Comparison opoerators on numpy
print(array > 0.2)

# Filtering array values using comparison operators
print(array[array > 0.2])

# Math operations on numpy
print(np.round(array))

print("\n")
print("-"*30)

# How to perform math operations on an array, easily.
first = np.array([1,2,3])
second = np.array([1,2,3])
print(first + second)
print (first - second)
print(first * second)
print(first + 100)


print(f"\n----convert inches to cm")
dimensions_inch = np.array([1,2,3])
dimensions_cm = dimensions_inch * 2.54
print(dimensions_cm)


print(f"\n----convert inches to cm")
dimensions_cm = [x * 2.54 for x in dimensions_inch]
print(dimensions_cm)