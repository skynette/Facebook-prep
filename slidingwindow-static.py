
"""
Find max sub array sum
"""

# sliding window jutsu
def lenofsubstring(string):
	n = len(string)
	s = set()
	ans = 0
	i=0
	j = 1
	while i<n and j<n:
		window_sum = string[i] + string[j]
		s.add(window_sum)
		i+=1
		j+=1		
	return max(s)


string = list(map(int, input().split()))
# print(lenofsubstring(string))

"""
given an array of postive integers, Find the sub arrays that add up to a given number k
[1,7,4,3,1,2,1,5,1], k=7
find how many sub arrays have sum equal to 7
"""

