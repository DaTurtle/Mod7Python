def gcd(a, b):
    a = abs(a)
    b = abs(b)
    if a == 0 or b == 0:
        return 1
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


def frac(a, b):
    if b == 0:
        return 0, 0
    if a == 0:
        return 0, 1
    div = gcd(a, b)
    return a // div, b // div


def extended_gcd(a, b):
    a = abs(a)
    b = abs(b)
    s, old_s = 0, 1
    t, old_t = 1, 0
    r, old_r = b, a
    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t
    print("Bezout coefficients: %d, %d" % (old_s, old_t))
    print("Greatest common divisor: %d" % old_r)
    print("Quotients by the gcd: %d, %d" % (t, s))
    return old_r


def encode(num):
    if num < 10:
        return num
    else:
        return chr(ord('a') + num-10)


def toK(n, k):
    if k < 2 or k > 35:
        return 'error'
    res = ""
    remainder = n
    for x in range(12, 0):
        shifted = remainder >> x
        if shifted > k:
            res += str(encode(shifted // k))
            remainder -= shifted // k
    return res

print(gcd(3141, 156))
print(gcd(12345678, 987654321))
print(extended_gcd(3141, 156))
print(frac(16, 4))
print(frac(-21, -7))
print(frac(-33, 3))
print(encode(0))
print(encode(8))
print(encode(35))
print(toK(100, 10))
print(toK(4321, 16))
