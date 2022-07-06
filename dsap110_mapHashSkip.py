"""
第十章 映射,哈希表和跳跃表

"""

# %% 10-1 单词频率统计
def word_frequence(filename='da110.txt'):
    ants_word = ['the', 'and', 'are', 'is', 'of', 'in', 'on',
                 'we', 'do', 'to', 'you', 'our', 'us']
    freq = {}
    for piece in open(filename, encoding='UTF-8').read().lower().split():
        word = ''.join(c for c in piece if c.isascii()and c.isalpha())
        if word:
            freq[word] = 1+freq.get(word, 0)
            # dict.get(key,value) 若key不存在，返回value；否则返回dict[key]
    max3_word = ['','','']
    max3_count = [0,0,0]
    for (w,c) in freq.items():
        if w not in ants_word:
            if c>max3_count[2]:
                if c>max3_count[1]:
                    if c>max3_count[0]:
                        max3_word[0], max3_count[0] = w, c
                    else:
                        max3_word[1], max3_count[1] = w, c
                else:
                    max3_word[2], max3_count[2] = w, c
    print('most frequent word:',max3_word, 'occurs times', max3_count)
    return max3_word, max3_count
# %% 10-2 映射基类
from collections import MutableMapping
class MapBase(MutableMapping):
    """ 包含了_Item非公有类的抽象基类"""
    class _Item:
        __slots__ = '_key','_value'
        def __init__(self, k, v):
            self._key = k
            self._value = v
        def __eq__(self, other):
            return self._key==other._key
        def __ne__(self, other):
            return not (self==other)
        def __lt__(self, other):
            return self._key<other._key
# %% 10-3 列表 实现非排序表的map
class UnsortedTableMap(MapBase):
    """ 非排序列表的map实现"""
    def __init__(self):
        self._table = []
    def __getitem__(self, k):
        """ return key-item's value"""
        for i in self._table:
            if k==i._key:
                return i._value
        raise KeyError('key error:'+repr(k))
    def __setitem__(self, key, value):
        for item in self._table:
            if key==item._key:
                item._value = value
                return
        self._table.append(self._Item(key, value))
    def __delitem__(self, key):
        for i in range(len(self._table)):
            if key==self._table[i]._key:
                self._table.pop(i)
                return
        raise KeyError('key error:'+repr(key))
    def __len__(self):
        return len(self._table)
    def __iter__(self):
        for item in self._table:
            yield item._key
# %% 10-4 哈希表实现基类
from random import randrange
class HashMapBase(MapBase):
    """ 用MAD(Multiply-Add-Divide)压缩函数的哈希表实现 映射基类"""
    def __init__(self, cap=11, p=109345121):
        """ 映射区间为[0,N-1], p为比中N大的素数, """
        self._table = cap*[None]    # 桶数组
        self._n = 0     # 哈希表中不同元组的个数
        self._prime = p  # 素数
        self._scale = 1+randrange(p-1)
        self._shift = randrange(p)
    def _hash_function(self, k):
        return (hash(k)*self._scale+self._shift)%self._prime%len(self._table)
    def __len__(self):
        return self._n
    def __getitem__(self, k):
        i = self._hash_function(k)
        return self._bucket_getitem(i,k)
    def __setitem__(self, key, value):
        i = self._hash_function(key)
        self._bucket_setitem(i, key, value)
        if self._n>len(self._table)//2:
            self._resize(2*len(self._table)-1)
    def __delitem__(self, key):
        i = self._hash_function(key)
        self._bucket_delitem(i, key)
        self._n-=1
    def _resize(self, c):
        old = list(self.items())
        self._table = c*[None]
        self._n = 0
        for (k,v) in old:
            self[k] = v
# %% 10-5 分离链表实现哈希映射
class ChainHashMap(HashMapBase):
    """ 用分离链表解决冲突 实现哈希表"""
    def _bucket_getitem(self, i, k):
        bucket = self._table[i]
        if bucket is None:
            raise KeyError('key error:'+repr(k))
        return bucket[k]
    def _bucket_setitem(self, j, k, v):
        if self._table[j] is None:
            self._table[j] = UnsortedTableMap()
        oldsize = len(self._table[j])
        self._table[j][k] = v
        if len(self._table[j]) > oldsize:
            self._n+=1
    def _bucket_delitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('key error'+repr(k))
        del bucket[k]
    def __iter__(self):
        for bucket in self._table:
            if bucket is not None:
                for key in bucket:
                    yield key
