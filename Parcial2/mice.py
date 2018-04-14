from sys import stdin
from heapq import heappop,heappush

#Estudiante: Maria Paula Carrero Rivas.
#Se usó el file de python Dijkstra que está en la página del profesor Camilo Rocha
#ID de estudiante: 8911963
INF = float('inf')
ans, final, T = 0, None, None
lista = None
N = None

def solve(source,T,E,N,lista):
	global ans
	ans = 0
	temp = E-1
	dist = [ INF for i in range(N) ] ; dist[source] = 0
	visited = [ False for i in range(N) ]
	heap = [ (0,source)]

	while len(heap)!=0:
		d,u = heappop(heap)
		if not(visited[u]):
			visited[u] = True
			for v,w in lista[u]:
				if dist[v]>d+w:
					dist[v] = d+w
					heappush(heap,(dist[v],v))
	for i in range (N):
		if dist[i] <= T:
			ans+=1

def main():

  global T, E, ans
  inp = stdin
  l = 0
  cases = int(inp.readline().strip())
  while l != cases:
  	lineavacia=stdin.readline()
  	N=int(inp.readline().strip())
  	E =int(inp.readline().strip())
  	T = int(inp.readline().strip())
  	M = int(inp.readline().strip())
  	lista = [list() for i in range(N)]
  	for i in range(M):
  		a, b, time=[ int(x) for x in stdin.readline().split() ]
  		lista[b-1].append((a-1, time))
  	solve(E-1, T,E,N, lista)
  	print(ans)
  	l+=1
  	if l != cases:
  		print()

main()