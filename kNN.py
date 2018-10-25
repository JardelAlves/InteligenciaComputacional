import numpy as np

X = np.array(([3,5], [5,1], [10,2]), dtype=float)
Y = np.array(([75], [82], [93]), dtype=float)

X = X/np.amax(X, axis=0)
Y = Y/100

print (X, '\n\n', Y)
