import math
s = ('number', float('nan'), 'attributes', 'parameters')
print(s)


print(type(s[1]), isinstance(s[1], str))
print(type(s[2]), isinstance(s[2], str))

s1 = tuple([x if isinstance(x, str) else '' for x in s])
print(s1)
if s1[1]:
    print(s1)
