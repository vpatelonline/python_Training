s=set()
s.add(1)
s.add(2)
print(s)
s.add(2)
print(s)
s.clear()
print(s)
s={1,2,3}
sc=s.copy()
print(sc)
s.add(4)
print(s)
print(sc)
print(s.difference(sc))

s1={1,2,3}
s2={1,5,6}
s1.difference_update(s2)
print(s1)
print(s2)
s2.discard(5)
print(s2)
s3={1,2,6}
s4={1,2,4,6,7}
print(s4.issuperset(s3))
s5=s3.intersection(s4)
print(s5)
print(s3)
print(s4)
s3.intersection_update(s4)
print(s3)
print(s3.isdisjoint(s4))
print(s3.symmetric_difference(s4))
print(s3.union(s4)) 
s3.update(s4)
print(s3)

