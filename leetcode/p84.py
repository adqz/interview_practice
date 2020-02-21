'''
@author: adnan
Problem 274. H-Index (Medium)

'''
from typing import List
from collections import Counter
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0
        if len(citations) == 1:
            return 0
        orig_N = len(citations)
        citations_counter = Counter(citations)
        citations = list(set(citations))
        N = len(citations)
        at_least = dict()
        no_more_than = dict()

        temp_count = 0
        for i, num_cites in enumerate(citations):
            at_least[num_cites] = citations_counter[num_cites] + (N-(i+1))
            no_more_than[num_cites] = temp_count
            temp_count += citations_counter[num_cites]
        
        max_h = float('-inf')
        for h in at_least.keys():
            num_papers_with_at_least_h_citations = at_least[h]
            num_papers_with_no_more_than_h_citations = no_more_than[h]
            if h == num_papers_with_at_least_h_citations:
                if num_papers_with_at_least_h_citations + num_papers_with_no_more_than_h_citations == orig_N:
                    if h > max_h:
                        max_h = h
        return max_h

if __name__ == "__main__":
    sol = Solution()
    print(sol.hIndex([3,0,6,1,5])) #3