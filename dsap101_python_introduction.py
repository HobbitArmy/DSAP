"""
第一章 Python入门

"""

# %% 1.5.1 函数信息传递
# 名称只是标识符,指向对象为同一
l=[[1],[2],[3]]
for i in l: i.append('a')
l   # i被视为一个标准标识符,与l中的元素只是同一对象的别名
def l_extend_1(li): li.append('1')
l_extend_1(l)
l   # 不同作用域标识符为同一对象别名,此例中函数内局部作用域
# 函数也是第一类对象
def sum(g): print('Redefine sum')


sum(k * k for k in range(0, 10))
# %% 1.5.2 内置函数
# 迭代器
l_iter=iter(l)  # 返回一个新的'迭代对象'
next(l_iter)    # 返回'迭代器生成对象'的下一个元素
# 哈希
hash(10)
hash('10')
# 数学运算
divmod(9.5,3)   # 返回商和余数
pow(3,2)
pow(3,2,5)  # (3**2)%5
round(1.4)  # 四舍五入取整
round(0.6156565465,3)    # 保留小数点后3位
# %% 1.6 文件读写
l_str = [str(l_i) for l_i in l]  # 只能写入string
file=open('da101.txt','a')  # 尾部追加
file2=open('da101.txt','r')  # 只读
file2.seek(0)   # 定位当前位置到开头
for line in file2: print(line,end='',sep='-')  # 取消结尾换行
print(file2.tell())  # 返回当前位置偏离字节数
file2.seek(10)      # 定位到第10个字节
print(file2.read(15))   # 换行视为一个字节
print(file2.readline())  # 读取改行剩余部分
file2.close()
file.write('file.write\n')  # file.write(str)默认结束无换行
file.writelines(l_str)  # 写入string序列
print('da101',file=file)    # 将print的输出重新定向给文件，此处末尾有换行
print('print',file=file)
file.close()
# %% 1.7 异常处理
def your_age():
    try:
        bir_year=int(input('Enter your birth year:'))
        if bir_year>2020:
            print('Haven\'t been born, Bro ?')
    except (ValueError,EOFError):
        print('***Invalid Input!***')
        return 'Please enter integer of the year'
        #raise  # 继续输出错误异常
    return 2020-bir_year
# %% 1.8 迭代器和生成器
l=[[1],[2],3,4]
l_iter=iter(l)  # 返回一个新的'迭代对象'
next(l_iter).append(2)    # 返回'迭代器生成对象'的下一个元素
l   # 迭代器保存原始列表的当前索引,该索引指向下一个元素
def factors(start,end):  # yield的存在表明这是个生成器,而不是传统函数
    for k in range(start,end+1):
        if end%k==0: yield k    # yield生成并返回一个迭代器iterator
iter_factors = factors(11,100)  # 计算从start开始,end的因子
next(iter_factors)
def fibonacci():    # 斐波那契数列
    a=0; b=1
    while True:
        yield a
        c=a+b;a=b;b=c
iter_fibonacci=fibonacci()
for i in range(10): print(next(iter_fibonacci))
# %% 1.9 Python-Tricks
print(i*2 if i>0 else i/2)  # 条件表达式 大于零加倍,否则减半
# 解析语法/生成式
a=[k*k for k in range(0,10) if k%2!=0]  # 范围内奇数平方
b={k*k for k in range(0,10) if k%2!=0}  # 生成集合
c=(k*k for k in range(0,10) if k%2!=0)  # 生成器 next(c)
d={k:k*k for k in range(0,10) if k%2!=0}  # 生成字典
sum(k * k for k in range(0, 10))    # 生成器用于函数参数
# 序列的自动打包和解包
tuple_da=1,2,3,4    # 右侧打包
a,b,c,d=range(4)    # 右侧解包
b,c=c,b  # 同时分配技术,先计算右侧,打包后,赋值给左侧
def simplify_fibonacci():   # 语句简化后的斐波那契数列
    a,b=0,1     # 同时分配简化
    while True:
        yield a
        a,b=b,b+a   # 同时分配简化
s_fib = simplify_fibonacci()
[next(s_fib) for i in range(10)]    # 列表生成式简化
# %% 1.10 作用域和命名空间
dir()   # 返回命名空间中标识符名称
vars()  # 返回完整的字典{标识符:值}

