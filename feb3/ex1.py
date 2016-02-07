from bb.perm import *

def composition(p, q):
    if len(p) != len(q):
        return False
    res = [0]*len(p)
    for i in range(len(p)):
        res[i] = p[q[i]]
    print(res)
    return res

def inverse(p):
    res = [0]*len(p)
    for i in range(len(p)):
        res[p[i]] = i
    return res

q = testPermutation(20)
print(q)
print()

p = [1, 2, 3, 0, 5, 4, 6, 7, 8, 9]
print(p)
printPermutation(p)
print(isTrivial(p))
print(p[0])
print(cycles(p))
print()

r = trivialPermutation(10)
print(r)
printPermutation(r)
print(r[0])
print(isTrivial(r))
print()

p = [1, 2, 3, 0, 5, 6, 4, 8, 7]
printPermutation(p)
q = composition(p, p)
printPermutation(q)
print()

print(inverse(p))
