
def power(x, n):
	if n==0:
		return 1
	else:
		return x*power(x, n-1)


vowel = "aeiou"
# time complexity will be o(n) for n calls (recursive stack)
def recursive_count_consonants(input_str):
	# base case if empty string
	if input_str == "":
		return 0

	if input_str[0].lower() not in vowel and input_str[0].isalpha():
		return 1 + recursive_count_consonants(input_str[1:])
	else:
		return recursive_count_consonants(input_str[1:])

# input_str = input("ENter string: ")
# print(recursive_count_consonants(input_str))

memo = {}
def fib(n):
	if n in [0,1]:
		return n
	if n in memo:
		return memo[n]
	res = fib(n-1) + fib(n-2)
	memo[n] = res
	return res


print(fib(998))

class Fibber(object):

	def __init__(self):
		self.memo = {}

	def fib(self, n):
		if n < 0:
			# Edge case: negative index
			raise ValueError('Index was negative. No such thing as a '
							 'negative index in a series.')
		elif n in [0, 1]:
			# Base case: 0 or 1
			return n

		# See if we've already calculated this
		if n in self.memo:
			return self.memo[n]

		result = self.fib(n - 1) + self.fib(n - 2)

		# Memoize
		self.memo[n] = result

		return result

# iterative approach O(1) space and O(n) time
def fib(n):
	if n in [0,1]:
		return n
	prev_prev = 0
	prev = 1
	for i in range(n-1):
		curr = prev + prev_prev
		prev_prev = prev
		prev = curr
	return curr

