'''

Basic Numpy Intro

'''


# 1. 
print('1. Importing NumPy as np\n')
import numpy as np                  


# 2.
a = np.arange(100)                  
print('2. a = NumPy array with 100 equally spaced values in the range 0 through 100 (not including 100)')
print(a)
print('')


# 3.
b = np.arange(0,100,10)
print('3. b = NumPy array with 10 equally spaced values in the range 0 through 100 (not including 100)')
print(b)
print('')


# 4. 
c = np.linspace(0,10,101,True)
print('4. c = NumPy array in the range 0 through 10 (inclusive) with values spaced at 0.1')
print(c)
print('')


# 5. 
d = np.random.random((10,10))
print('5. d = Random two-dimensional array with the dimensions 10 by 10')
print(d)
print('')


# 6. 
a = a.reshape(10,10)
print('6. a = Reshape a, two-dimensional array with the dimensions 10 by 10')
print(a)
print('')


# 7.
print('7. Results of a[4,5]:')
print(a[4,5])
print('')


# 8.
print('8. Results of a[4]:')
print(a[4])
print('')


# 9. 
print('9. Sum of d:')
print(np.sum(d))
print('')


# 10. 
print('10. Max of a:')
print(np.max(a))
print('')


# 11. 
print('11. Transpose of b:')
print(np.transpose(b))
print('')


# 12. 
print('12. Results of adding a and d:')
print(a+d)
print('')


# 13. 
print('13. Results of multiplying a and d:')
print(a*d)
print('')


# 14.
print('14. Results of computing the dot product of a and d:')
print(np.dot(a,d))
