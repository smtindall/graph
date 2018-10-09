class Vertex:
    def __init__(self,key):
        self.ID = key
        self.connectedTo = {}
        self.predecessor = None
        self.color = 'white'
        self.distance = 0

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.ID) +  'connected to' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getID(self):
        return self.ID

    def getWeight(self,nbr):
        return self.connectedTo[nbr]

    def getDistance(self):
        return self.distance

    def setDistance(self,d):
        self.distance = d

    def setPred(self,v):
        self.predecessor = v

    def getPred(self):
        return self.predecessor

    def getColor(self):
        return self.color

    def setColor(self,color):
        self.color = color

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices += 1
        newVertex=Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertList

    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
            _ = self.addVertex(f)
        if t not in self.vertList:
            _ = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t],cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())



    def getConnections(self):
        return self.vertList



