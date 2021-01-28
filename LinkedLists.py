from time import sleep
"""
A linked list is an ordered collection of values. 
Linked lists are similar to arrays in the sense that they contain objects in a linear order. 
However they differ from arrays in their memory layout.
"""
class DListNode:
	"""
	A node in a doubly-linked list.
	"""
	def __init__(self, data=None, prev=None, next=None):
		self.data = data
		self.prev = prev
		self.next = next

	def __repr__(self):
		return repr(self.data)


class DoublyLinkedList:
	def __init__(self):
		"""
		Create a new doubly linked list.
		Takes O(1) time.
		"""
		self.head = None

	def __repr__(self):
		"""
		Return a string representation of the list.
		Takes O(n) time.
		"""
		nodes = []
		curr = self.head
		while curr:
			nodes.append(repr(curr))
			curr = curr.next
		return '[' + ', '.join(nodes) + ']'

	def prepend(self, data):
		"""
		Insert a new element at the beginning of the list.
		Takes O(1) time.
		"""
		new_head = DListNode(data=data, next=self.head)
		if self.head:
			self.head.prev = new_head
		self.head = new_head

	def append(self, data):
		"""
		Insert a new element at the end of the list.
		Takes O(n) time.
		"""
		if not self.head:
			self.head = DListNode(data=data)
			return
		curr = self.head
		while curr.next:
			curr = curr.next
		curr.next = DListNode(data=data, prev=curr)

	def find(self, key):
		"""
		Search for the first element with `data` matching
		`key`. Return the element or `None` if not found.
		Takes O(n) time.
		"""
		curr = self.head
		while curr and curr.data != key:
			curr = curr.next
		return curr  # Will be None if not found

	def remove_elem(self, node):
		"""
		Unlink an element from the list.
		Takes O(1) time.
		"""
		if node.prev:
			node.prev.next = node.next
		if node.next:
			node.next.prev = node.prev
		if node is self.head:
			self.head = node.next
		node.prev = None
		node.next = None

	def remove(self, key):
		"""
		Remove the first occurrence of `key` in the list.
		Takes O(n) time.
		"""
		elem = self.find(key)
		if not elem:
			return
		self.remove_elem(elem)

	def reverse(self):
		"""
		Reverse the list in-place.
		Takes O(n) time.
		"""
		curr = self.head
		prev_node = None
		while curr:
			prev_node = curr.prev
			curr.prev = curr.next
			curr.next = prev_node
			curr = curr.prev
		self.head = prev_node.prev



class ListNode:
	"""docstring for ListNode"""
	def __init__(self, data=None, next_node=None):
		self.data = data
		self.next_node = next_node

	def __repr__(self):
		return repr(self.data)
	
class LinkedList:
	def __init__(self):
		self.head = None

	def __repr__(self):
		# str representation of list takes O(n) time
		nodes = []
		curr = self.head
		while curr:
			nodes.append(repr(curr))
			curr = curr.next_node
		return '[' + ' -> '.join(nodes) + ']'

	def prepend(self, data):
		# insert a new element at start of list O(1) time
		self.head = ListNode(data=data, next_node=self.head)

	def append(self, data):
		# insert element at end of list takes O(n) time
		if not self.head:
			self.head = ListNode(data=data)
			return
		curr = self.head
		while curr.next_node:
			curr = curr.next_node
		curr.next_node = ListNode(data=data)

	def remove(self, key):
		# removes first occurence of key in the list takes O(n) time.
		# find the element and keep a reference to the element before it
		curr = self.head
		prev = None
		print("head is", self.head)
		print("prev is", prev)
		print()
		sleep(1)
		while curr and curr.data != key:
			print("curr is {} and curr.data is {}".format(curr, curr.data))
			print("set prev {} to curr {}".format(prev, curr))
			print("also set curr {} to curr.next {}".format(curr, curr.next_node))
			prev = curr
			curr = curr.next_node
			print()
		sleep(1)
		# time to unlink from the list
		if prev is None:
			print("Prev is None setting head {} to curr.next {}".format(self.head, curr.next_node))
			print()
			sleep(1)
			# if previous node was none meaning we at the head, 
			# then set the head to the next node
			self.head = curr.next_node    
		elif curr:
			print("set prev.next {} to curr.next {}".format(prev.next_node, curr.next_node))
			print("also set curr.next {} to None".format(curr.next_node))
			print()
			sleep(1)
			# set the curr node to next one and the next one to none
			prev.next_node = curr.next_node
			curr.next_node = None

	def find(self, key):
		# search for the first element with data matching key
		# return the element or None if not found takes O(n) time
		curr = self.head
		while curr and curr.data != key:
			curr = curr.next_node
		return curr		# if nothing is found None will be returned
	
	def reverse(self):
		# reverse list in place, takes O(n) time
		curr = self.head
		prev = None
		next_node = None
		while curr:
			next_node = curr.next_node
			curr.next_node = prev
			prev = curr
			curr = next_node
		self.head = prev


