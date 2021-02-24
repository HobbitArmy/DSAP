"""
第一章 python入门

"""

# %% R1.1    检查n为m的倍数
def is_multiple(n, m):
    if n % m == 0: return True
    return False
# %% R1.2    检查k是否为偶数
def is_even(k):
    while k != 0:
        k = k - 2 if k > 0 else k + 2
        if k == 1 | -1: return False
    return True
# %% R1.3    找出序列中最小和最大数,以len=2元组返回
def minmax(data):
    mi = ma = data[0]
    for i in data:
        if i < mi: mi = i
        if i > ma: ma = i
    return mi, ma
# %% R1.4    返回1~n的平方和
def sum_square_n(n):
    sum_s_n = 0
    for k in range(n + 1): sum_s_n += k * k
    return sum_s_n
# %% R1.5    用解析语法和sum写单独命令求R1.4题
sum([k * k for k in range(5 + 1)])
# %% R1.6    返回1~n奇数平方和
def sum_square_odd(n):
    sum_s_o = 0
    # 只循环奇数
    for k in range(1, n + 1, 2): sum_s_o += k * k
    return sum_s_o
# %% R1.7    解析语法和sum求解R1.6
sum(k * k for k in range(1, 5 + 1, 2))
# %% R1.8    -n<=k<0,求j>=0,使s[k]=s[j]
s = 'asdasd'
n = len(s)
k = -3
print(s[n + k] == s[k])  # j=n+k
# %% R1.10   生成序列8,6,4,2...-4,-6,-8
temp = [e for e in range(8, -9, -2)]
# %% R1.11   列表解析法生成[1,2,4,...,256]
square_2 = [2 ** i for i in range(0, 9)]
# %% R1.12   用randrange实现choice(data)
from random import randrange
def rand_choice(data):  # randrange(start,stop,step)
    return data[randrange(0, len(data))]
# %% C1.13   输出逆序列表的函数
def reverse_list(list_n):
    l = len(list_n)
    return [list_n[l - i] for i in range(1, l + 1)]
# %% C1.14   判断整数序列中是否有乘积为奇数的不相同数
def find_odd_different(seq):
    for i in seq:
        for j in seq:
            if i != j and not is_even(i * j):
                return i, j
    return None
# %% C1.15   判断所有数字互不相同
def find_all_different(seq):
    l = len(seq)
    for i in range(l):
        if seq[i] in seq[0:i] + seq[i + 1:l]:
            return False
    return True
# %% C1.16   传入函数的data是形参,是原实参的别名,因此可通过赋值改变原data
def scale(data, factor):
    print(data)
    for k in range(len(data)):
        data[k] *= factor
    print(data)
# %% C1.17  for val in data: val*=factor不可改变传入的data,因为val为本地变量
def scale2(data, factor):
    for i in data:
        i *= factor
    print(data)
# %% C1.18  列表解析语法产生[0,2,6,...,56,72,90]
temp = [i * (i + 1) for i in range(10)]
# %% C1.19   列表解析产生['a','b','c',...,'z']
temp = [chr(i) for i in range(ord('a'), ord('z') + 1)]
# %% C1.20   randint实现shuffle
from random import randint
def randint_shuffle(data):
    output = []
    while data:
        output.append(data.pop(randint(0, len(data) - 1)))
    data += output
# %% C1.21  读取行,直到抛出异常;然后逆行序输出
def eof_error_test():
    store_list = []
    while True:
        try:
            store_list.append(input('input line'))
        except (EOFError, KeyboardInterrupt):
            print('End-Of-File Error')
            break
        except:
            print('\nUnknown Error')
            break
    while store_list:
        print(store_list.pop())
# %% C1.22  求两个等长整型数组的点积
def dot_product(a,b):
    c=[]
    for i in range(len(a)): c.append(a[i]*b[i])
    return c
# %% C1.23  索引越界异常捕获
def index_error_test():
    a_2=[0,1]
    try: print(a_2[2])
    except IndexError:
        print('***⚠Buffer Overflow Attacks Warning⚠***'
              '\n***⚠缓冲区溢出攻击警告⚠***')
        raise
