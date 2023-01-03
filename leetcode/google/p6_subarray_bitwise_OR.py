class Solution:
    def subarrayBitwiseORs(self, A):
        # Tabulation is a list of sets, one for each number in A. 
        # Each set, at position i, is initialised to containing the element at A[i]
        tabulation = [set([A[i]]) for i in range(len(A))]
        print('tabulation = ', tabulation)
        
        # And now we need to go through, updating the sets based on the previous set.
        for i in range(1, len(A)):
            for previous_result in tabulation[i - 1]:
                tabulation[i].add(A[i] | previous_result)
                print(f'previous_result = {A[i]}, OR = {A[i] | previous_result}, tabulation[{i}] = {tabulation[i]}')
        
        # Return the number of unique numbers in the tabulation list.
        return len(set.union(*tabulation)) if len(A) > 0 else 0

if __name__ == "__main__":
    sol = Solution()
    print(sol.subarrayBitwiseORs([4, 5, 10, 2, 16, 4, 5, 2, 1, 3]))