# Author: Aric Hagberg (hagberg@lanl.gov)

#    Copyright (C) 2004-2019 by
#    Aric Hagberg <hagberg@lanl.gov>
#    Dan Schult <dschult@colgate.edu>
#    Pieter Swart <swart@lanl.gov>
#    All rights reserved.
#    BSD license.



#    Modified by Shivendra Agrawal
import random
import re
import matplotlib.pyplot as plt
import networkx as nx




## DO NOT MODIFY THE CODE WITHIN THIS BLOCK ########################################

# this function returns the graph to be considered
def miles_graph():
    """ Return the cites example graph in miles_dat.txt
        from the Stanford GraphBase.
    """
    # open file miles_dat.txt.gz (or miles_dat.txt)
    import gzip
    fh = gzip.open('miles_dat.txt.gz', 'r')

    G = nx.Graph()
    G.position = {}
    G.population = {}

    cities = []
    for line in fh.readlines():
        line = line.decode()
        if line.startswith("*"):  # skip comments
            continue

        numfind = re.compile("^\d+")

        if numfind.match(line):  # this line is distances
            dist = line.split()
            for d in dist:
                G.add_edge(city, cities[i], weight=int(d))
                i = i + 1
        else:  # this line is a city, position, population
            i = 1
            (city, coordpop) = line.split("[")
            cities.insert(0, city)
            (coord, pop) = coordpop.split("]")
            (y, x) = coord.split(",")

            G.add_node(city)
            # assign position - flip x axis for matplotlib, shift origin
            G.position[city] = (-int(x) + 7500, int(y) - 3000)
            G.population[city] = float(pop) / 1000.0
    return G




# this function is unimportant - it simply draws the graph
def draw_graph(G, kruskal_selected_edges, sorted_edges):
    '''
    Plots the networkx graph with MST selected by Kruskal's as overlay

    :param G: Networkx graph
    :param kruskal_selected_edges: List of edge tuple
    :return: None
    '''
    pos = G.position  # positions for all nodes
    # nodes
    nx.draw_networkx_nodes(G, pos, node_size=10)
    title = ""

    if len(kruskal_selected_edges) > 0:
        non_MST_edges = [edge for edge in sorted_edges if edge not in kruskal_selected_edges]
        nx.draw_networkx_edges(G, pos, edgelist=kruskal_selected_edges, width=0.5, edge_color='g')
        print("\nNumber of edges selected by Kruskal's = ", len(kruskal_selected_edges))

    #    nx.draw_networkx_edges(G, pos, edgelist=non_MST_edges, width=1, alpha=0.5, edge_color='b')
        title = ", Edges in the MST = " + str(len(kruskal_selected_edges))
    #else:
    #    nx.draw_networkx_edges(G, pos, edgelist=sorted_edges, width=1, alpha=0.5, edge_color='b')
    plt.title("Threshold = " + str(EDGE_SELECTION_CRITERIA) + title)
    plt.savefig('MST.png')
    plt.show()






# this is the union-find Find(x) function - very important, use it in Kruskal's
def find(vertex):
    '''
    Function that returns the leader vertex for any 'vertex'
    '''
    return leader_dict[vertex]

####################################################################################







# 1. (b)
def union(u,v):
    
    # if find(u) is the bigger set, let u swallow v
    if len(components[find(u)]) >= len(components[find(v)]):
        
        # let find(u) swallow everything in the smaller set
        for i in range(0,len(components[find(v)])):
            components[find(u)].append(components[find(v)][i])
            
        # let find(u) become the leader of everything in the smaller set
        for i in range(0,len(components[find(u)])):
            leader_dict[components[find(u)][i]] = find(u)
        
    # if find(v) is the bigger set, let v swallow u
    else:
          
        # let find(v) swallow everything in the smaller set
        for i in range(0,len(components[find(u)])):
            components[find(v)].append(components[find(u)][i])
        
        # let find(v) become the leader of everything in the smaller set
        for i in range(0,len(components[find(v)])):
            leader_dict[components[find(v)][i]] = find(v)








if __name__ == '__main__':
    
    
    
    ########## DO NOT MODIFY THE CODE IN THIS BLOCK ################################

    EDGE_SELECTION_CRITERIA = random.choice([500 + (i+1)*20 for i in range(4)])
    
    
    # G is the graph to be considered
    G = miles_graph()
    print("Loaded miles_dat.txt containing 128 cities.")
    print("digraph has %d nodes with %d edges" % (nx.number_of_nodes(G), nx.number_of_edges(G)))


    # all edge(u,v) and weight(u,v) in E are in this list as tuple + dictionary
    # ex. ('Youngstown, OH', 'Winston-Salem, NC', {'weight': 494})
    edges_to_consider = [(u, v, d) for (u, v, d) in G.edges(data = True) if d['weight'] <= EDGE_SELECTION_CRITERIA]
    
    
    # all sorted edge(u,v) in E are in this list as a tuple
    # ex. ('Wheeling, WV', 'Steubenville, OH')
    sorted_edges = [(u, v) for (u, v, d) in sorted(edges_to_consider, key=lambda x:x[2]['weight'])]


    # all v in V are in this list
    # ex. Stevens Point, WI
    vertices = []
    for u, v in sorted_edges:
        vertices.append(u)
        vertices.append(v)
    vertices = list(set(vertices))
    print("Edges considered (in ascending order) for this graph = ", len(sorted_edges))


    # dictionary with key:value as edge(u,v):weight(u,v)
    length_of_edge = {(u, v):d for (u, v, d) in edges_to_consider}

    # dictionary with key:value as v:Find(v)
    leader_dict = {v : v for v in vertices}

    # dictionary with key:value as Find(v): all v in Find(v)
    components = {find(v) : [v] for v in vertices}


    # MST = NULL
    kruskal_selected_edges = []
    ################################################################################



    # 1. (a)
    temp = 0
    k = 2 # modify the value of k here
    # for each edge(u,v) in E, in ascending weight order
    for i in range(0, len(sorted_edges)):

        # if Find(u) != Find(v)
        if (find(sorted_edges[i][0]) != find(sorted_edges[i][1])):

            # MST = MST U edge(u,v)
            kruskal_selected_edges.append(sorted_edges[i])

            # Union(u,v)
            union(sorted_edges[i][0], sorted_edges[i][1])
            
            # 1. (c)
            temp = temp + 1
            if(temp == 127 - k + 1):
                spacing = length_of_edge[kruskal_selected_edges[-1]]['weight']
                print("\nspacing =", spacing)
            
    del kruskal_selected_edges[-1]
            
        

    # Do not remove this line, it will save the MST as a figure for you
    draw_graph(G, kruskal_selected_edges, sorted_edges)
