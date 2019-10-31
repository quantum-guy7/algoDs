
'''Returns true if there is a path from source 's' to sink 't' in 
    residual graph. Also fills parent[] to store the path '''
def BFS(graph,s, t, parent,n,aug_path): 
  
        # Mark all the vertices as not visited 
        visited =[0]*n
          
        # Create a queue for BFS 
        queue=[] 
          
        # Mark the source node as visited and enqueue it 
        queue.append(s) 
        visited[s] = True
           
         # Standard BFS Loop 
        while queue: 
  
            #Dequeue a vertex from queue and print it 
            u = queue.pop() 
            aug_path.append(u)
            # Get all adjacent vertices of the dequeued vertex u 
            # If a adjacent has not been visited, then mark it 
            # visited and enqueue it 
            for ind, val in enumerate(graph[u]): 
                if visited[ind] == 0 and val > 0 : 
                    queue.append(ind) 
                    visited[ind] = 1
                    parent[ind] = u 
  
        # If we reached sink in BFS starting from source, then return 
        # true, else false 
        return True if visited[t] else False
              
      
    # Returns tne maximum flow from s to t in the given graph 
def FordFulkerson(graph,source, sink,n): 
  
        # This array is filled by BFS and to store path 
        parent = [-1]*n 
  
        max_flow = 0 # There is no flow initially
        aug_path=[]
         
        # Augment the flow while there is path from source to sink 
        while BFS(graph,source, sink, parent,n,aug_path) : 
  	    #k=BFS(graph,source, sink, parent,n)
            print("Augmented path:",aug_path)
            aug_path=[]
            # Find minimum residual capacity of the edges along the 
            # path filled by BFS. Or we can say find the maximum flow 
            # through the path found. 
            path_flow = 10000 
            s = sink 
            while(s !=  source): 
                path_flow = min (path_flow, graph[parent[s]][s]) 
                s = parent[s] 
  
            # Add path flow to overall flow 
            max_flow +=  path_flow 
  
            # update residual capacities of the edges and reverse edges 
            # along the path 
            v = sink 
            while(v !=  source): 
                u = parent[v] 
                graph[u][v] -= path_flow 
                graph[v][u] += path_flow 
                v = parent[v] 
  
        return max_flow 
  
   
# Create a graph given in the above diagram 
  
graph = [[0, 16, 13, 0, 0, 0], 
        [0, 0, 10, 12, 0, 0], 
        [0, 4, 0, 0, 14, 0], 
        [0, 0, 9, 0, 0, 20], 
        [0, 0, 0, 7, 0, 4], 
        [0, 0, 0, 0, 0, 0]] 
  
n=6
source = 0; sink = 5
print ("The maximum possible flow is:" ,FordFulkerson(graph,source, sink,n)) 
