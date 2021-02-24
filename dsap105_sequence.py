"""
第五章 基于数组的序列

"""

# %% 5-1 List-length and cache-size
import sys
def list_size_test(n=10):
    data=[]
    for k in range(n):
        a=len(data)
        b=sys.getsizeof(data)
        print('Length:%d; Size in bytes:%d'%(a,b))
        data.append(None)
# %% 5-3 Implement DynamicArray using ctypes-method
import ctypes
class DynamicArray:
    """ A dynamic array class akin to Python-list"""
    def __init__(self):
        """ Create an empty array"""
        self._n=0           # 动态数组长度
        self._capacity=1    # 动态数组容量
        self._A=self._make_array(self._capacity)
    def __len__(self):
        """ Return numbers of elements in array"""
        return self._n
    def __getitem__(self, item):
        """ Return element at index item"""
        if not 0<=item<self._n:
            raise IndexError('Found # Invalid Index')
        return self._A[item]
    def __str__(self):
        """ To show this data-struct"""
        return 'd'+str(self._A[:self._n-1])+'d'
    def append(self,obj):
        """ Add object to the end of array"""
        if self._n==self._capacity:
            self._resize(2*self._capacity)
        self._A[self._n]=obj
        self._n+=1
    # 5-5 添加元素方法
    def insert(self, k, value):
        """ 在索引k处插入值value"""
        if self._n==self._capacity:  # 若空间不足,扩充
            self._resize(2*self._capacity)
        for i in range(self._n, k, -1):
            self._A[i] = self._A[i-1]
        self._A[k]=value
        self._n+=1
    # 5-6 删除元素方法
    def remove(self,value):
        """ 删除值为value的第一次出现的元素"""
        for i in range(self._n):
            if self._A[i] == value:
                for j in range(i,self._n-1):
                    self._A[j] = self._A[j+1]
                self._n-=1
                return
        raise ValueError(' Announced Value not found.')
    def _resize(self,c):
        """ 为数组动态扩增提供支持 Resize the internal array"""
        B=self._make_array(c)
        for i in range(self._n):
            B[i]=self._A[i]
        self._A=B
        self._capacity=c
    # @staticmethod   # 静态方法无需实例化类即可在外部调用
    def _make_array(self, c):
        """ 调用ctypes模块创建底层数组 Return new array with capacity-c"""
        return (c*ctypes.py_object)()
# %% 5-4 测量列表类增添操作的摊销花费
from time import time
def compute_average_amortization_time(n):
    """ 计算向列表中加入n个元素时的平均摊销时间花费
        结果得到：每个append的摊销时间独立于n"""
    temp=[]
    time_start=time()
    for i in range(n):
        temp.append(None)
    time_end=time()
    return (time_end-time_start)/n
# %% 5-7 GameEntry类用于存储玩家姓名和得分
class GamePlayer:
    """ 表示对每个玩家的信息记录"""
    def __init__(self,name,score):
        self._name = name
        self._score = score
    def get_name(self):
        return self._name
    def get_score(self):
        return self._score
    def __str__(self):
        return '[{0}:{1}]'.format(self._name,self._score)
# %% 5-8 Scoreboard类 用于实现计分榜功能
class Scoreboard:
    """ 将高分更新至容量有限的计分榜上"""
    def __init__(self, capacity=6):
        self._board = [None]*capacity   # 保留计分空间
        self._n = 0     # 计分榜上已有记录的个数
    def __getitem__(self, item):
        """ 返回索引为item处的元素"""
        return self._board[item]
    def __str__(self):
        """ 返回计分榜的字符串表示"""
        return '\n'.join(str(self._board[i]) for i in range(self._n))
    def add(self,entry):
        """ 尝试添加一个元素到计分榜上"""
        score=entry.get_score()
        if self._n<len(self._board) or self._board[-1].get_score()<=score:
            # 计分榜未满 或 新分数大于等于榜上最小值
            if self._n<len(self._board):
                self._n+=1  # 先扩充一个
            j=self._n-1
            while j>0 and self._board[j-1].get_score()<score:
                self._board[j] = self._board[j-1]
                j-=1
            self._board[j]=entry
