# O(n^2) Time complexity but more efficient than bubble sort
# This process continues and requires 𝑛 − 1 passes to sort 𝑛 items, since the final item
# must be in place after the (𝑛 − 1)st pass.

def selection_sort(a_list):
	for fill_slot in range(len(a_list) - 1, 0, -1):
		pos_of_max = 0
		for location in range(1, fill_slot + 1):
			if a_list[location] > a_list[pos_of_max]:
				pos_of_max = location
		temp = a_list[fill_slot]
		a_list[fill_slot] = a_list[pos_of_max]
		a_list[pos_of_max] = temp

def selection_sort2(a_list):
	for fill_slot in range(len(a_list) - 1, 0, -1):
		pos_of_max = 0
		for location in range(1, fill_slot + 1):
			if a_list[location] > a_list[pos_of_max]:
				pos_of_max = location
		a_list[fill_slot], a_list[pos_of_max] = a_list[pos_of_max], a_list[fill_slot] # Exchange without a temp variable

a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print("Usorted list {}".format(a_list))
selection_sort2(a_list)
print("Bubble sorted list {}".format(a_list))