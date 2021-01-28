# O(n^2) time complexity

def bubble_sort(a_list):
	for pass_num in range(len(a_list) - 1, 0, -1):
		for i in range(pass_num):
			if a_list[i] > a_list[i + 1]:
				temp = a_list[i]
				a_list[i] = a_list[i + 1]
				a_list[i + 1] = temp

def bubble_sort2(a_list):
	for pass_num in range(len(a_list)-1):
		for i in range(len(a_list)-1):
			if a_list[i] > a_list[i + 1]:
				a_list[i], a_list[i+1] = a_list[i+1], a_list[i]


a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print("Unsorted list {}".format(a_list))
bubble_sort2(a_list)
print("Bubble sorted list {}".format(a_list))
