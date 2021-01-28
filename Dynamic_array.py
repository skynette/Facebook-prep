"""
Implementing a Dynamic Array in python
"""

class DynamicArray:
	# ”””A dynamic array class akin to a simplified Python list.”””
	def __init__(self):
		# ”””Create an empty array.”””
		self.size=0 # count actual elements
		self.capacity = 1 # default array capacity
		self.Array = self.make_array(self.capacity) # low-level array

	def __len__(self):
		# ”””Return number of elements stored in the array.”””
		return self.size

	def __getitem__(self, k):
		# ”””Return element at index k.”””
		if not 0 <= k < self.size:
			raise IndexError("invalid index")
		return self.Array[k] # retrieve from array

	def append(self, obj):
		# ”””Add object to end of the array.”””
		if self.size == self.capacity: # not enough room
			self._resize(2 * self.capacity) # so double capacity
		self.Array[self.size] = obj
		self.size += 1

	def _resize(self, c): # nonpublic utitity
		# ”””Resize internal array to capacity c.”””
		B = [None]*c
		for k in range(self.size): # for each existing value
			B[k] = self.Array[k]
		self.Array=B # use the bigger array
		self.capacity = c

	def make_array(self, c):
		# ”””Return new array with capacity c.”””
		return [None]*c

import ctypes # provides low-level arrays
class DynamicArray2:
	# ”””A dynamic array class akin to a simplified Python list.”””
	def __init__(self):
	# ”””Create an empty array.”””
		self.n=0 # count actual elements
		self.capacity = 1 # default array capacity
		self.Array = self.make_array(self.capacity) # low-level array

	def __len__(self):
	# ”””Return number of elements stored in the array.”””
		return self.n
	
	def __getitem__(self, k):
	# ”””Return element at index k.”””
		if not 0 <= k < self.n:
			raise IndexError("invalid index")
		return self.Array[k] # retrieve from array
	
	def append(self, obj):
	# ”””Add object to end of the array.”””
		if self.n == self.capacity: # not enough room
			self.resize(2*self.capacity) # so double capacity
		self.Array[self.n] = obj
		self.n += 1

	def insert(self, k, value):
		# insert value at index k, shifting the subsequence values rightwards
		if self.n == self.capacity:		# not enough space
			self.resize(2*self.capacity)
		for j in range(self.n, k, -1):
			self.Array[j] = self.Array[j-1] # shift rightmost element
		self.Array[k] = value
		self.n+=1

	def resize(self, c): # nonpublic utitity
	# ”””Resize internal array to capacity c.”””
		B = self.make_array(c) # new (bigger) array
		for k in range(self.n): # for each existing value
			B[k] = self.Array[k] # copy items
		self.Array=B # use the bigger array
		self.capacity = c
	
	def make_array(self, c): # nonpublic utitity
	# ”””Return new array with capacity c.”””
		return (c*ctypes.py_object)()

a = DynamicArray2()
print(len(a))
a.append('1')
a.append('10')
a.append('41')
a.append('5')
a.append('99')
print(len(a))
print(a[0])
print(a[1])
