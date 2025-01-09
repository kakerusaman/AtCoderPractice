K = int(input())
S= input()
T = input()

#文字列の長さを見て変更できるかどうか考える。
#Kは必ず1のため、TよりもSが1大きいか小さいかでまずは判定する。
def len_check():
    if len(S) == len(T):
        pass
    elif len(T) == len(S)-1:
        pass
    elif len(T) == len(S)+1:
        
        for i in range(len(T)):
            if len(T)-1 == i:
                break 
            if S[i] == T[i]:
                pass
            elif S[i]!= T[i]:
                

    else:
        print("No")
    
