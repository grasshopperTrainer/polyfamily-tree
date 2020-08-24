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
# loop error
try:
    c.fm_append_member(c, a)
except Exception as e:
    print(e)
# index error
try:
    print(a.fm_get_child(1))
except Exception as e:
    print(e)