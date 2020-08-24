from polyfamily_tree import *


class A(FamilyMember):
    def __init__(self, id):
        super().__init__()
        self._id = id

    def __str__(self):
        return f"<{self._id}>"

    def __repr__(self):
        return str(self)

a, b, c = A('a'), A('b'), A('c')

# build linear relationship
a.fm_append_member(a, b)
b.fm_append_member(b, c)
# checking graph
print(a.fm_get_children())
print(b.fm_get_children())
print(c.fm_get_children())
print()
print(c.fm_get_parents())
print(b.fm_get_parents())
print(a.fm_get_parents())
print()
# getitem
print(a.fm_get_child(0), b.fm_get_parent(0))
# removing relationship
b.fm_remove_relationship(b, a)
print(a.fm_get_children(), b.fm_get_parents())
