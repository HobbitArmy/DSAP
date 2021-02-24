"""
第七章 链表

"""
# %% 7-5~7-6 单向链表实现栈
from dsap106_stack_queue import Empty
class LinkedStack:
    """ LIFO Stack implementation using linked lists for storage"""
    # ------ Nested Linked._Node class------
    class _Node:
        """ Lightweight, private class for storing a singly linked node """
        __slots__ = '_element', '_next'  # streamline memory usage
        def __init__(self, element, next_element):
            """ initialize node's field"""
            self._element = element     # reference to the element
            self._next = next_element   # reference to next node
    # ------ Stack method------
    def __init__(self):
        """ Create an empty stack"""
        self._head = None
        self._size = 0
    def __len__(self):
        """ Return the number of elements in stack"""
        return self._size
    def is_empty(self):
        """ Return True if the stack is empty"""
        return self._size == 0
    def push(self, e):
        """ Add element e to the top of the stack"""
        self._head = self._Node(e, self._head)
        self._size += 1
    def top(self):
        """ Return but not remove the element at the top of the stack"""
        if self.is_empty():
            raise Empty('Stack if empty')
        return self._head._element
    def pop(self):
        """ Remove and return the element at the top of the stack"""
        if self.is_empty():
            raise Empty('Stack if empty')
        pop_value = self._head._element
        self._head = self._head._next
        self._size -= 1
        return pop_value
# %% 7-7~7-8 单向链表实现队列
class LinkedQueue(LinkedStack):
    """ FIFO queue implementation using linked-lists for storage"""
    def __init__(self):
        super().__init__()
        self._tail=None
    def pop(self):
        """ don't use this method in Queue"""
        pass
    def push(self, e):
        """ don't use this method in Queue"""
        pass
    def dequeue(self):
        """ Remove and return the first element of the queue"""
        if self.is_empty():
            raise Empty('Stack if empty')
        first_value = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return first_value
    def enqueue(self,e):
        """ Add an element to the back of the queue"""
        new_element = self._Node(e,None)
        if self.is_empty():
            self._head = new_element
        else:
            self._tail._next = new_element
        self._tail = new_element
        self._size += 1
# %% 7-9~7-10 循环链表实现队列
class CircularQueue:
    """ Queue implementation using circular-linked-list for storage"""
    # ------ Nested Linked._Node class------
    class _Node:
        """ Lightweight, private class for storing a singly linked node """
        __slots__ = '_element', '_next'  # streamline memory usage
        def __init__(self, element, next_element):
            """ initialize node's field"""
            self._element = element     # reference to the element
            self._next = next_element   # reference to next node
    # ------ Stack method------
    def __init__(self):
        """ Create an empty queue"""
        self._tail = None
        self._size = 0
    def __len__(self):
        """ Return the number of elements in the queue"""
        return self._size
    def is_empty(self):
        """ Return True if the queue is empty"""
        return self._size == 0
    def first(self):
        """ Return but not remove the first element at the queue"""
        if self.is_empty():
            raise Empty('Queue is empty')
        head = self._tail._next
        return head._element
    def dequeue(self):
        """ Remove and return the first element at the queue"""
        if self.is_empty():
            raise Empty('Queue is empty')
        head = self._tail._next
        if self._size == 1:
            self._tail = None
        else:
            self._tail._next = head._next
        self._size -= 1
        return head._element
    def enqueue(self, e):
        """ Add element-e to the end of the queue"""
        new_element = self._Node(e, None)
        if self.is_empty():
            new_element._next = new_element
        else:
            new_element._next = self._tail._next
            self._tail._next = new_element
        self._tail = new_element
        self._size += 1
    def rotate(self):
        """ Rotate the first element to the end of the queue"""
        if not self.is_empty():
            self._tail = self._tail._next
# %% 7-11~7-12 双向链表基类的实现
class _DoublyLinkedBase:
    """ A base class providing a doubly-linked-list representation """
    class _Node:
        """ Lightweight, private class for storing a doubly-linked-node"""
        __slots__ = '_element', '_prev', '_next'
        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next
    def __init__(self):
        """ Create an empty doubly-linked-list"""
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0
    def __len__(self):
        return self._size
    def is_empty(self):
        return self._size == 0
    def _insert_between(self, e, predecessor: _Node, successor: _Node):
        """ Add an element between 2 existing nodes and return this new node"""
        new_node = self._Node(e, predecessor, successor)
        predecessor._next = new_node
        successor._prev = new_node
        self._size += 1
        return new_node
    def _delete_node(self, node: _Node):
        """ Delete non-sentinel node from DL-list and return element of this node"""
        predecessor = node._prev
        successor = node._next
        predecessor._next, successor._prev = successor, predecessor
        self._size -= 1
        node_element = node._element
        node._prev = node._next = node._element =None
        return node_element
# %% 7-13 由双向链表基类 实现 链式双端队列
class LinkedDeque(_DoublyLinkedBase):
    """ Double-ended queue implementation based on a doubly linked list"""
    def first(self):
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._header._next._element
    def last(self):
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._trailer._prev._element
    def insert_first(self, e):
        self._insert_between(e, self._header, self._header._next)
    def insert_last(self, e):
        self._insert_between(e, self._trailer._prev, self._trailer)
    def delete_first(self):
        if self.is_empty():
            raise Empty(' Deque is empty')
        return self._delete_node(self._header._next)
    def delete_last(self):
        if self.is_empty():
            raise Empty(' Deque is empty')
        return self._delete_node(self._trailer._prev)
