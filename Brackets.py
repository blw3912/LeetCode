'''
Given a string s containing just the characters
'(', ')', '{', '}', '[' and ']', determine if the input string is valid.
'''
s= '({})[]'

#preliminary testing
if s.count('(') == s.count(')') and s.count('[') == s.count(']') and s.count('{') == s.count('}'):
    print('Pairs ok')

lst = list(s)
for i in range(len(lst)):
    if lst[i] == '(' and lst[i+1] == ')':
        lst.pop(i)
        lst.pop(i+1)
for _ in range(len(lst)):
    if lst[i] == '[' and lst[i+1] == ']':
        lst.pop(i)
        lst.pop(i+1)
for _ in range(len(lst))
    if lst[i] == '{' and lst[i+1] == '}':
        lst.pop(i)
        lst.pop(i+1)

print(lst)
