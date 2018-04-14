from sys import stdin
from heapq import heappop,heappush
#Estudiante: Maria Paula Carrero Rivas.
#Se usó el file de python Dijkstra que está en la página del profesor Camilo Rocha, teniendo en cuenta el codigo de DFS (delta)
#ID de estudiante: 8911963
INF = float('inf')
ans, final, T = 0, None, None
lista = None
N = None
delta = [(-1, 0), (0,-1), (1,0), (0,1)]

def solve(source,destination, lista, N , M, m0):
  global ans
  ans = 0
  dist = [ INF for i in range(N*M) ] ;
  visited = [ False for i in range(N*M) ] 
  heap = [ (m0,source)]
  while len(heap)!=0:
    d,u = heappop(heap)
    if not(visited[u]):
      visited[u] = True
      for v,w in lista[u]:
        if dist[v]>d+w:
          dist[v] = d+w
          heappush(heap,(dist[v],v))
  return dist[destination]

def main():

  global T, E, ans,delta
  ans = 0
  inp = stdin
  l = 0
  cases = int(inp.readline().strip())
  while l != cases:
    N=int(inp.readline().strip())
    M =int(inp.readline().strip())
    visited = [ [ 0 for c in range(M) ] for r in range(N) ]
    lista = [list() for i in range(N*M)]
    matrix = [ list() for r in range(N) ]
    for i in range (N):
      fila = [ int(x) for x in stdin.readline().split() ]
      matrix[i] = fila
    i = 0
    for r in range (N):
      for c in range(M):
        lista[i].append((i, matrix[r][c]))
        for dr,dc in delta:
          if 0<=r+dr<N and 0<=c+dc<M and visited[r][c]==0:
            if r+dr > r or r+dr < r:
              lista[i].append((i+(dr*M), matrix[r+dr][c]))
            elif c+dc < c or c+dc > c:
              lista[i].append((i+dc, matrix[r][c+dc]))
        i+=1
    print(solve(0, N*M-1, lista,N, M, matrix[0][0]))
    l+=1

main()