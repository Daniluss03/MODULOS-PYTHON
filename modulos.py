from collections import Counter
l=[1,2,3,4,1,2,3,1,2,1]
print(Counter(l))
p="palabra"
print(Counter(p))
animales="gato perro canario perro canario perro"
animales.split()
c=Counter(animales.split())
c=c.most_common(2)
print(c)

m=[10,20,30,40,10,20,30,10,20,10]
p=Counter(m)
p=p.items()
print(p)
#from collections import  defaultdict
# d=defaultdict(object)
n={}
n["uno"]='one'
n["dos"]="two"
n["tres"]='three'
print(n)
from collections  import OrderedDict
n= OrderedDict()
n["uno"]='one'
n["dos"]="two"
n["tres"]='three'
print(n)
