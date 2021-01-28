# My implementation

class Queue():
	def __init__(self):
		self.items = []
	def data(self):
		return self.items
	def enqueue(self, item):
		self.items.append(item)
	def dequeue(self):
		self.items.remove(self.items[0])
	def first(self):
		return self.items[0]
	def is_empty(self):
		return self.items == []
	def __len__(self):
		return len(self.items)

# A better approach, use of circlular array
class ArrayQueue():
	DEFAULTY_CAPACITY = 10

	def __init__(self):
		self.data = [None]*ArrayQueue.DEFAULTY_CAPACITY
		self.size = 0
		self.front = 0

	def __len__(self):
		return self.size
	def is_empty(self):
		return self.size == 0
	def first(self):
		if not self.is_empty():
			return self.data[self.front]
	def dequeue(self):
		if not self.is_empty():
			answer = self.data[self.front]
			self.data[self.front] = None
			self.front = (self.front+1)%len(self.data)
			self.size -= 1
			return answer
	def enqueue(self, item):
		if self.size == len(self.data):
			self.resize(2*len(self.data))
		avail = (self.front + self.size)%len(self.data)
		self.data[avail] = item
		self.size += 1
	def resize(self, capacity):
		old = self.data
		self.data = [None]*capacity
		walk = self.front
		for k in range(self.size):
			self.data[k] = old[walk]
			walk = (1+walk)%len(old)
		self.front = 0

