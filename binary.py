def findIndex(array, target, left, right):
	if left>right:
		return -1
	else:
		middle = (left+right)//2
		if target == array[middle]:
			return middle
		elif target<array[middle]:
			return findIndex(array, target, left, middle-1)
		else:
			return findIndex(array, target, middle+1, right)

array = [1,2,3,4,5,6,7,8,8,9]
print(findIndex(array, 5, 0, len(array)-1))	
print(findIndex(array, 9, 0, len(array)-1))	
