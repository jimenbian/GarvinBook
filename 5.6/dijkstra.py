class Dijkstra():
    def __init__(self,graph, start, end):
        self.graph = graph
        self.start = start
        self.end = end
        self.weights = self.init_weights()
        self.Preds = self.init_Preds()
        self.S = self.init_S()
        self.shortest_path = []

    def calculate_preds(self):
        position = self.start
        while self.S[self.end-1] == False:
            try:
                self.calculate_weight(position)
                weight, vertex = min(
                        [ (weight, vertex) 
                        for vertex, weight in enumerate(self.weights)
                        if self.S[vertex] == False]
                        )
                if self.S[position-1] == False:
                    self.S[position-1] = True
                position = vertex+1
            except:
                print "Erro - Without shortest path, please check the vertex and weights"
                self.S[self.end-1] = True

    def calculate_weight(self,position):        
        for vertex , weight in self.graph.get(position).iteritems():
            if (weight + self.weights[position-1] <= self.weights[vertex-1]):
                self.Preds[vertex-1] = position
                self.weights[vertex-1] = weight + self.weights[position-1]

    def calculate_shortest_path(self):
        end = self.end
        self.shortest_path.append(end)
        while end != -1:
            if self.Preds[end-1] != -1:
                self.shortest_path.append(self.Preds[end-1])            
            end = self.Preds[end-1]
        self.shortest_path.reverse()

    def get_Pred(self, vertex):
        return self.Preds[vertex-1]

    def get_weight(self,cost):
        return self.weights[cost-1]

    def init_weights(self):
        weights = []
        for position in range(len(self.graph)):
            weights.append(float("inf"))
        weights[self.start-1] = 0
        return weights

    def init_Preds(self):
        Preds = []
        for position in range(len(self.graph)):
            Preds.append(None)
        Preds[self.start-1] = -1
        return Preds

    def init_S(self):
        S = []
        for position in range(len(self.graph)):
            S.append(False)
        return S
    def set_labels(self):
        labels={}
        for position in self.graph.keys():
            labels[position]=position
        return labels
    
    def get_edgelist(self):
        start =  self.start
        list_shortest_path = []
        for vertex in self.shortest_path:
            neighbor = (start,vertex)
            list_shortest_path.append(neighbor)
            start = vertex
        return list_shortest_path

    def get_list_weights_edge(self):
        list_weights_edge={}
        for position in self.graph.keys():
            for vertex, weight in self.graph.get(position).iteritems():
                if not(list_weights_edge.get((vertex,position))):                    
                    list_weights_edge[(position,vertex)] = weight
        return list_weights_edge

if __name__ == '__main__':
   print "Exemplo 1 - Graph"
   graph = { 
        1: { 2: 1, 3: 5 },
        2: { 4: 1, 5: 6},
        3: { 4: 2, 5: 1},
        4: { 3: 2, 2: 1},
        5: { 2: 6, 3: 1},
        }
   for value in range(1,len(graph)+1):
       print value, graph.get(value)
    
   print "\n"
   print "Start: %s \nEnd: %s" %(1,5)
   dijkstra = Dijkstra(graph,1,5)
   dijkstra.calculate_preds()
   dijkstra.calculate_shortest_path()
   print "Shortest path : %s" %(dijkstra.shortest_path)