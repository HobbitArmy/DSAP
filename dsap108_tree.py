"""
第8章 树

"""
# %% 8-1 树的抽象基类
class Tree:
    """ Abstract base class representing a tree structure"""
    # ------nested Position class
    class Position:
        def element(self):
            """ return the element stored at this position"""
            raise NotImplemented('please implement in subclass')
        def __eq__(self, other):
            """ return True if other-Position represents the same location"""
            raise NotImplemented('please implement in subclass')
        def __ne__(self, other):
            """ return True if not represents the same"""
            raise NotImplemented('please implement in subclass')
    # ------abstract methods
    def root(self):
        """ return Position representing the tree's root """
        raise NotImplemented('please implement in subclass')
    def parent(self, p):
        """ return Position representing p's parent """
        raise NotImplemented('please implement in subclass')
    def num_children(self, p):
        """ return the number of children that position p has"""
        raise NotImplemented('please implement in subclass')
    def children(self, p):
        """ genrate an iteration of Positions representing p's children"""
        raise NotImplemented('please implement in subclass')
    def __len__(self):
        """ return total number of elements in the tree"""
        raise NotImplemented('please implement in subclass')
    # ------concrete methods
    def is_root(self, p):
        return self.root() == p
    def is_leaf(self, p):
        return self.num_children(p) == 0
    def is_empty(self):
        return len(self) == 0
    def depth(self, p):
        """ return the number of levels separating Position p from the root """
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))
    def _height(self, p):
        """ return the height of the subtree rooted at Position p"""
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height(i) for i in self.children(p))
    def height(self, p=None):
        if p == None:
            p = self.root()
        return self._height(p)
# 扩展BinaryTree抽象基类
class BinaryTree(Tree):
    """ 二叉树抽象基类"""
    def left(self, p):
        """ Return left child or None"""
        raise NotImplemented('please implement in subclass')
    def right(self, p):
        """ Return right child pr None"""
        raise NotImplemented('please implement in subclass')
    def sibling(self, p):
        """ Return p's sibling or None"""
        parent = self.parent(p)
        if parent is None:
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)
    def children(self, p):
        """ Generate an iteration of p's children's Positions"""
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)










