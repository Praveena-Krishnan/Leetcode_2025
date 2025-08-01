class Solution:
    # Function to return Breadth First Search Traversal of given graph.
    def bfs(self, adj):
        n=len(adj)
        vis=[0]*n
        vis[0]=1
        q=[]
        q.append(0)
        bfs=[]
        while(len(q)!=0):
            node=q[0]
            q.pop(0)
            bfs.append(node)
            
            for i in adj[node]:
                if not vis[i]:
                    vis[i]=1
                    q.append(i)
                    
        return bfs