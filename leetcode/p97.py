from typing import List
from collections import Counter

import heapq

class MaxHeapObj(object):
    def __init__(self,val): self.val = val
    def __lt__(self,other): return self.val > other.val
    def __eq__(self,other): return self.val == other.val
    def __str__(self): return str(self.val)

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        done = False
        pending_tasks = Counter(tasks)
        task_wait_time = dict()
        cpu_intervals = 0
        task_order = []

        print(task_order)
        return cpu_intervals
    
    def all_tasks_done(self, pending_tasks):
        if sum(pending_tasks.values()) == 0:
            return True
        else:
            return False

if __name__ == "__main__":
    sol = Solution()
    print(sol.leastInterval(["A","A","A","B","B","B"], 2))


'''
# Solution 1: Not working
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        done = False
        pending_tasks = Counter(tasks)
        task_wait_time = dict()
        cpu_intervals = 0
        task_order = []

        while not(done):
            task_executed = False
            if self.all_tasks_done(pending_tasks):
                done = True
                break

            for task, num_pending in pending_tasks.items():
                
                if num_pending == 0:
                    continue
                
                if task not in task_wait_time:
                    pending_tasks[task] -= 1
                    task_order.append(task)
                    task_executed = True
                    task_wait_time[task] = n
                    continue
                    
                elif task_wait_time[task] <= 0:
                    del task_wait_time[task]
                    pending_tasks[task] -= 1
                    task_order.append(task)
                    task_executed = True
                    task_wait_time[task] = n
                    continue
                
            for task in task_wait_time:
                task_wait_time[task] -= 1
            
            print(task_wait_time)
            
            if not task_executed:
                task_order.append('idle')
            
            cpu_intervals += 1
        print(task_order)
        return cpu_intervals
    
    def all_tasks_done(self, pending_tasks):
        if sum(pending_tasks.values()) == 0:
            return True
        else:
            return False
    
    def reduce_wait_of_all_tasks(self, task_wait_time):
        return {k: v-1 for k,v in task_wait_time.items()}
'''