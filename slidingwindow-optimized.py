from colorama import init, Fore
init(autoreset=True)

# sliding window jutsu
def lenofsubstring(string):
	n = len(string)
	hashMap = {}
	ans = 0
	i=0
	j = 0
	while j<n:
		# window = string[i:j]
		if hashMap.get(string[j]):
			b = hashMap.get(string[j])+1
			ans = max(b, i)
		else:
			hashMap[string[j]] = j
		ans = max(ans, j-i+1)
		hashMap[string[i]] = j
		j+=1
	return ans


string = input()
print(lenofsubstring(string))


# if hashMap.get(string[j]):
# 	i = max(hashMap.get(string[j]), i)
# ans = max(ans, j-i+1)
# hashMap[string[i]] = j
# j+=1