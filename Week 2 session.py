def say_hello():
    print('Hello, World')

for i in range(5):
    say_hello()

'''
formular
=SUMIFS(Expenses!$D$1:$D, Expenses!$B$1:$B, ">="&$A2, Expenses!$B$1:$B, "<" & (EOMONTH($A2,0)+1), Expenses!$E$1:$E, "="&B$1)
=SUMIFS(Income!$D$1:$D, Income!$B$1:$B, ">="&$A2, Income!$B$1:$B, "<" & (EOMONTH($A2,0)+1), Income!$C$1:$C, "="&B$1)


Linked Lists
* Uses pointers
* Can be used like Array (in a way)


Example
hash (key) % array_length

We have a list like -> l = [1,2,3,4,5] 
We want it to look like -> [1,2,3,6,4,5]

5 -> 9 -> 7 -> 8


Hash tables
* map from keys to values 
* retrieve values given the key
* we need to have an array powering a hash table


Slots    Contents
0        [("name","tayo")]
1        []
2        [("school,"MIT"),("fav food","rice)]

15      []
.
.
.
N        []


ht = HashTable()
ht["name"]  = "tayo" hash("name") 0
ht["school"] = "MIT" hashes to 2
ht["fav food"] = "rice" hashes to 2


'''



'''


Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "lovele"
return 2.

Algorithm

dict = {'l':2,'o':'v':1, 'e':1}

dict[c]>1
dict['l':1, 'e':1]


* Create a frequency table for characters in the string
* Loop through the string
    * for each ch, check if its occurrence in freq table > 1:
            return index
    * return -1

'''

from collections import defaultdict

def find_first_unique_char_2(string):
    ht = defaultdict()
    
    for ch in string:
        ht[ch]+=1
    
    for i,ch in enumerate(string):
        if ht[ch] > 1:
            return i
    return -1
                          
    
    

def find_first_unique_char(string):
    ht = {}
    ans = -1
    for ch in string:
        if ht.get(ch):
            if ht[ch] == 1:
                ans = string.index(ch)
                return ans
        else:
            ht[ch] = 1
    return ans


'''
Given two strings, write a method to check if one is a permutation of the other

dog, god -> True

cat atc -> True

# create a set of both and compare
ht = letters and freq {}
w1  = {'d':1 'o':1, 'g':1}


dog vs dogf

w1[lett] w2[lett]
'''