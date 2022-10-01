
from queue import PriorityQueue


class Node:
    def __init__(self, name:str ,type:str):
        self.name = name 
        self.type = type
      
class Wire:

    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.nodes_list = []
        self.pre_switch_nodes = []
        self.post_switch_nodes =[]
        self.graph =  [[0 for row in range(num_nodes)]
                      for column in range(num_nodes)]
        self.string_to_node = {}
        self.which_switch_map = {}

    def pre_switch(self, type:str)->bool:
        if type == "breaker" or type == "outlet" or type == "box":
            return True
        return False
    
    def is_switch(self, type:str)->bool:
        if type == "switch":
            return True
        return False
    
    def post_switch(self, type: str) ->bool:
        if type == "light":
            return True
        return False
    
    #this function should take of all the cases that we cant have 
    def can_connect(self,start:Node, end:Node)->bool:
        node_1_type = start.type
        node_2_type = end.type

        if self.pre_switch(node_1_type) and self.pre_switch(node_2_type):
            return True
        if self.pre_switch(node_1_type) and self.is_switch(node_2_type):
            return True 
        if self.post_switch(node_1_type) and self.post_switch(node_2_type):
            if self.which_switch_map[start.name]==self.which_switch_map[end.name]:
                return True
        if self.is_switch(node_1_type) and self.post_switch(node_2_type):
            if self.which_switch_map[end.name]==start.name:
                return True
        if self.post_switch(node_1_type) and self.is_switch(node_2_type):
            if self.which_switch_map[start.name]==end.name:
                return True
    
        return False

    def prims_mst(self, start):
        heap = PriorityQueue()
        second_priority = PriorityQueue()
       
        heap.put((0,start.name))
      
        visited = []
        cost = 0
        switch_nodes = []
        
        while (len(visited) < self.num_nodes):
           
            second_priority= PriorityQueue()
            while (not heap.empty()):
                first,second = heap.get()
                second_priority.put((first,second))
            heap = second_priority
       
            
            if len(visited) < len(self.pre_switch_nodes):
                #this means if you havent seen all of the pre_switch_nodes yet
                second,first = heap.get()
               
                while first not in self.pre_switch_nodes or first in visited:
                    
                    if first not in self.pre_switch_nodes:
                        switch_nodes.append(first)
                        switch_nodes.append(second)
    
                    second,first = heap.get()
                   
                
            else:
              
                if len(switch_nodes)!=0:
                  
                    for x in range(0,len(switch_nodes), 2):
                        heap.put((switch_nodes[x+1],switch_nodes[x]))
                    switch_nodes = []
                second,first = heap.get()
                
                while first in visited:
                    second,first= heap.get()


            cost += int(second)
            visited.append(first)
            
            node = self.string_to_node[first]
            index = self.nodes_list.index(node)
            
            for neighbors in range(self.num_nodes): 
                if self.graph[index][neighbors]!= 0 and self.can_connect(self.nodes_list[index],self.nodes_list[neighbors]):
                    weight = self.graph[index][neighbors]
                    heap.put((weight, self.nodes_list[neighbors].name))
            

        return cost
       
        
if __name__ == '__main__':
    # test_file = open("wires.txt")
    numbers = input().split()
    # numbers = test_file.readline().split()
    junctions = int(numbers[0])
    wire = Wire(junctions)
    dependencies = int(numbers[1])
    wire.num_edges = dependencies

   
    for x in range(junctions):
        # node = test_file.readline().split()
        node = input().split()
        new_node = Node(node[0], node[1])
        if node[1]=="light":
            if wire.nodes_list[x-1].type == "switch":
                wire.which_switch_map[node[0]] = wire.nodes_list[x-1].name
            if wire.nodes_list[x-1].type == "light":
                wire.which_switch_map[node[0]] = wire.which_switch_map[wire.nodes_list[x-1].name]

        if wire.pre_switch(node[1]):
            wire.pre_switch_nodes.append(new_node.name)
        else:
            wire.post_switch_nodes.append(new_node.name)

        wire.string_to_node[node[0]]= new_node
        wire.nodes_list.append(new_node)
    
    for x in range(dependencies):
        # edge = test_file.readline().split()
        edge = input().split()
        node_1 = wire.string_to_node[edge[0]]
        node_2 = wire.string_to_node[edge[1]]
       
        wire.graph[wire.nodes_list.index(node_1)][wire.nodes_list.index(node_2)]=int(edge[2])
        wire.graph[wire.nodes_list.index(node_2)][wire.nodes_list.index(node_1)]=int(edge[2])
    
    breaker_box = wire.nodes_list[0]
    print(wire.prims_mst(breaker_box))
