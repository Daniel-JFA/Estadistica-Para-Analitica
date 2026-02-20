import numpy as np

#creacion basica
a = np.array([1, 2, 3])
b = np.array([(1, 2, 3), (1, 2, 3)])

#placeholders
c = np.zeros(5)

print(a)
print(b)
print(c)


#vector 

d = (2,3)
e = (4,5)

type(d)

print(type(e))

f = np.array(d+e)

print(f)