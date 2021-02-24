"""
第7章 链表

"""

# %% R-7.1 找到单向链表倒数第二个节点
from dsap107_linkedList import LinkedStack
def penultimate_node(linked_list: LinkedStack):
    if len(linked_list) < 2:
        raise ValueError('Linked-List must have at least 2 elements')
    walk = linked_list._head
    while walk._next._next is not None:
        walk = walk._next
    return walk
# %% R-7.2 合并两个单向链表
def connect_2linkedLists(L: LinkedStack, M: LinkedStack):
    walk = L._head
    while walk._next is not None:
        walk = walk._next
    walk._next = M._head
    M._head = None  # 移除M链表的头节点
# %% R-7.3 计算单向链表节点数量-递归
def count_linkedNodes(node: LinkedStack._Node):
    if node is None:
        return 0
    else:
        return count_linkedNodes(node._next)+1
# %% R-7.4 交换节点
def exchange_2nodes(linked_list: LinkedStack, x: LinkedStack._Node,
                    y:LinkedStack._Node):
    walk = linked_list._head
    before_x, before_y = None, None
    while (before_x and before_y) is None:
        if walk._next == x:
            before_x = walk
        elif walk._next == y:
            before_y = walk
        walk = walk._next
    x._element, y._element = y._element, x._element
    x._next, y._next = y._next, x._next
    before_x._next, before_y._next = before_y._next, before_x._next
# %% R-7.5 统计循环链表节点个数
from dsap107_linkedList import CircularQueue
def count_circularNodes(circular_linked_list: CircularQueue):
    if circular_linked_list._tail is None:
        return 0
    walk = circular_linked_list._tail._next
    count = 1
    while walk != circular_linked_list._tail:
        count += 1
        walk = walk._next
    return count
# %% R-7.6 判断x和y是否来自同一个循环链表
def is_from_same_cll(x: CircularQueue._Node, y: CircularQueue._Node):
    walk = x._next
    while (walk != x) and (walk != y):
        if walk == y:
            return True
        elif walk == x:
            return False
        walk = walk._next
# %% R-7.7 不创建新节点的情况下,为LinkedQueue添加rotate()方法
from dsap107_linkedList import LinkedQueue
class LinkedQueue2(LinkedQueue):
    def rotate(self):
        if not self.is_empty():
            self._tail._next = self._head
            self._head = self._head._next
            self._tail = self._tail._next
            self._tail._next = None
# %% R-7.8 找双向链表中间节点
from dsap107_linkedList import _DoublyLinkedBase
def mid_node(db_linked: _DoublyLinkedBase):
    if db_linked._size == 0:
        raise ValueError('list is empty')
    backward_node = db_linked._header._next
    forward_node = db_linked._trailer._prev
    while backward_node != forward_node and backward_node._next != forward_node:
        backward_node = backward_node._next
        forward_node = forward_node._prev
    return backward_node
# %% R-7.9 已知头尾节点,合并2个双向链表
def connect_2dbLindedLists(L: _DoublyLinkedBase, M: _DoublyLinkedBase):
    L._trailer._prev._next, M._header._next._prev = M._header._next, L._trailer._prev
    L._trailer, M._header = None, None
# %% R-7.10 --
# %% R-7.11 返回位置列表中最大的元素
from dsap107_linkedList import PositionalList
def max_element_pList(pList: PositionalList):
    if len(pList) == 0:
        raise ValueError('list is empty')
    max_node = walk = pList.first()
    while walk is not None:
        if walk.element() > max_node.element():
            max_node = walk
        return max_node.element()
# %% R-7.12 --
# %% R-7.13 位置链表中加入find(e)方法,返回第一次出现在链表中元素e的位置
def find_element(pList: PositionalList, e):
    walk = pList._header._next
    while walk is not pList._trailer and walk._element != e:
        walk = walk._next
    if walk is pList.trailer:
        return None
    else:
        return pList.Position(pList, e)












