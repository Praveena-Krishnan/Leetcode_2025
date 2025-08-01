#get input for no. of vertices and edges
n,m=map(int,input().split())
# Initialize the adjacency matrix
adj_matrix=[[0 for i in range(n)] for j in range(n)]
for i in range(m):
    u,v=map(int,input().split())
    adj_matrix[u][v]=1
    adj_matrix[v][u]=1  # For undirected graph
    
# Print the adjacency matrix
for i in range(n):
    for j in range(n):
        print(adj_matrix[i][j], end=' ')
    print()
    
#initialise adjacency list
adj_list={i:[] for i in range(n)}
# Fill the adjacency list
for i in range(m):
    u,v=map(int,input().split())
    adj_list[u].append[v]