#A program implementing sets

a={1,2,3,4,5,6,7,8,9,10}
b={6,7,8,9,10,11,12,13,14,15}

print(a.union(b))
print(b.union(a))

print(a.intersection(b))
print(b.intersection(a))

print(a.difference(b))
print(b.difference(a))

print(a.symmetric_difference(b))
print(b.symmetric_difference(a))