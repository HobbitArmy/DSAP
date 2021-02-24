"""
第二章 面向对象编程

"""

# %% R2.1 生死攸关的软件应用
""" 放射性医疗器械控制/游乐园刺激设施的软件控制/一些高危险系数的实验仪器中的软件控制/飞机导航控制系统"""
# %% R2.2 适应性对产品销售和破产的生命周期
""" 支付宝需要顺应支付的需求 增删一些功能"""
# %% R2.3 文本编辑器GUI的组件
""" 窗口/文件交互/字体显示/等"""
# %% R2.4 Flower类
class Flower:
    """ a class of flower, which include <str>name/<int>petal_number/<float>price"""
    def __init__(self,name='daisy',petal_number=8,price=12.5):
        self._name=name
        self._petal_number=petal_number
        self._price=price
    def set_name(self,name):
        if isinstance(name,str):
            self._name=name
            return True
        return False
    def set_petal_number(self,petal_number):
        if isinstance(petal_number,int):
            self._petal_number=petal_number
            return True
        return False
    def set_price(self,price):
        if isinstance(price,float)|isinstance(price,(int,float)):
            self._price=price
            return True
        return False
    def get_name(self):
        return self._name
    def get_petal_number(self):
        return self._petal_number
    def get_price(self):
        return self._price
# %% R2.5 使charge和make_payment确保传递参数为数字/2.6 make_payment负值检验/2.7 允许初始化余额不为零/2.30
class CreditCard:
    def __init__(self,customer,bank,account,limit,balance=0):
        self._customer=customer     # _variable AKA nonpublic
        self._bank=bank
        self._account=account
        self._limit=limit
        self._balance=balance
    def get_customer(self):
        """name of the customer"""
        return self._customer
    def get_bank(self):
        return self._bank
    def get_account(self):
        """card id number"""
        return self._account
    def get_balance(self):
        return self._balance
    def get_limit(self):
        return self._limit
    def _set_balance(self,b):
        """ change balance (indirectly access _balance)"""
        self._balance=b
    def charge(self,price):
        """Charge given to the card, Return True if charge processed, else False"""
        if not isinstance(price,(int,float)):
            raise TypeError('elements must be numeric')
        if price+self._balance>self._limit:
            return False
        else:
            self._balance+=price
            return True
    def make_payment(self,amount):
        """Reduce amount from balance"""
        if not isinstance(amount,(int,float)):
            raise TypeError('elements must be numeric')
        elif amount<0:
            raise ValueError('payment cannot be negative')
        self._balance-=amount
# %% R2.9 实现Vector类的__sub__和/R2.10 __neg__方法/R2.11 []+u=u+[]/R2.12 __mul__/R2.13 __rmul__
class Vector2:  # R2.14 __mul__ u*v/R2.15 v=Vector([1,2,3])
    """Multi-d vector representation"""
    def __init__(self,d):
        """create a d-D vector"""
        if isinstance(d,int):
            self._coordinates=[0]*d
        if isinstance(d,(list,tuple)):
            self._coordinates=d
    def __len__(self):
        """return vector dimension"""
        return len(self._coordinates)
    def __getitem__(self, item):
        """return vector[item]"""
        return self._coordinates[item]
    def __setitem__(self, key, value):
        """set vector[key] as value"""
        self._coordinates[key]=value
    def __add__(self, other):
        """vector addition"""
        if len(self)!=len(other):
            raise ValueError('dimension inconsistent')
        result=Vector2(len(self))
        for v in range(len(self)):
            result[v]=self[v]+other[v]
        return result
    def __sub__(self, other):
        """vector subtraction"""
        if len(self)!=len(other):
            raise ValueError('dimension inconsistent')
        result=Vector2(len(self))
        for v in range(len(self)):
            result[v]=self[v]-other[v]
        return result
    def __neg__(self):
        result=Vector2(len(self))
        for v in range(len(self)):
            result[v]=-self[v]
        # for v in range(len(self)):    # directly change itself
        #     self[v]=-self[v]
        return self
    def __radd__(self, other):
        return self+other
    def __mul__(self, other):
        if isinstance(other,(int,float)):
            result=Vector2(len(self))
            for v in range(len(self)):
                result[v]=self[v]*other
        elif isinstance(other,Vector2)&(len(other)==len(self)):
            result=0
            for v in range(len(self)):
                result+=other[v]*self[v]
        return result
    def __rmul__(self, other):
        return self*other
    def __eq__(self, other):
        """vector comparison"""
        return self._coordinates==other._coordinates
    def __str__(self):
        """string representation 定义了类的外部表达形式"""
        return '<'+str(self._coordinates)[1:-1]+'>'
    def __trythis__(self):
        print('self:',self,',self._coordinates',self._coordinates)
        return self,self._coordinates
