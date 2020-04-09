cache = dict()
def getNthFib(n):

    if n in cache:
        return cache[n]
    if n==1:
        return 0
    if n==2:
        return 1

    ans = getNthFib(n-1) + getNthFib(n-2)
    cache[n] = ans
    return ans