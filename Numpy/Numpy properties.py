import numpy as np

marks = np.array(
    [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
)

print(marks.shape)
print(marks.ndim)
print(marks.size)
print(marks.dtype)

# mathematical operations

print(marks+5)
print(marks-5)
print(marks*5)
print(marks/2)