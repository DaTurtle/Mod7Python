from graphIO import loadgraph, writeDOT  # graphIO imports basicgraphs.py, so we do not need to import it here.
# Use these options to change the tests:

TestBellmanFordDirected = True
TestBellmanFordUndirected = False
TestDijkstraDirected = True
TestDijkstraUndirected = False
TestKruskal = False

WriteDOTFiles = False

# Use these options to select the graphs to test your algorithms on:
# TestInstances = ["weightedexample.gr"]
# TestInstances=["randomplanar.gr"]
# TestInstances=["negativeweightexample.gr"]
# TestInstances=["negativeweightcycleexample.gr"]
# TestInstances=["WDE100.gr","WDE200.gr","WDE400.gr","WDE800.gr","WDE2000.gr"]; WriteDOTFiles=False
# TestInstances=["bbf2000.gr"]
TestInstances=["graph1.gr", "graph2.gr", "graph3.gr", "graph4.gr", "graph5.gr", "graph6.gr", "graph7.gr"]

# If you have implemented a module fastgraphs.py (compatible with basicgraphs.py),
# you can set this option to True:
UseFastGraphs = False


def BellmanFordUndirected(G, start):
    """
    Arguments: <G> is a graph object, where edges have integer <weight>
        attributes,	and <start> is a vertex of <G>.
    Action: Uses the Bellman-Ford algorithm to compute all vertex distances
        from <start> in <G>, and assigns these values to the vertex attribute <dist>.
        Optional: assigns the vertex attribute <indedge> to be the incoming
        shortest path edge, for every reachable vertex except <start>.
        <G> is viewed as an undirected graph.
    """
    # Initialize the vertex attributes:
    for v in G.V():
        v.dist = None
        v.inedge = None
    start.dist = 0

# Insert your code here.


def BellmanFordDirected(G, start):
    """
    Arguments: <G> is a graph object, where edges have integer <weight>
        attributes,	and <start> is a vertex of <G>.
    Action: Uses the Bellman-Ford algorithm to compute all vertex distances
        from <start> in <G>, and assigns these values to the vertex attribute <dist>.
        Optional: assigns the vertex attribute <indedge> to be the incoming
        shortest path edge, for every reachable vertex except <start>.
        <G> is viewed as a directed graph.
    """
    for v in G.V():
        v.dist = None
        v.inedge = None
    start.dist = 0

    # Insert your code here.
    for i in range(1, len(G.V())-1):
        for edge in G.E():
            if edge.tail().dist is not None:
                if (not edge.head().dist) or edge.tail().dist + edge.weight < edge.head().dist:
                    edge.head().dist = edge.tail().dist + edge.weight
                    edge.head().inedge = edge.tail()

    for edge in G.E():
        if edge.weight < 0:
            print("negative edge")

    return G, start


def DijkstraUndirected(G, start):
    """
    Arguments: <G> is a graph object, where edges have integer <weight>
        attributes,	and <start> is a vertex of <G>.
    Action: Uses Dijkstra's algorithm to compute all vertex distances
        from <start> in <G>, and assigns these values to the vertex attribute <dist>.
        Optional: assigns the vertex attribute <indedge> to be the incoming
        shortest path edge, for every reachable vertex except <start>.
        <G> is viewed as an undirected graph.
    """

    for v in G.V():
        v.dist = None
        v.inedge = None
    start.dist = 0


def DijkstraDirected(G, start):
    """
    Arguments: <G> is a graph object, where edges have integer <weight>
        attributes,	and <start> is a vertex of <G>.
    Action: Uses Dijkstra's algorithm to compute all vertex distances
        from <start> in <G>, and assigns these values to the vertex attribute <dist>.
        Optional: assigns the vertex attribute <indedge> to be the incoming
        shortest path edge, for every reachable vertex except <start>.
        <G> is viewed as a directed graph.
    """

    for v in G.V():
        v.dist = None
        v.inedge = None
    start.dist = 0

    # Insert your code here.
    Q = []
    while len(Q) < len(G.V()):
        u = None
        for vertex in G.V():
            if vertex in Q:
                continue
            if vertex.dist is not None and (u is None or u.dist > vertex.dist):
                u = vertex
        if u is None:
            break
        Q.append(u)
        for edge in u.inclist():
            alt = edge.otherend(u)
            if edge.tail() == u:
                if alt.dist is None or alt.dist > u.dist + edge.weight:
                    alt.dist = u.dist + edge.weight
                    alt.inedge = u



