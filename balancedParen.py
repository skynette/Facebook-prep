from stack import Stack

def is_Match(p1, p2):
	if p1 == "(" and p2 == ")":
		return True
	elif p1 == "[" and p2 == "]":
		return True
	elif p1 == "{" and p2 == "}":
		return True
	else:
		return False
def is_BalancedParen(string):
	s = Stack()
	is_Balanced = True
	index = 0
	while index <len(string) and is_Balanced:
		paren = string[index]
		if paren in "({[":
			s.push(paren)
		else:
			if s.is_empty():
				is_Balanced = False
			else:
				top = s.pop()
				if not is_Match(top, paren):
					is_Balanced = False
		index += 1
	if s.is_empty():
		return True
	else:
		return False

		
# Another solution could be
def is_matched(expression):
	lefty = '([{'
	righty = ')]}'
	s = Stack()
	for i in expression:
		if i in lefty:
			s.push(i)
		elif i in righty:
			if s.is_empty():
				return False
			if righty.index(i) != lefty.index(s.pop()):
				return False
	return s.is_empty()

i = "()()(()(){}{}{}{[]][]})"
print(is_BalancedParen(i))
print(is_matched(i))