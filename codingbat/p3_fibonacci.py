def fibonacci(n, cache=dict()):
    if n in cache:
        return cache[n]
    if n in [0,1]:
        return 1
    else:
        ans = fibonacci(n-1) + fibonacci(n-2)
        cache[n] = ans
        return ans

if __name__ == "__main__":
    print(fibonacci(40))