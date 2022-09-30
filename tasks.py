from collections import defaultdict

# topological sorting of a graph using kahns algorithm: BFS 
# liza trundle 
#emt8kdn 
# cs 3100 : algorithms

class Graph:
    def __init__(self, edges, vertices):
        self.edges = edges
        self.vertices = vertices 
        self.topological_sorted = ""
        self.adj_list = defaultdict(list)
        self.incoming_edges = {}
        self.no_edges = []

    def top_sort(self):
        count = 0
        for vertex in range(self.vertices):
            if list(self.adj_list.keys())[vertex] not in self.incoming_edges:
                self.no_edges.append(list(self.adj_list.keys())[vertex])
        
        while self.no_edges:
            self.no_edges.sort()
            start = self.no_edges.pop(0)
            if start in self.adj_list:
                for node in self.adj_list[start]:
                    self.incoming_edges[node]-=1
                    if self.incoming_edges[node]==0:
                        self.no_edges.append(node)
            self.topological_sorted+=start + " "
            count+=1
        if count != self.vertices:
            return("IMPOSSIBLE")
        else:
            return(self.topological_sorted)

if __name__ == '__main__':
    
    numbers = input()
    numbers = numbers.split()
    vertices= int(numbers[0])
    edges = int(numbers[1])

    graph = Graph(edges, vertices)

    for x in range(vertices):
        graph.adj_list[input()]
        
    for x in range(edges):
        edge= input()
        res = edge.split()
        graph.adj_list[res[0]].append(res[1])
        if res[1] in graph.incoming_edges:
            graph.incoming_edges[res[1]]+=1
        if res[1] not in graph.incoming_edges:
            graph.incoming_edges[res[1]]=1

    print(graph.top_sort())
