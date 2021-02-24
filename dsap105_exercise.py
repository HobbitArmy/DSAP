"""
第五章 基于数组的序列

"""

# %% R-5.1/5.2/5.3 length of List and actual-occupied-size
import sys
data=[]
data2=[None]*100
for k in range(100):
    l=len(data); l2=len(data2)
    s=sys.getsizeof(data); s2=sys.getsizeof(data2)
    # print('Length:'+str(l)+'; Size-bytes:'+str(s))
    # data.append(None)
    # if s!=sys.getsizeof(data):
    #     print(k)
    data2.pop()
    if s2!=sys.getsizeof(data2):
        print('Length:'+str(l2)+'; Size-bytes:'+str(s2))
        print(100-k)
# %% R-5.4/5.6 使DynamicArray.__getitem__支持负索引
from dsap105_sequence import DynamicArray
class DynamicArray2(DynamicArray):
    def __getitem__(self, item):
        """ 更新__getitem__方法,使支持负索引"""
        if not -self._n <= item < self._n:
            raise IndexError('Found # Invalid Index')
        elif item < 0:
            item += self._n
        return self._A[item]
    def insert(self, k, value):
        """ 在索引k处插入值value,直接移动元素到最终位置,避免._resize方法循环移动"""
        if self._n==self._capacity:  # 若空间不足,扩充并移动
            B=self._make_array(2*self._capacity)
            for i in range(k):
                B[i] = self._A[i]
            B[k]=value
            for i in range(k+1,self._capacity+1):
                B[i] = self._A[i-1]
            self._capacity*=2
            self._A=B
        else:
            for i in range(self._n, k, -1):
                self._A[i] = self._A[i-1]
            self._A[k]=value
        self._n+=1
# %% R-5.5 数组扩增摊销计算
""" 
数组大小扩大 k -> 2k, 需要k个硬币, 其摊销需要2+1个
而扩大 k - 2k, 需要3k个情况下, 摊销需要6+1=7个
"""
# %% R-5.7 找出自然数数组A中唯一重复的整数
def find_duplicate(A):
    """ trick: 用数组中的值(自然数且不重复)作为索引"""
    t=[False]*len(A)
    for v in A:
        if t[v]:
            return v
        t[v] = True
# %% R-5.8 评估可变索引为参数的pop方法效率
from dsap105_sequence import DynamicArray
class DynamicArray3(DynamicArray):
    """ 添加索引pop方法,评估其效率"""
    def pop(self,k):
        """ pop an item from sequence"""
        value=self._A[k]
        for i in range(k,self._n-1):
            self._A[i] = self._A[i+1]
        self._A[self._n]=None
        self._n -= 1
        return value
# %% R-5.9 用于其他语言时,应将首字母改变
# %% R-5.10 简化凯撒密码构造函数为生成式
from dsap105_sequence import CassarCipher
class CassarCipher2(CassarCipher):
    """ 简写构造部分"""
    def __init__(self, shift=2):
        self._encode = ''.join(chr(i+shift)%26 + ord('A') for i in range(26))
        self._decode = ''.join(chr(i-shift)%26 + ord('A') for i in range(26))
# %% R-5.11 --
# %% R-5.12 sum计算n*n结构的数据(列表的列表实现)
def sum_2d(a):
    return sum(sum(subset) for subset in a)
# %% C-5.13 --
# %% C-5.14 重新排序列表
from random import randrange
def shuffle_list(origin:list):
    """ 随机交换任意两个元素实现随机重排"""
    for i in range(len(origin)):
        t= randrange(len(origin))
        origin[i],origin[t] = origin[t],origin[i]
# %% C-5.15 --
# %% C-5.16 实现pop方法,元素个数小于N/4时，数组大小减为一半
from dsap105_sequence import DynamicArray
class DynamicArray4(DynamicArray):
    """ 添加pop方法,评估其效率"""
    def pop(self):
        value=self._A[self._n-1]
        self._A[self._n-1]=None
        self._n-=1
        if self._n<self._capacity/4:
            self._resize(int(self._capacity/2))
        return value
# %% C-5.17~5.24 --
# %% C-5.25 实现remove_all方法,删除所有值为value的元素
def remove_all(data,value):
    keep_num=0
    for i in range(len(data)):
        if data[i] != value:
            data[keep_num] = data[i]
            keep_num+=1
    while len(data)>keep_num:
        data.pop()
# %% C-5.26 找到数组中5个重复的整数
def find_duplicate(data):
    sorted_data=sorted(data)
    for i in range(len(data)-1):
        if sorted_data[i]==sorted_data[i+1]:
            print(sorted_data[i])
# %% C-5.27~5.30 --
# %% C-5.31 递归增加元素值
def add_1d(array,value,n):
    """ 一维数组实现"""
    if n<=0:
        return array
    else:
        array[n-1]+=value
        return add_1d(array,value,n-1)















