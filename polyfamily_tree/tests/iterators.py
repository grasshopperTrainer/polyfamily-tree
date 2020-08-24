from polyfamily_tree import *


class A(FamilyMember):
    def __init__(self, id):
        super().__init__()
        self._id = id

    def __str__(self):
        return f"<{self.__class__.__name__}:{self._id}>"

    def __repr__(self):
        return str(self)


class B(A):
    pass


a, b, c, d, e = A('a'), A('b'), B('c'), A('d'), B('e')

# build linear relationship
a.fm_append_member(a, b)
d.fm_append_member(b, d)
e.fm_append_member(d, e)
a.fm_append_member(a, c)
b.fm_append_member(b, c)
# iter type filter
print(list(TypeFilterIterator(PreorderIterator(ChildrenIterator(a)), B)))
# iter first degree
print(list(FirstDegreeIterator(c)))
# iter first degree type filter
print(list(TypeFilterIterator(FirstDegreeIterator(c), A)))
# iter first degree type filter without subclassing(?)
print(list(TypeFilterIterator(FirstDegreeIterator(c), A, is_subclass_valid=False)))