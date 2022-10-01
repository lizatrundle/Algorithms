
class Board:

     def __init__(self, count):
        self.path = ""
        self.visited = []
        self.num_nodes = count
        self.start_node = 0
        self.end_node = self.num_nodes -1
        self.matrix = [[0 for column in range(self.num_nodes)]for row in range(self.num_nodes)]
       
     def add_edge(self, u,v):
        self.matrix[u][v]=1
        self.matrix[v][u]=1
       
     def remove_edge(self, edge):
        for x in range(self.num_nodes):
            self.matrix[x][edge]=0
            self.matrix[edge][x]=0

     def exhaustive_dfs(self, graph, start, end, visited, path):
        path += str(start)+ "-"
        visited.append(start)

        if start == end:
            path = path.rstrip(path[-1])
            print(path)
        
        for neighbors in range(self.num_nodes): 
            if self.matrix[start][neighbors]==1 and neighbors not in visited:
                    self.exhaustive_dfs(graph,neighbors,end,visited,path)
                    visited.remove(neighbors)

if __name__ == '__main__':
    
    num_intersections = input()
    num_roads = input()
    num_roads = int(num_roads)
    graph = Board(int(num_intersections))

    for line in range(num_roads):
        text = input().split()
        u = text[0]
        v = text[1]
        u = int(u)
        v = int(v)
        graph.add_edge(u,v)
    
    dangerous = input()
    dangerous = int(dangerous)

    for x in range(dangerous):
        edge = input()
        graph.remove_edge(int(edge))

    graph.exhaustive_dfs(graph.matrix,graph.start_node, graph.end_node, graph.visited, graph.path)
   