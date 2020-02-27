class Solution:
    def fibonacci(self, n, cache=dict()):
        if n in cache:
            return cache[n]
        if n in [0,1]:
            return 1
        else:
            ans = self.fibonacci(n-1) + self.fibonacci(n-2)
            cache[n] = ans
            return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.fibonacci(0))
    print(sol.fibonacci(1))
    print(sol.fibonacci(10))