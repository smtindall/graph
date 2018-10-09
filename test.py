from graph import Graph,Vertex

g=Graph()

for i in range(6):
    g.addVertex(i)

print(g.vertList)
# {0: <graph.Vertex object at 0x000001F790B8EEF0>,
# 1: <graph.Vertex object at 0x000001F790B913C8>,
# 2: <graph.Vertex object at 0x000001F790B91BE0>,
# 3: <graph.Vertex object at 0x000001F790B91C18>,
# 4: <graph.Vertex object at 0x000001F790B91C50>,
# 5: <graph.Vertex object at 0x000001F790B91C88>}

g.addEdge(0,1,5)
g.addEdge(0,5,2)
g.addEdge(1,2,4)
g.addEdge(2,3,9)
g.addEdge(3,4,7)
g.addEdge(3,5,3)
g.addEdge(4,0,1)
g.addEdge(5,4,8)
g.addEdge(5,2,1)

for v in g:
    for w in v.getConnections():
        print("(%s, %s)" % (v.getID(),w.getID()))

# (0, 1)
# (0, 5)
# (1, 2)
# (2, 3)
# (3, 4)
# (3, 5)
# (4, 0)
# (5, 4)
# (5, 2)



