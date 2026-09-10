from numpy import append
import numpy as np

marks = np.array([10,20,30]) #update
marks[0] = 5

print(marks)

marks = np.append(marks,40) #append

print(marks)

marks = np.insert(marks,1,100) #insert

print(marks)

marks = np.delete(marks,1) #delete

print(marks)