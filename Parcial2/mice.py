from sys import stdin
from heapq import heappop,heappush

#Estudiante: Maria Paula Carrero Rivas.
#Se usó el file de python Dijkstra que está en la página del profesor Camilo Rocha
#ID de estudiante: 8911963
INF = float('inf')
ans, final, T = None, None, None
lista = None
N = None
def solve():
	pass

def solve1(source,T,E,N,lista):
	global ans
	temp = E-1
	dist = [ INF for i in range(N) ] ; dist[source] = 0
	#print(dist)
	visited = [ False for i in range(N) ]
	flag = 0
	heap = [ (0,source) ]
	#print('source = ',sourc
	while len(heap)!=0:
		d,u = heappop(heap)
		if not(visited[u]):
			visited[u] = True
			for v,w in lista[u]:
				if dist[v]>d+w:
					dist[v] = d+w
					heappush(heap,(dist[v],v))
	if dist[temp] <=T:
		ans+=1						

def solve2(lista,T,E,N):
	global ans
	ans = 0
	i = 0
	if T == 0:
		return ans+1
	while i < (len(lista)):
		if i == E-1:
			ans+=1
		else:
			solve1(i,T,E,N,lista)
		i+=1
	return ans

def main():

  global T, E
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
  		lista[a-1].append((b-1, time))
  	print(solve2(lista, T,E,N))
  	l+=1
  	if l != cases:
  		print()

main()