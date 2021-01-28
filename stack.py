
"""
implementing The Stack data structure
all operations run at O(n) time complexity
"""

class Stack():
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    def is_empty(self):
        return self.items == []
    def get_stack(self):
        return self.items
    def __len__(self):
        return len(self.items)


'''


Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.


Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]


1. initialize with an empty array O(1)
2. push: add items to stack by calling append() O(1)
3. pop: pop items by calling pop() O(1)
4. top: calling array[-1] O(1)
5. getMin: min(array) O(n)

have a variable thatkeep track of items pushed into the stack
4,0,-4,6,1,0,-2
[
-2
0
1
6
-4
0
4
]
[4,0,-4]
v=1

PUSH(0)
PUSH(4)
PUSH(0)
get_min()
pop()
get_min()

[(0,0),(4,0),(0,0)]

[
4
0
]
[0]
https://leetcode.com/problems/min-stack/

'''
class Stack():
    def __init__(self):
        self.array = []
        self.aux_array = []
        
    def push(self, item):
        self.array.append(item)
        if self.aux_array == []:
            self.aux_array.append(item)
        elif item <= self.aux_array[-1]:
            self.aux_array.append(item)
        return
        
    def pop(self):
        item = self.array.pop()
        if item == self.aux_array[-1]:
            self.aux_array.pop()
            
    def top(self):
        return self.array[-1]
    
    def getMin(self, aux_array):
        return self.aux_array[-1]

# def is_match(p1, p2):
    if p1 == "{" and p2 == "}":
      return True
    elif p1 == "(" and p2 == ")":
      return True
    elif p1 == "[" and p2 == "]":
      return True
    else:
      return False

"""
Balance Brackets
A bracket is considered to be any one of the following characters: (, ), {, }, [, or ].
We consider two brackets to be matching if the first element is an open-bracket, 
e.g., (, {, or [, and the second bracket is a close-bracket of the same type, e.g., ( and ), [ and ], and 
{ and }
are the only pairs of matching brackets.
Furthermore, a sequence of brackets is said to be balanced if the following conditions are met:
The sequence is empty, or
The sequence is composed of two, non-empty, sequences both of which are balanced, or
The first and last brackets of the sequence are matching, and the portion of the
sequence without the first and last elements is balanced.
You are given a string of brackets. Your task is to determine whether each sequence 
of brackets is balanced. 
If a string is balanced, return true, otherwise, return false
"""

def isBalanced(s):
  # Write your code here
  stack = []
  left_paren = "{(["
  right_paren = "})]"
  index = 0
  is_balanced = True
  while index < len(s) and is_balanced:
    paren = s[index]
    if paren in left_paren:
      stack.append(paren)
    else:
      if len(stack) == 0:
        is_balanced = False
      else:
        top = stack.pop()
        if not is_match(top, paren):
          is_balanced = False
    index +=1
  if stack == [] and is_balanced:
    return True
  else:
    return False