# %% C1.24  统计字符串中元音字母个数
def aeiou_number(str):
    aeiou=['a','e','i','o','u']
    num=0
    for i in str:
        if i in aeiou: num+=1
    return num
# %% C1.25  字符串清除标点
def clear_punctuation(str):
    output=''
    for item_s in str:
        if ord('a') <= ord(item_s) <= ord('z') or\
                ord('A') <= ord(item_s) <= ord('Z') or\
                ord(item_s)==ord(' '):
            output+=item_s
    return output
# %% C1.26  直角三角形检验:勾股定理
def gougu(a,b,c):
    square_a=a*a;square_b=b*b;square_c=c*c
    square_sum=square_a+square_b+square_c
    if square_sum-2*square_a==0 or square_sum-2*square_b==0 or\
        square_sum-2*square_c==0:
        return True
    return False
# %% C1.27  顺序化求因子
def ordered_factors(n):
    k=1;buffer=[]
    while k*k<n:
        if n%k==0:
            yield k
            buffer.append(n//k)
        k+=1
    if k*k==n:
        yield k
    for b in reversed(buffer):
        yield b
a=ordered_factors(20)
while(True):
    try:print(next(a))
    except:print('over');break
# %% C1.28  求向量v的p范数
def norm_vp(v,p=2):
    temp=0
    for i in v:
        temp+=i**p
    return temp**(1/p)

# %%% *P1.29  输出字符串内字符组成的所有可能字符串(相同字母仅用一次)
def all_possible_string(str_list, permutation):
    # 使用递归来生成所有可能的组合
    if len(str_list)==0:
        print(''.join(permutation))
        # 每当permutation中加载好一种组合可能,打印输出
    else:
        for k in range(len(str_list)):
            permutation.append(str_list.pop(k))
            # 取出str_list中k位置字符,并加到permutation末尾
            all_possible_string(str_list,permutation)
            # 递归,将改变后的str_list,permutation传输给本函数
            str_list.insert(k,permutation.pop())
            # 将本次循环中,先前取出的k位置字符放回str_list中
# %% P1.30  求该数正整数可被2整除至商小于2的次数
def find_divd_by2_num(the_num):
    # 普通迭代解法,实则为求以2为底的对数 int(math.log(n))
    n=0; k=2
    while k>=2:
        k=the_num//2
        n+=1
    return n
def recursion_divid_by2_num(the_num,n=0):
    # 递归求解
    # print(the_num)
    the_num//=2
    if the_num>=2:
        n=n+1
        recursion_divid_by2_num(the_num,n)
    else:
        print(n)
        return n    # None ???
# %% P1.31  找零钱
def recursion_give_change(change,denomination):
    change_list=[0,0,0,0,0,0]
    for i in range(1,len(change_list)+1):
        div,mod=divmod(change,denomination[-i])
        if div>0:
            change_list[-i]=div
            change=mod
    return change_list
def give_change(price,paid_money):
    if price>paid_money:
        print('Money Paid Not Enough'); return
    elif price==paid_money:
        print('Thanks, No Change'); return
    denomination=[1,5,10,20,50,100]
    change=paid_money-price
    change_list=recursion_give_change(change,denomination)
    print('找您',end='')
    for c in range(len(change_list)):
        if change_list[c]>0: print(
                change_list[c],'个{',denomination[c],'}块的 ',end=',')
# %% P1.32&33  计算器项目,控制台每行为一次按键输入,可为数字/运算符号/复位/清除操作

# %% P1.34  编号所有句子,并随机选择8处加入小错误
# %% P1.35  生日悖论 n>23时 有两人生日相同的可能性超过一半
import random
def same_birthday_num(n):
    birthday_list=[]
    for i in range(n):
        birthday_list.append((random.randint(1,12), random.randint(1,30)))
    return not find_all_different(birthday_list)
def probability_same_bd(n,k):
    numerator=0
    for i in range(k):
        if same_birthday_num(n)==True: numerator+=1
    return numerator/k
# %% P1.36  单词列表每个词次数统计
def word_arise_times(word_list):
    word_dict={}
    for word in word_list:
        if word in word_dict:
            word_dict[word]=word_dict[word]+1
        else:
            word_dict[word]=1
    return word_dict
words_list=['a','b','c','d','a']

