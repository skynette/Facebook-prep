'''
* Two linked lists
* Sorted
* Merge these 2 linked lists into a sorted single linked list

1->2

3

0->1

0->1->2->3->4->4
Result -> 1->2->4->4->4->7

[1,2,4,4,3,7] -> sort -> transform back to ll

'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def merge_sorted_llist(self, head1, head2):
        head1 = head1
        head2 = head2
        sorted_list = ListNode(0)
        head = sorted_list
        while head1 and head2:
            if head1.val < head2.val:
                sorted_list.next = head1
                head1 = head1.next
            else:
                sorted_list.next = head2
                head2 = head2.next
            sorted_list = sorted_list.next
        
        if head1 is None:
            sorted_list.next = head2
        else:
            sorted_list.next = head1
        return head.next
    
    
    
'''
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

https://assets.leetcode.com/uploads/2020/12/01/tree2.jpg

https://assets.leetcode.com/uploads/2020/12/01/tree1.jpg


A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.


root

left < root
left
right > root

[1,2,1,17]

left -> node -> right
     5
     /\
    1  7
       /\
      1  17
      
      5
     / \
     6  SUPER LARGE
     
'''
# time complexity O(n) n is size of tree
# space complexity O(n) because of our aux array
class Node:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value

    def check(self):
        arr = []
        def check_valid_BST(self, node):
            'left-node-right'
            if node:
                check_valid_BST(node.left)
                arr.append(node)
                check_valid_BST(node.right)

        for i in range(len(arr)-1):
            if not arr[i] < arr[i+1]:
                return False
        return True
    
