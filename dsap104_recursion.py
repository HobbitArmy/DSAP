"""
第四章 递归

"""

# %% Factorial function implementation
def factorial(n):
    """ Return the value of n!
        Time-complexity:O(n)"""
    if n==0: return 1
    else: return n*factorial(n-1)
# %% British ruler
def drawLine(line_length,line_label=''):
    line='-'*line_length
    if line_label:
        line+=line_label
    print(line)
def drawInterval(center_length):
    if center_length>0:
        drawInterval(center_length-1)
        drawLine(center_length)
        drawInterval(center_length-1)
def drawBritishRuler(num_inches,major_length):
    """ Print British Ruler, with given inches, major trick length
        Time-complexity:O(2^n)"""
    drawLine(major_length,'0')
    for i in range(1,1+num_inches):
        drawInterval(major_length-1)
        drawLine(major_length,str(i))
# %% Binary Search
def binarySearch(data,target,low,high):
    """ Return position of target if found in data[low, high]
        Time-complexity:O(log(n))"""
    if low>high:
        return False
    else:
        mid=(low+high)//2
        if target==data[mid]:
            return mid
        elif target<data[mid]:
            return binarySearch(data,target,low,mid-1)  # mid has been tested
        else: return binarySearch(data,target,mid+1,high)
# %% Os system
import os
def diskUseage(path):
    """ Return the total bytes used by a file and any descendents
        Time-complexity:O(n)"""
    total_size=os.path.getsize(path)
    if os.path.isdir(path):
        for child_name in os.listdir(path):
            total_size+=diskUseage(os.path.join(path,child_name))
    print(total_size,'-bytes\t',path)
    return total_size
# %% 4-8 Good fibonacci
def goodFibonacci(n):
    """ Return pair of Fibonacci numbers: (F(n), F(n-1))
        Time-complexity:O(n)"""
    if n<=1:
        return n, 0
    else:
        a,b=goodFibonacci(n-1)
        return a + b, a
# %% 4-9 Recursion sum
def recursionSum(S,n):
    """ Return the first n numbers of sequence S
        Time-complexity:O(n); Space-complexity:O(n)"""
    if n==0: return 0
    else: return recursionSum(S,n-1)+S[n-1]
# %% 4-10 Recursion reverse
def recursionReverse(S,start,stop):
    """ Reverse elements in implicit sequence-slice S[start,stop]
        Time-complexity:O(n)"""
    if start<stop-1:
        S[start], S[stop-1] = S[stop-1], S[start]
        recursionReverse(S, start+1, stop-1)
# %% 4-11 Recursion power function
def recursionPower(x,n):
    """ Return x^n , in-which n is non-negative integer
        Time-complexity:O(n)"""
    if n==0: return 1
    else: return x*recursionPower(x,n-1)
# %% 4-12 Square power function
def squRecursionPower(x,n):
    """ Using square to accelerate x^n computation
        Time-complexity:O(log(n)); Space-complexity:O(log(n))"""
    if n==0: return 1
    else:
        partial=squRecursionPower(x,n//2)
        result=partial*partial
        if n%2==1:
            result*=x
        return result
# %% 4-13 Binary sum up
def binarySum(S,start,stop):
    """ Using binary to sum up
        Time-complexity:O(n); Space-complexity:O(log(n))"""
    if start>=stop: return 0
    elif start==stop-1: return S[start]
    else:
        mid=(start+stop)//2
        return binarySum(S,start,mid) + binarySum(S,mid,stop)


# %% test