def Kruskal(G):
    """
    Arguments: <G> is a graph object, where edges have integer <weight> attributes.
    Action: Uses Kruskal's algorithm to compute all a minimum weight spanning tree
        of <G> (or a minimum weight maximal spanning forest if <G> is not connected).
        Returns a list <ST> of all edges that are in the minimum weight spanning
        tree (forest).
    """
    ST = []  # will be the spanning tree. Append edge objects to this list.

    # Insert your code here.

    return ST


# Insert your code here.


def printmaxdist(G):
    unreachable = False
    numreachable = 0
    unreachablev = []
    remote = G[0]
    for v in G:
        if v.dist == None:
            unreachable = True
            unreachablev.append(v)
        # print("Vertex",v,"is unreachable")
        else:
            numreachable += 1
            if remote.dist == None or v.dist > remote.dist:
                remote = v
    print("Number of reachable vertices:", numreachable, "out of", len(G.V()))
    if (len(G.V()) - numreachable > 0):
        print("Vertices that are unreachabe:", unreachablev)
    print("Largest distance:", remote.dist, "For vertex", remote)


##############################################################################
#
# Below is test code that does not need to be changed.
#
##############################################################################

def preparedrawing(G):
    for e in G.E():
        e.colornum = 0
    for v in G.V():
        if hasattr(v, "inedge") and v.inedge != None:
            v.inedge.colornum = 1
    for v in G:
        if v.dist != None:
            v.label = v.dist
        else:
            v.label = "inf"






if __name__ == "__main__":
    from time import time

    if UseFastGraphs:
        import fastgraphs
    for FileName in TestInstances:
        if UseFastGraphs:
            print("\n\nLoading graph", FileName, "(Fast graph)")
            # G=loadgraph("graphs/"+FileName,graph)
            G = loadgraph(FileName, fastgraphs.graph)
        else:
            print("\n\nLoading graph", FileName)
            # G=loadgraph("graphs/"+FileName)
            G = loadgraph(FileName)

        for i in range(len(G.V())):
            G[i].colornum = i

        # Tuple arguments below:
        # First: printable string
        # Second: Boolean variable: should test be done?
        # Third: Function
        # Fourth: Filename
        # Fifth: Whether output should be directed
        for testalg in [("Bellman-Ford, undirected", TestBellmanFordUndirected, BellmanFordUndirected,
                         "BellmanFordUndirected", False),
                        ("Bellman-Ford, directed", TestBellmanFordDirected, BellmanFordDirected, "BellmanFordDirected",
                         True),
                        ("Dijkstra, undirected", TestDijkstraUndirected, DijkstraUndirected, "DijkstraUndirected",
                         False),
                        ("Dijkstra, directed", TestDijkstraDirected, DijkstraDirected, "DijkstraDirected", True),
                        ("Kruskal", TestKruskal, Kruskal, "Kruskal", False)]:
            if testalg[1]:
                print("\n\nTesting", testalg[0])
                startt = time()
                if testalg[0] == "Kruskal":
                    ST = testalg[2](G)
                    totalweight = 0
                    for e in ST:
                        totalweight += e.weight
                else:
                    testalg[2](G, G[0])
                endt = time()
                print("Elapsed time in seconds:", endt - startt)

                if testalg[0] != "Kruskal":
                    printmaxdist(G)
                    preparedrawing(G)
                else:
                    if len(ST) < len(G.V()) - 1:
                        print("Total weight of maximal spanning forest:", totalweight)
                    else:
                        print("Total weight of spanning tree:", totalweight)
                    for e in G.E():
                        e.colornum = 0
                    for e in ST:
                        e.colornum = 1
                    for v in G.V():
                        v.label = v._label

                if WriteDOTFiles:
                    # writeDOT(G,'graphs/'+testalg[3]+'.dot',directed=testalg[4])
                    writeDOT(G, testalg[3] + '.dot', directed=testalg[4])
