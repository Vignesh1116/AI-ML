import numpy as np

marks = np.array([90,35,56,78,93,67])

high_marks = marks[marks>=80]
print(high_marks)

result =np.where(marks>=50,"pass","fail") # where
print(result)

sorted = np.sort(marks) # sort
print(sorted)

