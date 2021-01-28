

def URLify(st):
	# split the string in a list
	ls = st.split()
	# join all items in the list with desired delimeter
	ans = "%20".join(ls)
	return ans

def URLify2(st):
	ls = list(st)
	for i in range(len(st)):
		if ls[i] == " ":
			ls[i] = "%20"
	ls = "".join(ls)
	return ls

# sort both strings and compare the length
def CheckPerm(string1, string2):
	string1 = sorted(string1)
	string2 = sorted(string2)
	if len(string1) == len(string2):
		return True
	return False

# keep a table for the letters and their counts for both and compare
from collections import Counter
def CheckPerm2(string1, string2):
	table1 = dict(Counter(string1))
	table2 = dict(Counter(string2))
	if table1 == table2:
		return True
	return False

def PanlidromePerm(string):
	string = string.lower()
	string = string.replace(" ", "")
	ans = 0
	table = dict(Counter(string))
	if len(string)%2 == 0:
		for count in table.values():
			if count%2 != 0:
				return False
	for count in table.values():
		if count%2 != 0:
			ans+=1
			if ans>1:
				return False
	return True

def PanlidromePerm2(string):
	string = string.lower()
	string = string.replace(" ", "")
	string = dict(Counter(string))
	ans = 0
	for count in string.values():
		if count%2 != 0:
			ans+=1
	return ans<=1

"Check if a string can be made a palidrome by deleting one char"
"""Simply checking if character at left matches corresponding right until it doesn't. 
At that point we have a choice of either deleting the left or right character. 
If either returns Palindrome, we return true. To generalize this to more than one deletes,
we can simply replace the flag "deleted" to be a counter initialized to how many characters
we are allowed to delete and stop allowing for recursive calls when it reaches 0.
"""
def validPalindrome(self, s: str) -> bool:
	def verify(s, left, right, deleted):
		while left < right:
			if s[left] != s[right]:
				if deleted:
					return False
				else:
					return verify(s, left+1, right, True) or verify(s, left, right-1, True)
			else:
				left += 1
				right -= 1
		return True
	return verify(s, 0, len(s)-1, False)
# from itertools import groupby

# data = list(input())
# counts = []
# nums = []

# for num, count in groupby(data):
# 	counts.append(len(tuple(count)))
# 	nums.append((num))

# answer = list(zip(counts, nums))
# for i in answer:
# 	# print(i, end=" ")
# 	a, b = i
# 	print("{0}{1}".format(b,a), end="")

# Move Zeroes
# Given an array nums, write a function to move all 0's to the end of it 
# while maintaining the relative order of the non-zero elements.
class Solution:
	def moveZeroes(self, nums: List[int]) -> None:
		"""
		Do not return anything, modify nums in-place instead.
		"""
		# head is where we wanna put non zero elements.
		head = 0
		# count is num of zeroes we want to append at the end
		count = 0
		for i in range(len(nums)):
			if nums[i] != 0:
				nums[head] = nums[i]
				head+=1
			else:
				count+=1
		for i in range(1, count+1):
			nums[-i] = 0
		return


# find duplicate numbers in O(n) time and O(1) space
# Python3 program for the above approach 

# Function to find the duplicate 
# value in the given array arr[] 
def findDuplicate(arr): 

	# Initialise variables 
	tortoise = arr[0] 
	hare = arr[0] 

	# Loop till we find the 
	# duplicate element 
	while (1): 

		tortoise = arr[tortoise] 
		# Hare moves with twice 
		# the speed of tortoise 
		hare = arr[arr[hare]]
		if (tortoise == hare): 
			break

	tortoise = arr[0] 

	# Loop to get start point 
	# of the cycle as start 
	# point will be the duplicate 
	# element 
	while (tortoise != hare): 
		tortoise = arr[tortoise] 
		hare = arr[hare] 

	# Print the duplicate element 
	print (tortoise) 

# Driver Code 

# Given array 
arr = [ 2, 6, 4, 1, 3, 1, 5 ] 

# Function Call 
findDuplicate(arr) 

# This code is contributed by PratikBasu 
class Solution:
	def findDuplicate(self, nums: List[int]) -> int:
		t, h = nums[0], nums[nums[0]]
		while t != h: 
			t, h = nums[t], nums[nums[h]]
		t = 0
		while t != h:
			t, h = nums[t], nums[h]
		return t
		
		
# - Junaid Mansuri
# (LeetCode ID)@hotmail.com

# My solution
class Solution:
	def findDuplicate(self, nums: List[int]) -> int:
		tortoise = nums[0]
		hare = nums[nums[0]]
		
		while tortoise != hare:
			# advance hare twice as fast as tortoise
			# the hare will eventually meet the tortise then
			# break the loop
			tortoise = nums[tortoise]
			hare = nums[nums[hare]]
		
		# start tortoise from zero index 
		tortoise = 0
		
		while tortoise != hare:
			# advance both pointers one step and they will
			# meet at start of loop
			tortoise = nums[tortoise]
			hare = nums[hare]
		
		return tortoise


def verify_alien_dictionary(words, order):
	lookup = {}
	for index, val in enumerate(order):
		lookup[val] = index
	for i in range(len(words)-1):
		word1 = words[i]
		word2 = words[i+1]
		# Find the first difference word1[k] != word2[k].
		for i in range(min(len(word1), len(word2))):
			# If they compare badly, it's not sorted.
			if word1[i] != word2[i]:
				if lookup[word1[i]] > lookup[word2[i]]:
					return False
				break
		else:
			# If we didn't find a first difference, the
            # words are like ("app", "apple")
			if len(word1) > len(word2):
				return False
	return True