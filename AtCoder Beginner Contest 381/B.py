import collections


S = list(input())



result = False

def even_number():
    global result
    if len(S) % 2 == 0:
        string_check()
    else:
        result = False

def string_check():
    global result 
    flag = False
    for i in range(len(S)//2):
        if S[2*i]==S[2*i+1]:
            flag =True
        else:
            result = False
    if flag == True:

        pop_derees()
def pop_derees():
    global result
    tmp = collections.Counter(S)
    for value in tmp.values():
        if value == 2:
            result = True
        else:
            break


even_number()


if result == False:
    print("No")
else:
    print("Yes")


"""
#回答例上記のやつではエラー出る。
s=input()
flag=True
if len(s)%2==1:
    flag=False
if flag:
    for i in range(len(s)//2):
        if s[2*i]!=s[2*i+1]:
            flag=False
cnt=[0 for i in range(26)]
if flag:
    for i in range(len(s)):
        cnt[ord(s[i])-ord('a')]+=1
    for i in range(26):
        if cnt[i]!=0 and cnt[i]!=2:
            flag=False
if flag:
    print("Yes")
else:
    print("No")
        """