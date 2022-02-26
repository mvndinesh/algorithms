class Graph:
    def __init__(self):
        self.adj_list={}

    def add_vertex(self,vertex):
        adj_list = self.adj_list
        if vertex not in adj_list.keys():
            adj_list[vertex] = []
            return True
        return False

    def add_edge(self,v1,v2):
        adj_list = self.adj_list
        if v1 in adj_list.keys() and v2 in adj_list.keys():
            adj_list[v1].append(v2)
            adj_list[v2].append(v1)
            return True
        return False

    def print_vertex(self):
        adj_list = self.adj_list
        for each_key in adj_list.keys():
            print(adj_list[each_key])

    def remove_edge(self,v1,v2):
        adj_list = self.adj_list
        if v1 in adj_list.keys() and v2 in adj_list.keys():
            adj_list[v1].remove(v2)
            adj_list[v2].remove(v1)

    def remove_vertex(self,v1):
        adj_list = self.adj_list
        for each_key in adj_list[v1]:
            adj_list[each_key].remove(v1)
        del adj_list[v1]



graph = Graph()
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_vertex('D')
graph.add_edge('A','B')
graph.add_edge('A','C')
graph.add_edge('D','C')
graph.add_edge('D','B')
graph.add_edge('D','A')
# graph.remove_edge('D','A')
graph.remove_vertex('D')
graph.print_vertex()


