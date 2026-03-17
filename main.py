import sys
from collections import deque
 
def bfs_reachability(adj, s, t, n):
    """BFS: O(n+m) space. Check if t reachable from s."""
    visited=[False]*n; q=deque([s]); visited[s]=True
    while q:
        v=q.popleft()
        if v==t: return True
        for u in adj[v]:
            if not visited[u]: visited[u]=True; q.append(u)
    return False
 
def inductive_counting(adj, s, t, n):
    """Inductive counting for directed reachability (Savitch-style)."""
    def reach(u, v, k):
        if k==0: return u==v or v in adj[u]
        for w in range(n):
            if reach(u,w,k-1) and reach(w,v,k-1): return True
        return False
    return reach(s, t, (n-1).bit_length())
 
def st_connectivity_undirected(adj, s, t, n):
    """Undirected s-t conn: O(log^2 n) randomised (Reingold: O(log n) det)."""
    visited=set(); stack=[s]
    while stack:
        v=stack.pop()
        if v in visited: continue
        visited.add(v)
        if v==t: return True
        stack.extend(adj[v])
    return False
 
n=8
edges=[(0,1),(1,2),(2,3),(3,4),(4,5),(5,6),(6,7),(1,4),(2,5)]
adj={i:[] for i in range(n)}
for u,v in edges: adj[u].append(v); adj[v].append(u)
print(f"BFS: 0→7? {bfs_reachability(adj,0,7,n)}")
print(f"Inductive: 0→7? {inductive_counting(adj,0,7,n)}")
print(f"ST-conn: 0→6? {st_connectivity_undirected(adj,0,6,n)}")
