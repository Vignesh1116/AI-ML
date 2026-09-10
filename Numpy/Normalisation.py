import numpy as np

marks = np.array([20, 40, 60, 80, 100])

minimum = np.min(marks)
maximum = np.max(marks)

normalized = (marks - minimum) / (maximum - minimum) # normalisation

print(normalized)