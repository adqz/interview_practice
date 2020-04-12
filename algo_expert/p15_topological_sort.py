# O(j+d) time | O(j+d) space, where j and d are number of jobs and dependencies.
def topologicalSort(jobs, deps):
    jobGraph = createJobGraph(jobs, deps)
    return getTopologicalOrder(jobGraph)

def createJobGraph(jobs, deps):
    jobGraph = JobGraph(jobs)
    for prereq, job in deps:
        jobGraph.addPreReq(job, prereq)
    return jobGraph

def getTopologicalOrder(jobGraph):
    topologicalOrder = []
    for node in jobGraph.nodes:
        # print(node.name)
        # print(node.prereqs)
        containsCycle = dfs(node, topologicalOrder)
        if containsCycle:
            return []
    
    return topologicalOrder

def dfs(node, topologicalOrder):
    if node.visited:
        return False
    if node.visiting:
        return True
    node.visiting = True
    for prereqNode in node.prereqs:
        containsCycle = dfs(prereqNode, topologicalOrder)
        if containsCycle:
            return False
    
    node.visiting = False
    node.visited = True
    topologicalOrder.append(node.name)

    return False


class JobGraph:
    def __init__(self, jobs):
        self.nodes = []
        self.graph = dict()
        for job in jobs:
            self.addNode(job)
    
    def addNode(self, job):
        jobNode = JobNode(job)
        self.nodes.append(jobNode)
        self.graph[job] = jobNode
    
    def getNode(self, job):
        if job not in self.graph:
            self.addNode(job)
        
        return self.graph[job]
    
    def addPreReq(self, job, prereq):
        jobNode = self.getNode(job)
        prereqNode = self.getNode(prereq)
        jobNode.prereqs.append(prereqNode)

class JobNode:
    def __init__(self, name):
        self.name = name
        self.prereqs = []
        self.visited = False
        self.visiting = False
    
if __name__ == "__main__":
    jobs = [1,2,3,4]
    deps = [[1,2], [1,3], [3,2], [4,2], [4,3]]
    print(topologicalSort(jobs, deps)) #[1,4,3,2] or [4,1,3,2]