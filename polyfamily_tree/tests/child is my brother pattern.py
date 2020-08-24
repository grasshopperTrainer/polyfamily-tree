from polyfamily_tree import *


class A(FamilyMember):
    def __init__(self, id):
        super().__init__()
        self._id = id

    def __str__(self):
        return f"<{self.__class__.__name__}:{self._id}>"

    def __repr__(self):
        return str(self)

a, b, c, d = A('a'), A('b'), A('c'), A('d')

# build linear relationship
a.fm_append_member(a, b)
a.fm_append_member(a, c)
b.fm_append_member(b, c)
d.fm_append_member(b, d)

print(a.fm_get_children(), c.fm_get_parents())
print()
# iter parent
print(list(PreorderIterator(ParentIterator(c))))
print(list(PostorderIterator(ParentIterator(c))))
# iter child
print()
print(list(PreorderIterator(ChildrenIterator(a))))
print(list(PostorderIterator(ChildrenIterator(a))))