# %% 5-10 Insertion_sort 插入排序算法
def insertion_sort(A):
    """ 将列表元素按非减顺序排列"""
    for i in range(1,len(A)):
        cur=A[i]
        j=i
        while j>0 and A[j-1]>cur:
            A[j] = A[j-1]
            j-=1
        A[j]=cur
# %% 5-11 CaesarCipher 凯撒密码加密解密
class CassarCipher:
    """ 用于将字符串通过凯撒密码加密或解密"""
    def __init__(self,shift=2):
        """ 建立凯撒密码的整数编号替换表"""
        encoder = [None]*26
        decoder = [None]*26
        for i in range(26):
            encoder[i] = chr((i+shift)%26 + ord('A'))
            decoder[i] = chr((i-shift)%26 + ord('A'))
        self._encode_table = ''.join(encoder)
        self._decode_table = ''.join(decoder)
    def encrypt(self, message):
        """ 返回加密后的字符串"""
        return self._transform(message, self._encode_table)
    def decrypt(self, message):
        """ 返回解密后的字符串"""
        return self._transform(message, self._decode_table)
    def _transform(self, original_msg, code):
        """ 根据所给的编码加密或解密"""
        msg = list(original_msg)
        for i in range(len(original_msg)):
            if msg[i].isupper():
                j=ord(msg[i])-ord('A')
                msg[i]=code[j]
        return ''.join(msg)
# %% 5-12 TicTacToe 三连棋
class TicTacToe:
    """ 井字棋的类实现"""
    def __init__(self):
        """  开始游戏 初始化棋盘"""
        self._board=[[' ']*3 for i in range(3)]
        self._player='X'
        print('井字棋游戏开始，请输入TicTacToe.mark(i,j)表示下棋位置')
    def mark(self,i,j):
        """ 放置X或O到(i,j)位置"""
        if not(0<=i<=2 and 0<=j<=2):
            raise ValueError('Invalid board position')
        if self._board[i][j] != ' ':
            raise ValueError('Board position occupied')
        if self.winner() is not None:
            raise ValueError('Game is already done!')
        self._board[i][j] = self._player
        print(self.__str__())
        print(self.winner())
        if self._player=='X':
            self._player='O'
        else:self._player='X'
    def _is_win(self,mark):
        """ 检查该步是否会得出赢家"""
        board = self._board
        return (mark == board[0][0] == board[0][1] == board[0][2] or
                mark == board[1][0] == board[1][1] == board[1][2] or
                mark == board[2][0] == board[2][1] == board[2][2] or
                mark == board[0][0] == board[1][0] == board[2][0] or
                mark == board[0][1] == board[1][1] == board[2][1] or
                mark == board[0][2] == board[1][2] == board[2][2] or
                mark == board[0][0] == board[1][1] == board[2][2] or
                mark == board[0][2] == board[1][1] == board[2][0])
    def winner(self):
        """ 返回胜利玩家标号 或None表示平局"""
        for mark in 'XO':
            if self._is_win(mark):
                return 'Winner is '+mark
        return 'Game unfinished'
    def __str__(self):
        """ 返回字符串表示当前棋盘"""
        rows=['|'.join(self._board[i]) for i in range(3)]
        return '\n-----\n'.join(rows)

# %% test
if __name__=='__main__':
    a = DynamicArray()
    a._make_array(102400000)
    sys.getsizeof(a)
    # 5-11
    cipher1=CassarCipher(2)
    message='THIS IS NOT A BIG DEAL!'
    encode_msg=cipher1.encrypt(message)
    print('encode_msg:',encode_msg,'\ndecode_msg:',cipher1.decrypt(encode_msg))
    # 5-12
    game=TicTacToe()
    game.mark(1,1)
    game.mark(2,0)
    game.mark(2,2)
    game.mark(0,0)
    game.mark(1,2)
    game.mark(1,0)
    game.mark(0,1)
