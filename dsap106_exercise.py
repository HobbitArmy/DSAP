"""
第六章 栈、队列和双端队列
练习题

"""
# %% R-6.1~6.2 --
# %% R-6.3 栈转移
from dsap106_stack_queue import ArrayStack
def stackTransfer(S:ArrayStack,T:ArrayStack):
    while not S.is_empty():
        T.push(S.pop())
# %% R-6.4 栈清除-递归
def stackClean(S:ArrayStack):
    if S.is_empty():
        return True
    else:
        S.pop()
        return stackClean(S)
# %% R-6.5 栈实现列表逆置
def reverseList(L):
    s = ArrayStack()
    [s.push(i) for i in L]
    for j in range(len(L)):
        L[j] = s.pop()
    return L
# %% C-6.16~6.17 栈容量限制
from dsap106_stack_queue import ArrayStack
class StackFull(Exception):     # 定义栈满异常
    """ Error: attempting to access an element to a full stack"""
    pass
class ArrayStack2(ArrayStack):
    """ With a limitation og stack continent"""
    def __init__(self, maxlen=None):
        super().__init__()
        self.maxlen = 6 if maxlen is None else maxlen
        self._data=[None]*self.maxlen
    def push(self,e):
        """ Push an element to the top of the stack"""
        if self.__len__() == self.maxlen:
            raise StackFull('Stack is Full')
        self._data.append(e)
# %% C-6.18 --
# %% C-6.19 允许检验HTML中带属性的标签
def is_matched_html2(html_file):
    """ Return True if all HTML tags are properly match, False otherwise"""
    S = ArrayStack()
    file = open(html_file, 'r', encoding='utf-8')
    content = file.read()
    file.close()
    j=content.find('<')
    while j!= -1:   # '<' found
        k = content.find('>', j)
        if k==-1:   # '>' not found
            return False
        tag = content[j+1:min(k, content.find(' ', j+1))]    # tag in <>
        print(tag)
        if not tag.startswith('/'):
            S.push(tag)     # start tage
        else:
            if S.is_empty():
                return False
            elif tag[1:] != S.pop():
                return False
        j=content.find('<',k)
    return S.is_empty()
# %% C-6.20 栈实现前n个自然数的所有排列结果

