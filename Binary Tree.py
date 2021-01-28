from collections import deque

class Node:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

class BinaryTree:
	def __init__(self, root):
		self.root = Node(root)

	# tree traversal
	# preorder traversal
	def preorder(self, start, trav=""):
		"root -> left -> right"
		if start:
			trav += (str(start.val)+" -> ") 
			trav = self.preorder(start.left, trav)
			trav = self.preorder(start.right, trav)
		return trav
	# inorder traversal
	def inorder(self, start, trav=""):
		"left -> root -> right"
		if start:
			trav = self.inorder(start.left, trav)
			trav += (str(start.val)+' -> ')
			trav = self.inorder(start.right, trav)
		return trav
	# postorder traversal
	def postorder(self, start, trav=""):
		"left -> right -> root"
		if start:
			trav = self.postorder(start.left, trav)
			trav = self.postorder(start.right, trav)
			trav += (str(start.val)+' -> ')
		return trav

	# BFS
	def levelorder(self, start, trav=""):
		q = deque()
		q.append(self.root)
		while len(q) > 0:
			print(q[0].val, end=" -> ")
			node = q.popleft()
			if node.left:
				q.append(node.left)
			if node.right:
				q.append(node.right)
		return trav

	# height of binary tree
	def height(self, node):
		if node is None:
			return -1
		left_height = self.height(node.left)
		right_height = self.height(node.right)
		return 1 + max(left_height, right_height)

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.right.right.right = Node(8)
# print('height:',tree.height(tree.root))

# tree traversal: preorder, inorder, postorder
# print(tree.preorder(tree.root))
# print(tree.inorder(tree.root))
# print(tree.postorder(tree.root))
# print(tree.levelorder(tree.root))


# binary search trees 
# a tree in which the left child is always smaller 
# and the right child is always greater than the node
class Node:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

class BST:
	def __init__(self, root):
		self.root = Node(root)

	def add(self, current, val):
		if not self.root:
			self.root = Node(val)
		else:
			if val < current.val:
				if current.left == None:
					current.left = Node(val)
				else:
					self.add(current.left, val)
			else:
				if current.right == None:
					current.right = Node(val)
				else:
					self.add(current.right, val)
	# Wrong
	def check_bst_property(self, curr_node):
		if not self.root:
			return True
		else:
			if curr_node.left:
				if curr_node.val > curr_node.left.val:
					return self.check_bst_property(curr_node.left)
				else:
					return False
			elif curr_node.right:
				if curr_node.val < curr_node.right.val:
					return self.check_bst_property(curr_node.right)
				else:
					return False
		return True


	def preorder(self, current):
		if current:
			print(current.val, end=" -> ")
			self.preorder(current.left)
			self.preorder(current.right)

	def inorder(self, current):
		if current:
			self.preorder(current.left)
			print(current.val, end=" -> ")
			self.preorder(current.right)
	
	def postorder(self, current):
		if current:
			self.preorder(current.left)
			self.preorder(current.right)
			print(current.val, end=" -> ")

tree = BST(3)
# tree.add(tree.root, 2)
# tree.add(tree.root, 5)
# tree.add(tree.root, 1)
# tree.add(tree.root, 4)
tree.root.left = Node(2)
tree.root.left.left = Node(1)
tree.root.left.right = Node(4)
tree.root.right = Node(5)

# tree.preorder(tree.root)
# print()
tree.inorder(tree.root)
print()
# tree.postorder(tree.root)
# print()
print(tree.check_bst_property(tree.root))










# program to check if a binary tree is bst or not
""" Program to check if a given Binary 
Tree is balanced like a Red-Black Tree """
# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

# DFS approach
# Time complexity O(n)
# space complexity O(n)
class Solution:
	def isValidBST(self, root: TreeNode) -> bool:	

		def helper(root, min_val, max_val):
			if not root:
				return True
			if root.val <= min_val or root.val>= max_val:
				return False

			validLeft = helper(root.left, min_val, root.val)
			validRight = helper(root.right, root.val, max_val)

			return validLeft and validRight

		return helper(root, float('-inf'), float('inf'))

# alternative solution
# Iterative BFS solution
# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right
		
from collections import deque
class Solution:
	def isValidBST(self, root: TreeNode) -> bool:
		dq = deque()
		dq.append([root, -float("inf"), float("inf")])
		while dq:
			root, lower, upper = dq.popleft()
			left_child = root.left
			right_child = root.right
			if left_child:
				if root.val > left_child.val > lower:
					dq.append([left_child, lower, root.val])
				else:
					return False

			if right_child:
				if root.val < right_child.val < upper:
					dq.append([right_child, root.val, upper])
				else:
					return False
		return True


# BFS to get max depth of binary tree
def maxDepth(root):
	q = deque()
	q.append(self.root)
	depth = 0
	while len(q) > 0:
		depth+=1
		tmp = []
		for node in q:
			if node.left:
				tmp.append(node.left)
			if node.right:
				tmp.append(node.right)
		q = tmp
	return depth

# DFS to get max depth
def maxDepth(root):
	if not root:
		return 0
	else:
		return 1 + maxDepth(root.left, root.right)




# Minimum depth of Binary tree
# using bfs

from collections import deque
class Solution:
	def minDepth(self, root: TreeNode) -> int:
		if not root:
			return 0
		q = deque()
		q.append(root)
		min_depth = deque()
		min_depth.append(1)
		
		while q:
			node = q.popleft()
			depth = min_depth.popleft()
			
			if not node.left and not node.right:
				return depth
			if node.left:
				q.append(node.left)
				min_depth.append(depth+1)
			if node.right:
				q.append(node.right)
				min_depth.append(depth+1)