# %% 10-6 线性探测-开放寻址实现哈希映射
class ProbeHashMap(HashMapBase):
    """ 用线性探测处理冲突 实现哈希表"""
    _AVAIL = object()   # 用于标记上一次删除的位置
    def _is_available(self, j):
        return self._table[j] is None or self._table[j] is ProbeHashMap._AVAIL
    def _find_slot(self, j, k):
        """ 在索引j，寻找键k"""
        firstAvail = None
        while True:
            if self._is_available(j):
                if firstAvail is None:
                    firstAvail = j
                if self._table[j] is None:
                    return (False, firstAvail)
            elif k==self._table[j]._key:
                return (True, j)
            j = (j+1)%len(self._table)
    def _bucket_getitem(self, j, k):
        found, s = self._find_slot(j, k)
        if not found:
            raise KeyError('key error:'+repr(k))
        return self._table[s]._value
    def _bucket_setitem(self, j, k, v):
        found, s = self._find_slot(j, k)
        if not found:
            self._table[s] = self._Item(k, v)
            self._n+=1
        else:
            self._table[s]._value = v
    def _bucket_delitem(self, j, k):
        found, s = self._find_slot(j, k)
        if not found:
            raise KeyError('key error:'+repr(k))
        self._table[s] = ProbeHashMap._AVAIL
    def __iter__(self):
        for j in range(len(self._table)):
            if not self._is_available(j):
                yield self._table[j]._key
# %% 10-8 排序检索表
class SortedTableMap(MapBase):
    """ 用排序表 实现映射"""
    def _find_index(self, k, low, high):
        """ 返回在[low,high]范围内 >=k 的第一个位置索引
        如果不存在,返回high+1"""
        if high<low:
            return high+1
        else:
            mid = (low+high)//2
            if k==self._table[mid]._key:
                return mid
            elif k<self._table[mid]._key:
                return self._find_index(k, low, mid-1)
            else:
                return self._find_index(k, mid+1, high)
    def __init__(self):
        self._table = []
    def __len__(self):
        return len(self._table)
    def __getitem__(self, k):
        """ 返回键为k的值"""
        j = self._find_index(k, 0, len(self._table)-1)
        if j==len(self._table) or self._table[j]._key!=k:
            raise KeyError('key error:'+repr(k))
        return self._table[j]._value
    def __setitem__(self, key, value):
        j = self._find_index(key, 0, len(self._table)-1)
        if j<len(self._table) and self._table[j]._key==key:
            self._table[j]._value = value   # 重设值
        else:
            self._table.insert(j, self._Item(key, value))   # 插入新单元
    def __delitem__(self, key):
        j = self._find_index(key, 0, len(self._table)-1)
        if j==len(self._table) or self._table[j]._key!=key:
            raise KeyError('key error:'+repr(key))
        self._table.pop(j)
    def __iter__(self):
        for item in self._table:
            yield item._key
    def __reversed__(self):
        """ 生成反向的键 从最大到最小"""
        for item in reversed(self._table):
            yield item._key
    def find_min(self):
        if len(self._table)>0:
            return (self._table[0]._key, self._table[0]._value)
        else:
            return None
    def find_max(self):
        if len(self._table)>0:
            return (self._table[-1]._key, self._table[-1]._value)
        else:
            return None
    def find_ge(self, k):
        """ greater than or equal"""
        j = self._find_index(k, 0, len(self._table)-1)
        if j<len(self._table):
            return (self._table[j]._key, self._table[j]._value)
        else:
            return None
    def find_lt(self, k):
        j = self._find_index(k, 0, len(self._table)-1)
        if j>0:
            return (self._table[j-1]._key, self._table[j-1]._value)
        else:
            return None
    def find_gt(self, k):
        j = self._find_index(k, 0, len(self._table)-1)
        if j<len(self._table) and self._table[j]._key==k:
            j+=1
        if j<len(self._table):
            return (self._table[j]._key, self._table[j]._value)
        else:
            return None
    def find_range(self, start, stop):
        if start is None:
            j = 0   # 从映射的最小键开始
        else:
            j = self._find_index(start, 0, len(self._table)-1)
        while j<len(self._table) and (stop is None or self._table[j]._key < stop):
            yield (self._table[j]._key, self._table[j]._value)
            j+=1






















