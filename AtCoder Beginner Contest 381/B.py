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
    for i in range(len(S)/2):
        if S[2*i -1] == S[2*i]:
            result = True
        else:
            result = False
    
def pop_derees():
    print("horyuu")




if result == False:
    print("No")
else:
    print("Yes")





        