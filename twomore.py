import sys

from search import seach
v = sys.argv
print(v)
seach(adress=' '.join(v[1:-1]), spn=v[-1])