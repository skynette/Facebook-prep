

# hash table implementation 1
class HT:
	def __init__(self, capacity):
	# Creating Hashtable as a nested list. 
		self.capacity = capacity
		self.HashTable = [[] for _ in range(capacity)]

	# display hashtable in readable format O(n2) time
	def display_hash(self): 
		for i in range(len(self.HashTable)): 
			print(i, end = " ") 
			for j in self.HashTable[i]: 
				print("-->", end = " ") 
				print(j, end = " ") 
			print() 

	# Hashing Function to return key for every value. 
	def Hashing(self, keyvalue): 
		return (hash(keyvalue) % self.capacity)

	# Insert Function to add values to the hash table O(1) time
	def insert(self, keyvalue, value): 
		hash_key = self.Hashing(keyvalue) 
		self.HashTable[hash_key].append(value) 

# Driver Code 
ob = HT(40)
ob.insert("name", 'Allahabad') 
ob.insert(25, 'Mumbai') 
ob.insert(20, 'Mathura') 
ob.insert(9, 'Delhi') 
ob.insert(21, 'Punjab') 
ob.insert(21, 'Noida') 

# ob.display_hash() 


# hashtable implementation 2
class HashTable():
	# Time complexity of this operation is O(1)
	def __init__(self, capacity):
		self.table = capacity * [None]
		self.n = 0
		self.capacity = capacity
	# Time complexity of this operation is O(1)
	def hash_func(self, key):
		# get the index to store the data
		print("HAsh func spits", (hash(key)%len(self.table)))
		return (hash(key)%len(self.table))

	 # checks if ht is too populated
	 # Time complexity of this operation is O(1)
	def is_full(self):
		return self.n > len(self.table)/2

	# Time complexity of this operation is O(n2)
	# doubles the table length and re-add values
	def double(self):
		table2 = HashTable(capacity=len(self.table)*2)
		for i in range(len(self.table)):
			if self.table[i] is None:
				continue
			# if we get data copy all into new table
			for kvp in self.table[i]:
				table2[kvp[0]] = kvp[1]
		self.table = table2.table	# assign new table as table
		self.capacity = (len(self.table))
		print("doubles")

	# Time complexity of this operation is O(n) worst case scenario
	def __setitem__(self, key, value):
		if self.is_full():
			self.double()
		# add value to table by key
		index = self.hash_func(key)
		# meaning we already have an item here, meaning we either updating or adding new item
		# so check if this key already exists
		if self.table[index] is not None:
			for kvp in self.table[index]:
				# if we find a key then update to new value
				if kvp[0] == key:
					kvp[1] = value
					break
			# if no breaks were hit meaning new key found, just append to the end
			else:
				self.table[index].append([key, value])
				self.n+=1
			# empty index, then initiate new list there and append our key value pair
		else:
			self.table[index] = []
			self.table[index].append([key, value])
			self.n+=1

	# Time complexity of this operation is O(n)
	def __getitem__(self, key):
		# get a value by key
		index = self.hash_func(key)
		if self.table[index] is None:
			raise KeyError()
		else:
			# loop through all key-value pairs and find if our key exist, if it does return the value
			for kvp in self.table[index]:
				if kvp[0] == key:
					return kvp[1]
			# if at the end no return then key doesnt exist
			raise KeyError()
			
	def __len__(self):
		return self.n

	


ht = HashTable(10)

ht["name"] = "josh"
print(ht.table)
ht["sch"] = "uniben"
print(ht.table)
ht["level"] = 100
# print(ht.table)



# check palindrome
"""Given a string, determine if there is a way to arrange the string such that the string is a palindrome
if such an arrangement exists, return a palindrome otherwise return None"""

from collections import Counter
def check_palindrome(string):
	look_up = dict(Counter(string))
	even_pal = ""
	odd_char = ""
	for ch, count in look_up.items():
		if count % 2 == 0:
			even_pal += ch*(count//2)
		elif not odd_char:
			odd_char += ch
			even_pal += ch*(count//2)
		else:
			return None
	return even_pal + odd_char + even_pal[::-1]

# print(check_palindrome("aeiouaeiouq2"))

# count pairs with given sum
"""Given an array of integers, and a number ‘sum’, 
find the number of pairs of integers in the array whose sum is equal to ‘sum’."""
from collections import defaultdict
arr = [10, 12, 10, 15, -1, 7, 6, 5, 4, 2, 1, 1, 1,-4] 
k = 11
def numberOfWays(arr, k):
 	# Write your code here
  look_up = dict(Counter(arr))
  count = 0
  for i in range(len(arr)):
    try:
      count += look_up[k-arr[i]]
    except:
      count += 0
    if k - arr[i] == arr[i]:
      count-=1
  return int(count/2)