# %% R2.16 range() elements number
"""
n = max(0, (stop-start+step-1)//step)) ->((stop-1)-start)//step+1
arithmetic_sequence_terms = [(first-end)/step]+1
"""
# %% R2.18 get 8th of FibonacciProgression(2,2)
from dsap102_object_oriented_programming import FibonacciProgression
fib22=FibonacciProgression(2,2)
for i in range(8):t=fib22.__next__()
print(t)
# %% R2.22 sequence __eq__/R2.23 __lt__
from abc import ABCMeta,abstractmethod
class mySequence(ABCMeta):
    """ sequence abstract base class"""
    @abstractmethod
    def __len__(self):
        """Return the length of the sequence"""
    @abstractmethod
    def __getitem__(self, item):
        """Return the element at index <item> of the sequence"""
    def __contains__(self, item):
        """Return True if item in sequence; else False"""
        for i in range(len(self)):
            if self[i]==item:return True
        return False
    def index(self, item):
        """Return the index of first item in sequence, or raise ValueError"""
        for i in range(len(self)):
            if self[i]==item:return i
        raise ValueError('item not in sequence')
    def count(self, item):
        """Return the number of elements equal to item"""
        sumup=0
        for i in range(len(self)):
            if self[i]==item:sumup+=1
        return sumup
    def __eq__(self, other):
        """Return True if self==other, else False"""
        if len(self)==len(other):
            for i in range(len(self)):
                if self[i]!=other[i]:return False
            return True
        raise IndexError('sequence length unmatched')
    def __lt__(self, other):
        """Return True if self little than other"""
        for i in range(min(len(self),len(other))):
            if self[i]<other[i]:return True
            elif self[i]>other[i]:return False  # a strict prefix ot the other
        return len(self)<len(other)

# %% C2.26 ReversedSequenceIterator
class ReversedSequenceIterator:
    """iterator for any sequence type"""
    def __init__(self,sequence):
        """create a iterator for the given sequence"""
        self._seq=sequence
        self._k=len(self._seq)
    def __next__(self):
        self._k-=1
        if self._k>=0:
            return (self._seq[self._k])
        else:raise StopIteration()
    def __iter__(self):
        return self
# %% C2.28 XCreditCard(CreditCard): extend CreditCard Class/C2.29 least_payment
from dsap102_object_oriented_programming import CreditCard
class XCreditCard(CreditCard):
    """new features:1. deduct $5 when charge out of limit; 2.monthly interest(APR:AnnualPercentageRate)"""
    def __init__(self,customer,bank,account,limit,apr):
        super().__init__(customer,bank,account,limit)
        self._apr=apr
        self._charge_count=0
        self._payment_count=0
    def charge(self,price):
        self._charge_count+=1
        if self._charge_count>10:
            self._balance+=1
        success=super().charge(price)   # call inherited method
        if not success:
            self._balance+=5
        return success
    def make_payment(self,amount):
        super().make_payment(amount)
        self._payment_count+=amount
    def process_monthly(self):
        """assess monthly interest on outstanding balance"""
        if self._payment_count<10:  # at least 10 payment each month
            self._balance-=10-self._payment_count
        if self._balance>0:
            monthly_factor=(1+self._apr)**(1/12)    # assess monthly interest rate
            self._balance*=monthly_factor
# %% C2.31 differenceProgression
from dsap102_object_oriented_programming import Progression
class differenceProgression(Progression):
    """x2=|x1-x0|"""
    def __init__(self,first=2,second=200):
        super().__init__(first) # self._current=first
        self._prev=second-first
    def _advance(self):
        self._prev,self._current=self._current,abs(self._prev-self._current)
# %% C2.32 squareProgression
class squareProgression(Progression):
    """x2=x1**2"""
    def __init__(self,first=65536):
        super().__init__(first)
    def _advance(self):
        self._current*=self._current


# %% Test
a=list([1,2,3])
daisy=Flower()
daisy.get_name()
daisy.set_petal_number(13)
daisy.get_price()
import time
t0=time.time()
2 in range(10000000000)
t1=time.time()
99999999999999 in range(100000000000000)
t2=time.time()
print(t1-t0,'/',t2-t1)



