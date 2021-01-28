from colorama import init, Fore
init(autoreset=True)

# sliding window jutsu
def lenofsubstring(string):
	n = len(string)
	s = set()
	ans = 0
	i=0
	j = 0
	while i<n and j<n:
		print(Fore.GREEN+"Checking", string[j])
		window = string[i:j]
		print("current window:", window)
		if not string[j] in s:
			print(string[j], "not in set so adding")
			s.add(string[j])
			ans = max(ans, j-i+1)
			print("curr ans is", ans, "increasing window limit j to", j+1)
			j+=1
		else:
			print(string[j],"found in set so removing...")
			s.remove(string[i])
			print('increasing window limit i to ',i+1)
			i+=1


	return ans


string = input()
print(lenofsubstring(string))

# Max consecitive ones III leetcode question
# Approach:
# Sliding window with expansion of right pointer when A[right] is 1.
# If A[right] is 0 then we need to keep track of our remainingK to see if we can still push it forward.
# If remainingK is 0 then we need to shift left pointer forward until we can have remainingK to satisfy the right pointer's 0 to make the window valid again.
# Check to see if there is a maxWindow update when we hit the end of A or if window becomes invalid (i.e. A[right] = 0 but remainingK < 0).

class Solution:
    #592ms ~ O(n) runtime. Either the left or the right pointer are always moving, so at most we do 2*n operations.
    #O(1) extra space
    def longestOnes(self, A: List[int], K: int) -> int:
        
        lenA = len(A)
        if lenA == 0:
            return 0
        
        left = 0
        right = 0
        remainingK = K
        windowOnes = 0
        maxWindow = 0 #will contain the max window thusfar

        while True:
            #while 1, expand right
            while A[right] == 1:
                right += 1
                windowOnes += 1
                if right == lenA:
                    #at the righend of A, check if there's an update to max
                    if windowOnes > maxWindow:
                        maxWindow = windowOnes
                    return maxWindow
                
            #if 0 then grab it and reduce remainigK
            while A[right] == 0:
                #if remainingK is 0 then we have to keep shifting left forward until remainingK is no longer 0
                if remainingK == 0:
                    #calculate our current window to see if it's a max before adjusting
                    if windowOnes > maxWindow:
                        maxWindow = windowOnes
                    #now keep shifting the left pointer forward until there is remainingK again
                    while remainingK == 0:
                        if A[left] == 0:
                            remainingK += 1
                        left += 1
                        windowOnes -= 1
                
                #reduce remainingK so we can shift right forward
                remainingK -= 1
                windowOnes += 1
                right += 1

                if right == lenA:
					#at the righend of A, check if there's an update to max
                    if windowOnes > maxWindow:
                        maxWindow = windowOnes
                    return maxWindow


# max sum subarray problem
# given an array find the contigous sum of size k
# using sliding window to get best time and space complexity

def max_sum_subarray(arr, k):
    max_sum = float('-inf')
    start = 0
    curr_sum = 0

    for end, val in enumerate(arr):
        curr_sum += val
        # if we get to size k
        if end - start + 1 == k:
            # compare and set max sum
            max_sum = max(max_sum, curr_sum)
            # reset start position and remove start value
            # from current sum
            curr_sum -= arr[start]
            start += 1

    return max_sum


# given array of positive numbers
# find the size of smallest contigous subarray whose sum >= s

def smallest_subarray(arr, s):
    min_size = float('inf')
    curr_sum = 0
    start = 0
    
    for end, val in enumerate(arr):
        # we want to increase our current sum
        curr_sum += val
        # while the curr sum is >= s we wanna decrease the window and see if we can get any smaller
        while curr_sum >= s:
            # here the min_size is updated to the size of curr window
            min_size = min(min_size, end - start + 1)
            # remove the first item from the window and shrink
            curr_sum -= arr[start]
            # shrink the window and check again
            start += 1
    return min_size

