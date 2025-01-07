
s=input()
o=0
k=0
for i in range(len(s)):
    if s[i].islower():
        k+=1
    else:
        o+=1
if o>k:
    print(s.upper())
else:
    print(s.lower())