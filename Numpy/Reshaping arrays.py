import numpy as np

num = np.array([1,2,3,4,5,6])

new_array = num.reshape(3,2) # reshape

print(new_array)

flat = new_array.flatten() 
print(flat)