# remove target from linked list
class Solution:
	def deleteDuplicates(self, head: ListNode) -> ListNode:
		while head and head.next==head.val:
			head = head.next
		curr = head
		while curr:
			if curr.next and curr.next.val==curr.val:
				curr.next = curr.next.next
			else:
				curr = curr.next
		return head


"""
Reverse Operations
You are given a singly-linked list that contains N integers. 
A subpart of the list is a contiguous set of even elements,
bordered either by either end of the list or an odd element. 
For example, if the list is [1, 2, 8, 9, 12, 16], the subparts of the list are [2, 8] and [12, 16].
Then, for each subpart, the order of the elements is reversed. 
In the example, this would result in the new list, [1, 8, 2, 9, 16, 12].
The goal of this question is: given a resulting list, determine the original order of the elements.
"""
def reverse(head):
  # Write your code here
	node = head
	output = []

	while node:
		is_even = node.data % 2 == 0
		if is_even:  # even, start pushing
			output.append(node) # entire node !!!!!!!!!!!!!!!!!!!!!!

		if not is_even or node.next is None:  # not even, start popping
			left, right = 0, len(output)-1 # pointers are more optimal than pop()
			while len(output) > 1 and left < right:
				output[left].data, output[right].data = output[right].data, output[left].data # I am swapping only node.data, node.next is still the same
				left +=1
				right -= 1
				#output.pop(0) --> Will take O(N) to remove 1st element, because you need to shift everything to the left  
				#output.pop(-1) --> will take O(1) to remove last element 
			output.clear() # or "output = []" # O(N)
		node = node.next

	return head


# remove nth node from end of list
class Solution:
	def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
		fast = head
		slow = head
		# advance fast to nth position
		for i in range(n):
			fast = fast.next
			
		if not fast:
			return head.next
		# then advance both fast and slow now they are nth postions apart
		# when fast gets to None, slow will be just before the item to be deleted
		while fast.next:
			slow = slow.next
			fast = fast.next
		# delete the node
		slow.next = slow.next.next
		return head












ls = LinkedList()
print(ls)
ls.prepend(23)
ls.prepend('a')
ls.prepend('a')
ls.prepend('a')
ls.append(24)
ls.append(24)
ls.prepend(42)
ls.append("name")
ls.append(24)
ls.append(24)
print(ls)
ls.remove('name')
print("\n{}".format(ls))


'''
Class sessh

Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

[1,2,4,5,None]
[5,4,2,1]

curr = 1
prv = None
next = None

while not None


1->2->3->Null

1. https://www.youtube.com/watch?v=O0By4Zq0OFc
2. https://leetcode.com/problems/reverse-linked-list



'''

class ListNode:
	def __init__(self, val, next=None):
		self.val = val
		self.next = next

	# 1->2->3->None
	# rest = 2->3->None
	#   New List I'm Reversing ----> None<-1
	
			
# code to reverse linked list
class Solution:
	def reverseList(self, head: ListNode) -> ListNode:
		next_node = None
		prev_node = None
		cur_node = head
		  
		while cur_node is not None: 
			# save the next node in a temp variable
			next_node = cur_node.next 
			
			# since we saved the next node, we can make the connection 
			cur_node.next = prev_node
			
			# save for next iteration
			prev_node = cur_node 
			
			# Assign to the current node from temp variable
			cur_node = next_node 
		
		# At this point, the cur_node will be None, hence return the prev_node
		return prev_node

