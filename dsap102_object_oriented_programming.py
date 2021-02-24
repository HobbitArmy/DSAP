"""
第二章 面向对象编程

"""
# %% 2.3.1 CreditCard
class CreditCard:
    def __init__(self,customer,bank,account,limit):
        self._customer=customer     # _variable AKA nonpublic
        self._bank=bank
        self._account=account
        self._limit=limit
        self._balance=0
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
    def charge(self,price):
        """Charge given to the card, Return True if charge processed, else False"""
        if price+self._balance>self._limit:
            return False
        else:
            self._balance+=price
            return True
    def make_payment(self,amount):
        """Reduce amount from balance"""
        self._balance-=amount

# %% 2.3.3 n-D-VectorClass
class Vector2:
    """Multi-d vector representation"""
    def __init__(self,d):
        """create a d-D vector"""
        self._coordinates=[0]*d
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
    def __eq__(self, other):
        """vector comparison"""
        return self._coordinates==other._coordinates
    def __str__(self):
        """string representation 定义了类的外部表达形式"""
        return '<'+str(self._coordinates)[1:-1]+'>'
    def __trythis__(self):
        print('self:',self,',self._coordinates',self._coordinates)
        return self,self._coordinates

# %% IteratorClass
class SequenceIterator:
    """iterator for any sequence type"""
    def __init__(self,sequence):
        """create a iterator for the given sequence"""
        self._seq=sequence
        self._k=-1
    def __next__(self):
        self._k+=1
        if self._k<len(self._seq):
            return (self._seq[self._k])
        else:
            raise StopIteration()
    def __iter__(self):
        return self

# %% RangeClass
class myRange:
    def __init__(self,start,stop=None,step=1):
        if step==0:
            raise ValueError('step must be non-zero value')
        if stop is None:
            start,stop=0,start  # Simultaneous distribution
        self._length=max(0,1+(stop-start-1)//step)
        #   calculate effective length
        self._start=start; self._step=step
    def __len__(self):
        return self._length
    def __getitem__(self, item):
        """return self[item] """
        if item<0:
            item+=len(self)
        if not 0<=item<self._length:
            raise IndexError('index out of range')
        return self._start+item*self._step

# %% XCreditCard(CreditCard): extend CreditCard Class
class XCreditCard(CreditCard):
    """new features:1. deduct $5 when charge out of limit; 2.monthly interest(APR:AnnualPercentageRate)"""
    def __init__(self,customer,bank,account,limit,apr):
        super().__init__(customer,bank,account,limit)
        self._apr=apr
    def charge(self,price):
        success=super().charge(price)   # call inherited method
        if not success:
            self._balance+=5
        return success
    def process_monthly(self):
        """assess monthly interest on outstanding balance"""
        if self._balance>0:
            monthly_factor=(1+self._apr)**(1/12)    # assess monthly interest rate
            self._balance*=monthly_factor

# %%  BasicProgression Iterator
class Progression:
    """iterator producing a generic progression
            default produces the whole natural-number"""
    def __init__(self,start=0):
        self._current=start
    def _advance(self):
        """update self._current
            this should be override by subclass to customize
            'None' designating the end"""
        self._current+=1
    def __next__(self):
        if self._current is None:
            raise StopIteration()
        else:
            next_value=self._current
            self._advance()
            return next_value
    def __iter__(self):
        """by convention, an iterator must return itself as an iterator"""
        return self
    def printProgression(self,n):
        """print next n values of the progression"""
        print(' '.join(str(next(self)) for _ in range(n)))
        # str.join(sequence) -> connect element in sequence by str

#%% ArithmeticProgression
class ArithmeticProgression(Progression):
    """iterator producing an arithmetic progression"""
    def __init__(self,increment=1,start=0):
        super().__init__(start)
        self._increment=increment
    def _advance(self):
        self._current+=self._increment
class GeometricProgression(Progression):
    """iterator producing an geometric progression"""
    def __init__(self,base,start=1):
        super().__init__(start)
        self._base=base
    def _advance(self):
        self._current*=self._base
class FibonacciProgression(Progression):
    """iterator producing a Fibonacci progression"""
    def __init__(self,first=0,second=1):
        super().__init__(first)     # -> self._current=first
        self._prev=second-first
    def _advance(self):
        self._prev,self._current=self._current,self._prev+self._current

# %% mySequence
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


# %% Test Code
if __name__=='__main__':
    wallet=[]
    wallet.append(CreditCard('Alice', 'ICBC','0001',5000))
    wallet.append(CreditCard('Bob','ABC','0002',4000))
    wallet.append((CreditCard('David','BOC','0003',6000)))
    for i in range(3):
        wallet[i].charge(200*(i+2))
        print(wallet[i].get_balance())
    v1=Vector2(4); v2=Vector2(4)
    v1+=[2,3,4,5]; print('v1:',v1)
    print('v2!=v1 ',v2!=v1)
    FibP=FibonacciProgression(0,1)
    print('Fibonacci Progression:',FibP.printProgression(10))

