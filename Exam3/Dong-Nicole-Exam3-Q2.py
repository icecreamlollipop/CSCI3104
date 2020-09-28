"""
@author: Rhoenigman
         Shivendra
"""
import networkx as nx

"""
The function to generate the input graph

:return: Returns the NetworkX Graph for Q2
"""
def Question2():
    # Create a directed graph
    G = nx.DiGraph()

    # The 'length' on each edge should be ignored and is only for drawing.
    # Adding an edge also adds the node
    G.add_edge('EC', 'A', length=40, weight=1.0)
    G.add_edge('EC', 'H', length=40, weight=1.0)
    G.add_edge('EC', 'J', length=60, weight=1.0)

    G.add_edge('H', 'G', length=40, weight=1.0)
    G.add_edge('H', 'K', length=40, weight=1.0)

    G.add_edge('G', 'L', length=40, weight=1.0)
    G.add_edge('G', 'F', length=40, weight=1.0)

    G.add_edge('F', 'E', length=40, weight=1.0)

    G.add_edge('E', 'HUMN', length=40, weight=1.0)

    G.add_edge('J', 'S', length=80, weight=1.0)
    G.add_edge('J', 'K', length=60, weight=1.0)

    G.add_edge('K', 'L', length=40, weight=1.0)
    G.add_edge('L', 'M', length=40, weight=1.0)
    G.add_edge('M', 'N', length=40, weight=1.0)
    G.add_edge('M', 'F', length=60, weight=1.0)

    G.add_edge('N', 'O', length=80, weight=1.0)
    G.add_edge('N', 'E', length=80, weight=1.0)

    G.add_edge('O', 'HUMN', length=40, weight=1.0)

    G.add_edge('A', 'S', length=60, weight=1.0)
    G.add_edge('A', 'B', length=40, weight=1.0)

    G.add_edge('B', 'R', length=40, weight=1.0)
    G.add_edge('B', 'C', length=40, weight=1.0)

    G.add_edge('S', 'R', length=60, weight=1.0)
    G.add_edge('R', 'Q', length=40, weight=1.0)

    G.add_edge('Q', 'C', length=40, weight=1.0)
    G.add_edge('Q', 'P', length=60, weight=1.0)

    G.add_edge('C', 'D', length=40, weight=1.0)
    G.add_edge('D', 'HUMN', length=40, weight=1.0)
    G.add_edge('P', 'D', length=40, weight=1.0)
    G.add_edge('P', 'O', length=60, weight=1.0)
    G.add_edge('O', 'HUMN', length=40, weight=1.0)

    G.add_edge('T', 'Q', length=40, weight=1.0)
    G.add_edge('T', 'P', length=40, weight=1.0)
    G.add_edge('T', 'O', length=40, weight=1.0)
    G.add_edge('T', 'N', length=40, weight=1.0)
    G.add_edge('T', 'M', length=40, weight=1.0)

    G.add_edge('R', 'T', length=40, weight=1.0)
    G.add_edge('S', 'T', length=40, weight=1.0)
    G.add_edge('J', 'T', length=40, weight=1.0)
    G.add_edge('K', 'T', length=40, weight=1.0)
    G.add_edge('L', 'T', length=40, weight=1.0)

    return G











"""
A utility function to help visualize the generated graph

:param G: NetworkX Graph
:return: None (instead saves the input graph in .png format)
"""
def draw_graph(G):
    import matplotlib.pyplot as plt
    import pylab
    edge_labels = dict([((u, v,), d['weight'])
                        for u, v, d in G.edges(data=True)])
    node_labels = {node: node for node in G.nodes()}

    pos = nx.spectral_layout(G)
    nx.draw_networkx_labels(G, pos, labels=node_labels)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    nx.draw(G, pos, node_size=500, edge_cmap=plt.cm.Reds)
    plt.savefig('Finals_Q2_Graph.png')
    pylab.title("Input Graph")
    pylab.show()



INF = 999999999




def adjMatrix(G):

	global INF
	# u = EC which is also a number
	# v = HUMN which is also a number
	# define k later

	# create an empty adjacency matrix
	V = G.number_of_nodes()
	adj = [[INF for i in range(V)] for j in range(V)]

	# create a dictionary to map nodes to matrix indices
	dn = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7, "EC":8, "J":9, "K":10, "L":11, "M":12, "N":13, "O":14, "P":15, "Q":16, "HUMN":17, "R":18, "S":19, "T":20}

	# fill the adjacency matrix
	for i in G.edges.data():
		tmp = list(i)
		s = dn[tmp[0]]
		t = dn[tmp[1]]
		w = int(tmp[2]['weight'])
		adj[s][t] = w

	# diagonal elements are zero
	for i in range(0, V):
		for j in range(0, V):
			if(i == j):
				adj[i][j] = 0

	return adj




path = []


def findPath(adj, u, v, k):

	global path
	global INF

	# get number of nodes
	V = len(adj);

	# base cases
	if(k == 0 and u == v):
		return 0
	elif(k == 1 and adj[u][v] != -1):
		return adj[u][v]

	# initialize the distance as infinity
	dist = INF

	# iterate through all the vertices
	for i in range(V):

        # if there is a possible path from u to i, and the current vertex i isn't the start or end vertex,
		if adj[u][i] != INF and u != i and v != i:

            # find the distance from u to v if we include this current vertex i
			tmp = findPath(adj, i, v, k - 1)

            # either we include this current vertex or we don't; whichever is the smaller distance
			if tmp != INF:
				dist = min(dist, adj[u][i] + tmp)
                
			# if the current vertex is to be included, append it to the list
			if(dist == adj[u][i] + tmp):
				path.append(i)

	return dist





def main():
    ################## READ CAREFULLY ##############################

    # Note that you cannot use any networkx functionality
    # which makes the solution trivial

    # The 'length' on each edge (while generating the graph)
    # should be ignored and is only for drawing.
    # You should consider the 'weight' for finding the smallest path.
    # The above example has weights 1 but the weight can be anything.
    # Later on we may post some more graphs for testing.
    G = Question2()
    #draw_graph(G)

    # Call your function here that takes in the Graph "G"
    # and returns the shortest path
    # (note that it is not the length but the entire path)

    dn = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7, "EC":8, "J":9, "K":10, "L":11, "M":12, "N":13, "O":14, "P":15, "Q":16, "HUMN":17, "R":18, "S":19, "T":20}
    u = dn["EC"]
    v = dn["HUMN"]
    k = 4

    adj = adjMatrix(G)
    dist = findPath(adj, u, v, k + 1)

    path.append(dn["EC"])
    path.reverse()
    path.append(dn["HUMN"])

    for i in range(0, len(path)):
    	for key, val in dn.items():
    		if val == path[i]:
    			path[i] = key

    print("The shortest distance is =", dist)
    print("The path is =", path)


if __name__ == "__main__":
    # The driver function
    main()