'''
Platform: leetcode.com
938. Range Sum of BST
Link: https://leetcode.com/problems/range-sum-of-bst/
Difficulty: Easy
Author: hritik5102
Date: 17/1/2021
Submission: https://leetcode.com/submissions/detail/444136335/
(Time, Space) Complexity : O(n), O(H)

Range sum of BST 

1.  We can solve this problem using recursion and iteration 

iteration                                  Recursion 
1. implemented using loops                  1. implemented using function calls 
2. Defined by the control variable          2. Defined by the parameter value in the stack
value  
3. iteration makes size of Code            3. Recursion decreses the size of code
bigger                                      
4. Loop ends when control variable          4. Recursion ends when base case are True
satisfy the condition 
5. Infinite loops uses CPU Cycle            5. Infinite Recursion cause stack overflow at particular point or might crash the system
6. Execution is faster                      6. Execution is slower
Method 01
Inorder traversal ( Left child , Node , Right child)
Disadvantage of using Inorder traversal method

Using this approach we are visiting at each node of the binary tree and we are not utilizing the benefit of binary tree.

Time: O(n), space: O(h), where n is the number of total nodes, h is the height of the tree.
'''
class Solution:    
	def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
		output = []
		if root==None:
			return 0
		self.inOrderTraversal(root,low,high,output)
		return sum(output) 
	
	def inOrderTraversal(self, root,low,high,output):
		if root == None:
			return
		
		# Left 
		self.inOrderTraversal(root.left, low,high,output)
		
		# Node 
		if low <= root.val <= high:
			output.append(root.val)
			
		# Right
		self.inOrderTraversal(root.right, low,high,output)

'''So what we do when we search a particular number in a binary tree

first we check if a number is less then a root, if yes then we search in left subtree else if it's greater then we search in right subtree of root node

same here, we see

1. if low < root :
		 inOrderTraversal( root.left, low, high)

2. if High > root :
		 inOrderTraversal( root.right, low, high)     
Method 02
'''
class Solution:    
	def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
		output = []
		if root==None:
			return 0
		self.inOrderTraversal(root,low,high,output)
		return sum(output) 
	
	def inOrderTraversal(self, root,low,high,output):
		if root == None:
			return
			
		# left 
		if low<root.val:
			self.inOrderTraversal(root.left, low,high,output)
		
		# Node
		if low <= root.val <= high:
			output.append(root.val)
		
		# RIght 
		if high>root.val:
			self.inOrderTraversal(root.right, low,high,output)

# Method 03
# Same Logic but reduction in line of code
class Solution:    
	def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
		total = 0
		if root==None:
			return 0
		if low <= root.val <= high:
			total +=root.val
		if low<root.val:
			total += self.rangeSumBST(root.left, low,high)
		if high>root.val:
			total += self.rangeSumBST(root.right, low,high)
		
		return total 

# detect and remove cycle from linked list
# Python program to detect and remove loop in linked list

# Node class 
class Node:

	# Constructor to initialize the node object
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:

	# Function to initialize head
	def __init__(self):
		self.head = None

	def detectAndRemoveLoop(self):
		slow_p = fast_p = self.head
		
		while(slow_p and fast_p and fast_p.next):
			slow_p = slow_p.next
			fast_p = fast_p.next.next

			# If slow_p and fast_p meet at some point then
			# there is a loop
			if slow_p == fast_p:
				self.removeLoop(slow_p)
		
				# Return 1 to indicate that loop is found
				return 1
		
		# Return 0 to indicate that there is no loop
		return 0

	# Function to remove loop
	# loop_node --> pointer to one of the loop nodes
	# head --> Pointer to the start node of the linked list
	def removeLoop(self, loop_node):
		ptr1 = loop_node
		ptr2 = loop_node
		
		# Count the number of nodes in loop
		k = 1
		while(ptr1.next != ptr2):
			ptr1 = ptr1.next
			k += 1

		# Fix one pointer to head
		ptr1 = self.head
		
		# And the other pointer to k nodes after head
		ptr2 = self.head
		for i in range(k):
			ptr2 = ptr2.next

		# Move both pointers at the same place
		# they will meet at loop starting node
		while(ptr2 != ptr1):
			ptr1 = ptr1.next
			ptr2 = ptr2.next

		# Get pointer to the last node
		while(ptr2.next != ptr1):
			ptr2 = ptr2.next

		# Set the next node of the loop ending node
		# to fix the loop
		ptr2.next = None

	# Function to insert a new node at the beginning
	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	# Utility function to print the linked LinkedList
	def printList(self):
		temp = self.head
		while(temp):
			print temp.data,
			temp = temp.next


# Driver program
llist = LinkedList()
llist.push(10)
llist.push(4)
llist.push(15)
llist.push(20)
llist.push(50)

# Create a loop for testing
llist.head.next.next.next.next.next = llist.head.next.next

llist.detectAndRemoveLoop()

print "Linked List after removing loop"
llist.printList()

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)
