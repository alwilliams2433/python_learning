import numpy
import scipy.linalg
import time

size = 1_000
buildTimeStart = time.time()
matrix = numpy.random.rand(size,size)
independent = numpy.random.rand(size,1)
buildTimeEnd = time.time()
print('Build time: ', buildTimeEnd - buildTimeStart)

solveTimeStart = time.time()
solution = scipy.linalg.solve(matrix, independent)
solveTimeEnd = time.time()
print('Solve time: ', solveTimeEnd - solveTimeStart)

print('Error2 = ', scipy.linalg.norm(matrix@solution-independent))
print('ErrorInf = ', scipy.linalg.norm(matrix@solution-independent, numpy.inf))
