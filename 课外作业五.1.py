from numpy import *
A = [[1,0.5,5],[2.3,2,3],[4,1,1.7]]
A = mat(A)
A = A.I
b = [[1,2,3]]
b = mat(b)
b = b.T
x = A*b
print(x)