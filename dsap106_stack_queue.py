"""
第六章 栈、队列和双端队列

"""
# %% 6-1 Empty异常类错误定义
class Empty(Exception):
    """ Error: attempting to access an element from an empty stack"""
    pass
# %% 6-2 用列表实现一个栈
class ArrayStack:
    """ LIFO Stack implemented by a list as underlying storage"""
    def __init__(self):
        """ Create an empty stack"""
        self._data=[]
    def __len__(self):
        """ Return number of elements in the stack"""
        return len(self._data)
    def is_empty(self):
        """ Return True if stack is empty"""
        return len(self._data)==0
    def push(self,e):
        """ Push an element to the top of the stack"""
        self._data.append(e)
    def top(self):
        """ Return(but not remove) the element on the top"""
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]
    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()
# %% 6-3 逆置文件中各行
def reverse_file(filename):
    """ Overwrite given file with its contents reversed line-by-line"""
    S=ArrayStack()
    original = open(filename)
    for line in original:
        S.push(line.rstrip('\n'))
    original.close()
    output=open(filename,'w')   # overwrites original
    while not S.is_empty():
        output.write(S.pop()+'\n')
    output.close()
# %% 6-4 算术表达式分隔符匹配检验
def is_matched_arithExpression(expr):
    """ Return True if all delimiters are properly match, False otherwise"""
    start_mark = '([{'
    end_mark = ')]}'
    S=ArrayStack()
    for c in expr:
        if c in start_mark:
            S.push(c)
        elif c in end_mark:
            if S.is_empty():
                return False
            elif end_mark.index(c) != start_mark.index(S.pop()):
                return False
    return S.is_empty()  # all symbols matched
# %% 6-5 HTML标签匹配检验
def is_matched_html(html_file):
    """ Return True if all HTML tags are properly match, False otherwise"""
    S = ArrayStack()
    file = open(html_file, 'r', encoding='utf-8')
    content = file.read()
    file.close()
    j=content.find('<')
    while j!= -1:   # '<' found
        k = content.find('>',j+1)
        if k==-1:   # '>' not found
            return False
        tag = content[j+1:k]    # tag in <>
        if not tag.startswith('/'):
            S.push(tag)     # start tage
        else:
            if S.is_empty():
                return False
            elif tag[1:] != S.pop():
                return False
        j=content.find('<',k+1)
    return S.is_empty()
# %% 6-6&6-7 基于数组的队列实现
class ArrayQueue:
    """ FIFO queue implementation using List as underlying storage"""
    INIT_CAPACITY = 10
    def __init__(self):
        """ Create an empty queue"""
        self._data=[None]*self.INIT_CAPACITY    # an instance of List-class
        self._size=0        # number of elements in the queue
        self._front=0       # index of the first element
    def __len__(self):
        """ Return number of elements in the queue"""
        return self._size
    def is_empty(self):
        """ Return True if the queue is empty"""
        return self._size==0
    def first(self):
        """ Return(but not remove) the element at the front of the queue """
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]
    def dequeue(self):
        """ Remove and Return the element at the front of the queue"""
        if self.is_empty():
            raise  Empty('Queue is Empty')
        value=self._data[self._front]
        self._data[self._front]=None
        self._front=(self._front+1)%len(self._data)
        self._size-=1
        return value
    def _resize(self,capacity):
        """ Resize to a new list capacity(>=self._size)"""
        original=self._data     # keep track of original list
        self._data=[None]*capacity
        walk=self._front
        for i in range(self._size):
            self._data[i]=original[walk]
            walk=(walk+1)%len(original)
        self._front=0
    def enqueue(self,e):
        """ Add an element to the bottom of the queue """
        if self._size==len(self._data):
            self._resize(2*self._size)
        bottom_index = (self._front+self._size)%len(self._data)
        self._data[bottom_index] = e
        self._size+=1