# %% 7-14~7-16 基于双向链表的 位置列表类 PositionalList
class PositionalList(_DoublyLinkedBase):
    """ A sequential container of elements allowing Positional access"""
    # ------ nested Position class
    class Position:
        """ an abstraction representing the location of a single element"""
        def __init__(self, container, node):
            self._container = container
            self._node = node
        def element(self):
            return self._node._element
        def __eq__(self, other):
            """ return True if a Position representing the same location"""
            return type(other) is type(self) and other._node is self._node
        def __ne__(self, other):
            """ return True if not the same location"""
            return not(self == other)
    # ------ utility method 实用方法
    def _validate(self, p: Position):
        """ return Position's node, or raise appropriate error if valid
        位置p转换为节点node"""
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._next is None:
            raise ValueError('p is not valid')
        return p._node
    def _make_Position(self, node):
        """ return Position instance for given node(non-sentinel)
        节点node转换为位置p"""
        if node is self._header or node is self._trailer:
            return None
        else:
            return self.Position(self, node)
    # ------ accessors  访问器
    def first(self):
        return self._make_Position(self._header._next)
    def last(self):
        return self._make_Position(self._trailer._prev)
    def before(self, p):
        """ return the Position before p"""
        node_p = self._validate(p)
        return self._make_Position(node_p._prev)
    def after(self, p):
        """ return the Position after p"""
        node_p = self._validate(p)
        return self._make_Position(node_p._next)
    def __iter__(self):
        """ generate a forward iteration of the elements of the list"""
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)
    # ------ mutators   更新方法
    def _insert_between(self, e, predecessor, successor):
        """ overwrite to return Position, rather than Node"""
        node_e = super()._insert_between(e, predecessor, successor)
        return self._make_Position(node_e)
    def add_first(self, e):
        return self._insert_between(e, self._header, self._header._next)
    def add_last(self, e):
        return self._insert_between(e, self._trailer._prev, self._trailer)
    def add_before(self, p, e):
        """ insert element e into list before Position p and return new Position"""
        node_p = self._validate(p)
        return self._insert_between(e, node_p._prev, node_p)
    def add_after(self, p, e):
        node_p = self._validate(p)
        return self._insert_between(e, node_p, node_p._next)
    def delete(self, p):
        """ remove and return the element at Position p"""
        node_p = self._validate(p)
        return self._delete_node(node_p)
    def replace(self, p, e):
        """ replace the element at Position p with e
        return the element at p formerly"""
        node_p = self._validate(p)
        node_p_value = node_p._element
        node_p._element = e
        return node_p_value
# %% 7-17 基于位置列表的 插入排序算法
def insertion_sort(L: PositionalList):
    """ sort PositionalList of comparable elements into non-decreasing order 表头最小,递增"""
    if len(L)>1:
        marker = L.first()
        while marker != L.last():
            pivot = L.after(marker)
            pivot_value = pivot.element()
            if pivot_value > marker.element():  # 满足递增
                marker = pivot
            else:   # 不满足递增
                walk = marker   # 新元素的插入位置
                while walk != L.first() and L.before(walk).element() > pivot_value:
                    walk = L.before(walk)
                L.delete(pivot)
                L.add_before(walk, pivot_value)
# %% 7-18 用位置列表维护收藏夹-访问次数
class FavoritesList:
    """ 按照访问次数降序排列存储收藏夹元素"""
    # ------nested _item class
    class _item:
        __slots__ = '_value', '_count'
        def __init__(self, e):
            self._value = e
            self._count = 0
    # ------nonpublic utilities
    def _find_position(self, e):
        """ find position of e"""
        walk = self._data.first()
        while walk is not None and walk.element()._value != e:
            walk = self._data.after(walk)
        return walk
    def _move_up(self, p):
        """ move item at position p to front based on access count"""
        if p != self._data.first():
            cnt = p.element()._count
            walk = self._data.before(p)
            if cnt > walk.element()._count:
                while (walk!=self._data.first() and cnt>self._data.before(walk).element()._count):
                    walk = self._data.before(walk)
                self._data.add_before(walk, self._data.delete(p))
    # ------public methods
    def __init__(self):
        """ create an empty list of favorites"""
        self._data = PositionalList()
    def __len__(self):
        return len(self._data)
    def is_empty(self):
        return len(self._data) == 0
    def access(self, e):
        """ access element e, and increase its access count"""
        p = self._find_position(e)
        if p is None:
            p = self._data.add_last(self._item(e))  # if new, place it at end
            p.element()._count += 1
            self._move_up(p)
    def remove(self, e):
        p = self._find_position(e)
        if p is not None:
            self._data.delete(p)
    def top_n(self, n):
        if not 1 <= n <= len(self):
            raise ValueError('illegal value for n')
        walk = self._data.first()
        for i in range(n):
            item = walk.element()
            yield item._value       # yield 的作用就是把一个函数变成一个 generator
            walk = self._data.after(walk)
class FavoritesListMTF(FavoritesList):
    """ 使用Move-to-Front启发式算法排列记录收藏夹中元素"""
    def _move_up(self, p):
        if p!= self._data.first():
            self._data.add_first(self._data.delete(p))
    def top_n(self, n):
        if not 1 <= n <= len(self):
            raise ValueError('illegal value for n')
        # copy original list
        temp = PositionalList()
        for item in self._data:
            temp.add_last(item)
        # find largest n element, and remove it from temp
        for i in range(n):
            high_position = temp.first()
            walk = temp.after(high_position)
            while walk is not None:
                if walk.element()._count > high_position.element()._count:
                    high_position = walk
                walk = temp.after(walk)
            yield high_position.element()._value
            temp.delete(high_position)










