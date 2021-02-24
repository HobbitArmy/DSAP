"""
第四章 递归

"""

# %% R-4.1 Find max element in series S
def findMaxElement(S,n,idx=0):
    """ Find max element in series
        Time-complexity:O(n)"""
    if n<=1: return S[idx]
    elif S[n-1]>=S[idx]:
        return findMaxElement(S,n-1,n-1)
    else: return findMaxElement(S,n-1,idx)
# %% R-4.6 Calculate n-th harmonic number
def harmonicNumber(n):
    """ Return n-th harmonic number, which H(n)=sum(1/i) for i in range[1,n]"""
    if n<=1: return 1
    else: return harmonicNumber(n-1)+1/n
# %% R-4.7 Change str to int-number
def changeStr2Int(s,n:'len(s)'):
    """ Return the int-number converted from s"""
    if n<=1: return ord(s[n-1])-ord('0')
    else: return (ord(s[n-1])-ord('0'))+10*changeStr2Int(s,n-1)
def invertStr2Int(s,n=1):
    """ Return the int-number converted from inverted(s)"""
    if n>=len(s): return ord(s[n-1])-ord('0')
    else: return (ord(s[n-1])-ord('0'))+10*changeStr2Int(s,n+1)
# %% C-4.8 Find min&max in series
def findMinMaxElement(S,n:"len(s)",mm:"[S[0],S[0]]"):
    """ Find min & max in series"""
    if n<=1: return mm
    if S[n-1]>=mm[1]: mm[1]=S[n-1]
    elif S[n-1]<=mm[0]: mm[0]=S[n-1]
    return findMinMaxElement(S,n-1,mm)
# %% C-4.10 Calculate integral part of a logarithm
def integralPart(x):
    if x<2: return 0
    else: return integralPart(x/2)+1
# %% C-4.11 Element uniqueness test
def elementUnique(S,i=0,j=0):
    if j >= len(S):
        i += 1
        j = 0
    if i>=len(S):
        return True
    elif (i!=j) and (S[i]==S[j]): return False
    else:
        print(i,'#',j)
        return elementUnique(S,i,j+1)
# %% C-4.12 Calculate product of two integer using add&minus
def productFromAM(a,b):
    if a<=1: return b
    else: return b+productFromAM(a-1,b)
# %% C-4.14 Tower of Hanoi
global_step = 0
def hanoiMove(plate_id,from_pillar,to_pillar):
    """ How to move a plate on pillar"""
    global global_step
    global_step+=1
    print("step%i: move %i from %s to %s"%(global_step,plate_id,from_pillar,to_pillar))
def hanoiRecursion(plate_number,pillar1='a',pillar2='b',pillar3='c'):
    """ Move all plates from pillar1 to pillar3 with the help of pillar2"""
    if plate_number<1: return True
    else:
        hanoiRecursion(plate_number-1,pillar1,pillar3,pillar2)
        hanoiMove(plate_number,pillar1,pillar3)
        hanoiRecursion(plate_number-1,pillar2,pillar1,pillar3)
# %% C-4.15 Return all subsets of a n-member set
def allSubsets(s:list):
    """ Return all subsets of a list"""
    if len(s)==0: return [[]]
    return allSubsets(s[1:]) + [[s[0]] + i for i in allSubsets(s[1:])]
# %% C-4.16 Reverse string
def stringReverse(s:str):
    """ Return the reversed string"""
    if len(s)<1: return ''
    elif len(s)==1: return s
    return s[-1] + stringReverse(s[1:-1]) + s[0]
# %% C-4.17 Palindrome test
def palindromeTest(s:str):
    """ Return True if s is palindrome"""
    if len(s)<=1: return True
    return palindromeTest(s[1:-1]) & (s[0]==s[-1])
# %% C-4.18 Vowels more than consonants
def VowelsMore(s:str,v=0,c=0):
    """ Return True if vowels-number is more than consonants"""
    if s[0] in 'aeiou':v+=1
    else:c+=1
    if len(s)<=1: return v>c
    return VowelsMore(s[1:],v,c)
# %% C-4.19 Even before odd
def EvenFirst(L:list):
    """ Return even first then odd"""
    if len(L)<=0: return []
    if L[0]%2==0: return [L[0]]+EvenFirst(L[1:])
    else: return EvenFirst(L[1:])+[L[0]]
# %% C-4.20 Larger than k first
def LesserFirst(S:list,k):
    """ Return lesser first then large
        Time-complexity: O(n)"""
    if len(S)<=0: return []
    if S[0]<k: return[S[0]]+LesserFirst(S[1:],k)
    else: return LesserFirst(S[1:],k)+[S[0]]
# %% C-4.21 Find two-elements add-up to k
def FindTwoAdd(S,i,j,k):
    """ Return two elements sum-up to k
        Time-complexity: O(n)"""
    if i==j: return False
    else:
        if S[i]+S[j]<k: return FindTwoAdd(S,i+1,j,k)
        elif S[i]+S[j]>k:return FindTwoAdd(S,i,j-1,k)
        else: return True
# %% C-4.22 Using square to calculate power with non-recursion
def squPower(x,n):
    """ Using square to calculate x^n with no use of recursion"""
    k=0
    while 1<<k <= n: k+=1   # times need to
    ans=1
    for i in range(k-1,-1,-1):  # (k-1) -> (k-1)+1 -> ... -> 0
        ans*=ans
        if (1<<i) & n >0:   # 对应的n为奇数
            ans*=x
    return ans

# %% test


