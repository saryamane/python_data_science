#!/usr/bin/python

type(1)
type(2.5)
type(True)
"""The type tells whats the datatype of the paramter passed"""

# Python lists

k = [1 , 'b', True]
k[2]
print k

# You can have lists of lists
a = [[1,2,3],4,5]
print a[0]

# Python tuples, these are the immutable one's

x = (a, 'a', 2.5)
print x[1]

# x[1] = 'b' # This should give an error, since it is a tuple and immutable.

# Python sets, removes duplicate for you.

y = set([1,1,2,3,4,5,5,8])

print y

a = [1,1,1,1,4,5,6,77,8,8,8,77]

z = list(set(a))

print z

# Python dictionaries, un-ordered collections of key-value pairs. keys are immutable.

info = {'name': 'Samir', 'age': 54, 'kids': ['Tunnu', 'Tunni']}

print info['kids']

num_kids = len(info['kids'])
print num_kids

# Some of the important python packages for use.

import numpy as np

np.array([1,2,3])

# Numpy arrays are faster as they are stored in contigigous memory location.

print dir(np) # Will give you the contents within the dir space in numpy.

# All elements stored within numpy array, should be of the same type.

data = np.array([[1,2,3,4], [2,4,9]])

print data

print data[0]

# You can also load csv data into np.genfromtxt package.

dtypes = (int, int, int, float)

housing_data = np.genfromtxt('housing-data.csv', delimiter=',', names = True, dtype=dtypes)

print housing_data.dtype

print housing_data[0]

print housing_data[0][3] # prints the 4th column of the first row.

# housing_data[[:,1]] # Print all rows second column

print housing_data[['sqft', 'price']]

# Trick to get the normal list of tupes, we do.

print zip(housing_data['sqft'], housing_data['price'])

# Or if you want a regular numpy array.

print np.array([list(a) for a in zip(housing_data['sqft'], housing_data['price'])])








