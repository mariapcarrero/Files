from heapq import *
from sys import stdin
#Estudiante: Maria Paula Carrero Rivas.
#Trabajado con: Juan Sebastian Rivera
#ID de estudiante: 8911963
graph, banks, policeS = None,None,None
N, M, B, P = None, None, None , None
nodos, pq, distancia = None, None, None


def dijkstra(graph,source):
  global banks, policeS, N,M,B, P,nodos, pq, distancia
  visited = [ False for i in range(len(graph)) ]
  pq = []
  distancia = [ float('inf') for i in range(N+1) ]  
  for i in range(P):
    heappush(pq,(0,policeS[i])) ; distancia[policeS[i]] = 0
  while len(pq)!=0:
    wu,u = heappop(pq)
    if not(visited[u]):
      for v,wv in graph[u]:
        if distancia[v] > distancia[u] + wv:
          distancia[v] = min(distancia[u] + wv, distancia[v])
          if visited[v] == False: heappush(pq,(distancia[v],v))
      visited[u] = True

def main():
  global graph,banks, policeS, N,M , B ,P , distancia
  inp = stdin
  l = 1
  l = [ int(x) for x in stdin.readline().split() ]
  while l != []:
    N,M,B,P =l[0], l[1], l[2], l[3]
    graph = [ list() for i in range(N) ]
    banks = [ list() for i in range(B) ]
    markedbank = [ False for i in range(N) ]
    policeS = [ list() for i in range(P) ]
    i = 0
    while i < M:
      u,v,w = [ int(x) for x in stdin.readline().split() ]
      graph[u].append((v,w)) ; graph[v].append((u,w))
      i+=1
    banks = [ int(x) for x in stdin.readline().split() ]
    for x in range(B):
      markedbank[banks[x]] = True 
    if P != 0:
      policeS = [ int(x) for x in stdin.readline().split() ]
      values = (dijkstra(graph,policeS[0]))
    if P == 0:
      values = (dijkstra(graph,0))
    maxval, cops = 0, 0
    for i in range(N):
      if (markedbank[i]):
        maxval = max(maxval, distancia[i])
    for i in range(N):
      if (markedbank[i]):
        cops += maxval == distancia[i]
    if maxval == float('inf'):
      print(cops, '*')
    else:
      print('{} {}' .format( cops, maxval));
    for i in range(N):
      if (maxval == distancia[i] and markedbank[i]):
        cops-= 1
        if cops == 0:
          print (i, end = '\n')
        else:
          print (i, end = ' ')
    l = [ int(x) for x in stdin.readline().split() ]

main()