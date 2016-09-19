class State:
    edges = None
    h = None
    name = None
    def __init__(self, edges=None, h=None, name = None):
        self.edges = edges
        self.h = h
        self.name = name

    #Returns a tuple containing this structure: (connectingState, cost)
    def getEdges(self):
        return self.edges
    
    #Returns the heuristic value of this state
    def getH(self):
        return self.h

    def setEdges(self, edges):
        self.edges = edges

    def setName(self, name):
        self.name = name

    def getName():
        return name

def last(list):
    return list[len(list)-1]

def formatPath(path):
    names = map(lambda x:x.name,path)
    return ''.join(names)

#A* Search Algorithm, start = starting state, end = ending state, stateSpace = dict containing spacing keyed w/ names
def A(start, end, stateSpace):
    #Setup queue, expanded list, result, and lowest solution 
    #Queue is described by the following structure: ((tuple containing ordered path of states),f(lastState),currentPathLength)
    q = [([start],1,0)] #First item is initialized w/ f(start)=1, since no matter what it will always be picked
    expanded = []
    lowestSolution = float('inf')
    result = None
    while result == None:
        #Prune list of already expanded values, and values above the lowestSolution
        q = list(filter(lambda x: x[0][-1] not in expanded, q))
        q = list(filter(lambda x: x[1] <= lowestSolution, q))
        #Find and remove path w/ lowest f() value
        fValues = list(map(lambda x:x[1], q))
        toExpand = list(filter(lambda x:x[1]==min(fValues), q))[0]
        q.remove(toExpand)
        edges = toExpand[0][-1].getEdges()
        if toExpand[0][-1] == end:
            edges = []
        #Add node to the expanded list
        expanded.append(toExpand[0][-1])
        newPaths = []
        basePath = toExpand[0]
        #Iterate through expanded edges
        for i in edges:
            newEndNode = stateSpace[i[0]]
            newPathCost = toExpand[2] + i[1]
            f = newPathCost + newEndNode.getH()
            if f < lowestSolution and newEndNode not in expanded:
                #Are we at the target?
                if newEndNode == end:
                    lowestSolution = f
                newEntry = (basePath + [newEndNode], f, newPathCost)
                q.append(newEntry)
        if lowestSolution != float('inf') and len(q) == 0:
            return formatPath(toExpand[0])
    return result
        