from graph import Graph,Vertex
from queue import Queue
#first build a graph based on wordFile where connected words differ by at most 1 letter

def buildGraph(wordFile):
    d = {}
    g = Graph()
    wfile = open(wordFile,'r')
    # create buckets of words that differ by one letter
    for line in wfile:
        word = line[:-1]
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]
    # add vertices and edges for words in the same bucket
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1,word2)
    return g





def bfs(g,start,target=None):
   # start.setDistance(0)
    start.setPred(None)
    vertQueue = Queue()
    vertQueue.enqueue(start)
    while vertQueue.size() > 0:
        currentVert = vertQueue.dequeue()

        for nbr in currentVert.getConnections():
            # print('nbr=',nbr)
#             nbr = nbr
#             print('nbr = ',type(nbr))
            if (nbr.color) == 'white':
                # print(nbr.ID, '=?', target.ID)
                if nbr.ID == target.ID:
                    # print('matched= ', nbr.ID)
                    nbr.setPred(currentVert)
                    nbr.setDistance(nbr.getDistance() + 1)
                    return True
                nbr.setColor('gray')
                nbr.setDistance(nbr.getDistance() + 1)
                nbr.setPred(currentVert)
                vertQueue.enqueue(nbr)
        currentVert.setColor('black')



def traverse(v) :
    x = v
    print(x.ID)
    while x.getPred():
        # print(x.getID)
        x=x.getPred()
        print(x.ID)





