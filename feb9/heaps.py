"""
Jan-Willem Nijhuis
s1594575
9 Feb 2016
"""

def parent(i):
    return (i - 1) // 2


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def min_parent(E):
    return len(E) // 2


def ext_heapify(E, i, elem):
    E[i] = elem
    while i > 0 and E[parent(i)] < E[i]:
        print("switching with parent")
        E[i], E[parent(i)] = E[parent(i)], E[i]
        i = parent(i)
    while i <= min_parent(E) and (E[left(i)] > E[i] or E[right(i)] > E[i]):
        print("switching with child")
        if E[left(i)] >= E[right(i)]:
            largest = left(i)
        else:
            largest = right(i)
        E[i], E[largest] = E[largest], E[i]
        i = largest


heap = [100, 19, 36, 17, 3, 25, 1, 2, 7]
print(heap)
ext_heapify(heap, 4, 20)
print(heap)
ext_heapify(heap, 0, 3)
print(heap)
ext_heapify(heap, 3, 5)
print(heap)
ext_heapify(heap, 8, 2)
print(heap)
