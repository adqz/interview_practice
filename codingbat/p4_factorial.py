class Solution:
    def factorial(self, x):
        if x > 0:
            return x * self.factorial(x-1)
        else:
            return 1

if __name__ == "__main__":
    sol = Solution()
    print(sol.factorial(1))
    print(sol.factorial(2))
    print(sol.factorial(3))
    print(sol.factorial(10))