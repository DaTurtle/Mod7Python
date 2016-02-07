def multiples(max):
    sum = 0
    for x in range(0, max):
        if x % 3 == 0 or x % 5 == 0:
            sum += x
            print("%d : %d" % (x, sum))
    return sum

print(multiples(1000))


