# binary search recursive
def binarySearch(data, target, low, high):
# """
# def binary search(data, target, low, high):
# Return True if target is found in indicated portion of a Python list.  
# The search only considers the portion from data[low] to data[high] inclusive.
# """
	if low>high:
		return False
	else:
		middle = (low+high)//2
		if target == data[middle]:
			return True
		elif target<data[middle]:
			# recur on the portion left of the middle
			return binarySearch(data, target, low, middle-1)
		else:
		# recur on the portion right of the middle
			return binarySearch(data, target, middle+1, high)

data = [3, 5, 6, 8, 11, 12, 14, 15, 17, 18]
print(binarySearch(data, 8, 0, len(data)-1))	


"""
Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.
 

Example 1:

Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.
We will write a helper function that accepts a list, finds the index of the first negative element and subtracts it from the length of the list. This way, we arrive to the number of negative elements.
Consider:
[4, 3, 2, -1]
Index of the first negative element is 3. 4 minus 3 is 1. We have one negative element in the list
[-1, -1, -2, -3]
Index of the first negative element is 0. 4 minus 0 is 4. We have four negative elements in the list

Then we will traverse the matrix, passing every row into the helper function and updating res.
One edge case is a list with all non-negative elements
[6, 4, 2, 1]
In this case, our helper function will return 1 (4 minus 3, where 4 is the length of the list and 3 is the index of r once we complete the binary search). We take care of this situation by writing return len(nums) - r if nums[-1] < 0 else 0 because if the most-right element is non-negative, it means all elements to the left are non-negative as well."""

def countNegatives_bin_search(grid): 
    res = 0
    def _helper(nums):  
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] >= 0:
                l = m + 1
            else:
                r = m
        return len(nums) - r if nums[-1] < 0 else 0
    for row in grid:
        res += _helper(row)
    return res

# find point of rotation in an array
# Linear search first
# Python3 program to find number 
# of rotations in a sorted and 
# rotated array. 
  
# Returns count of rotations for 
# an array which is first sorted 
# in ascending order, then rotated 
# time complexity O(n), space O(1)
def countRotations(arr, n): 
  
    # We basically find index 
    # of minimum element 
    min = arr[0] 
    for i in range(0, n): 
      
        if (min > arr[i]): 
          
            min = arr[i] 
            min_index = i 
          
    return min_index; 
  
  
# Driver code 
arr = [15, 18, 2, 3, 6, 12] 
n = len(arr) 
print(countRotations(arr, n)) 
  
# This code is contributed by Smitha Dinesh Semwal 


# binary search method
"""Method 2 (Efficient Using Binary Search)
Here also we find the index of minimum element, but using Binary Search. The idea is based on the below facts :

The minimum element is the only element whose previous is greater than it. If there is no previous element, then there is no rotation (first element is minimum). We check this condition for middle element by comparing it with (mid-1)’th and (mid+1)’th elements.
If the minimum element is not at the middle (neither mid nor mid + 1), then minimum element lies in either left half or right half.
If middle element is smaller than last element, then the minimum element lies in left half
Else minimum element lies in right half."""


def countRotations(arr,low, high): 
  
    # This condition is needed to  
    # handle the case when array 
    # is not rotated at all 
    if (high < low): 
        return 0
  
    # If there is only one  
    # element left 
    if (high == low): 
        return low 
  
    # Find mid 
    # (low + high)/2  
    mid = low + (high - low)/2;  
    mid = int(mid) 
  
    # Check if element (mid+1) is 
    # minimum element. Consider  
    # the cases like {3, 4, 5, 1, 2} 
    if (mid < high and arr[mid+1] < arr[mid]): 
        return (mid+1) 
  
    # Check if mid itself is  
    # minimum element 
    if (mid > low and arr[mid] < arr[mid - 1]): 
        return mid 
  
    # Decide whether we need to go 
    # to left half or right half 
    if (arr[high] > arr[mid]): 
        return countRotations(arr, low, mid-1); 
  
    return countRotations(arr, mid+1, high) 
  
# Driver code 
arr = [15, 18, 2, 3, 6, 12] 
n = len(arr) 
print(countRotations(arr, 0, n-1))     
  
# This code is contributed by Smitha Dinesh Semwal 