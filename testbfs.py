from graph import Graph,Vertex
from bfs import buildGraph,bfs,traverse
from queue import Queue

#s=g.getVertex(0)
#bfs(g,s)


wg = buildGraph("fourletterwords.txt")

print (wg.numVertices)

s=wg.getVertex('FOOL')
t=wg.getVertex('SAGE')
bfs(wg,s,target=t)
print('traverse********************************************')
traverse(t)
#test
