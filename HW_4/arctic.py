from sys import stdin
import math

class dforest(object):

  def __init__(self,size=100):
    """create an emtpy forest"""
    self.__parent = [ i for i in range(size) ]
    self.__size = [ 1 for i in range(size) ]
    self.__rank = [ 0 for i in range(size) ]
    
  def __str__(self):
    """return the string representation of the forest"""
    return str(self.__parent)

  def __len__(self):
    """return the number of elements in the forest"""
    return len(self.__parent)
  
  def __contains__(self,x):
    """return if x is an element of the forest"""
    return 0 <= x < len(self)

  def find(self,x):
    """return the representative of the tree of x"""
    assert x in self
    if self.__parent[x]!=x:
      self.__parent[x] = self.find(self.__parent[x])
    return self.__parent[x]

  def union(self,x,y):
    """make the union of the trees of x and y"""
    assert x in self and y in self
    rx,ry = self.find(x),self.find(y)
    if rx!=ry:
      nx,ny = self.__rank[rx],self.__rank[ry]
      if nx<=ny:
        self.__parent[rx] = ry
        self.__size[ry] += self.__size[rx]
        if nx==ny: self.__rank[ry]+=1
      else:
        self.__parent[ry] = rx
        self.__size[rx] += self.__size[ry]
        
  def size(self,x):
    """return the size of the tree of x"""
    assert x in self
    return self.__size[self.find(x)]


def kruskal(G,a):
  """G is a connected graph in adjacency list representation. For each
  vertex u in G, G[u] is the list of pairs (v0,w0),...(vn,wn) such that
  there is an edge between u and vi with weight wi (0 <= i <= n)"""
  edges = list()
  for i in range(len(G)):               # collect the edges in G
    for v,w in G[i]:
      if(w != -1):
      	edges.append([i,v,w])
  # sort the edges in ascending order w.r.t weights in the edges
  edges.sort(key=lambda x: x[2])   
  df = dforest(len(G))
  i = 0
  nnum = 0;
  while i!=len(edges):
    u,v,w = edges[i]
    if df.find(u)!=df.find(v):
      df.union(u,v)
      nnum += 1;
      if(nnum == a):
      	return w;
    i += 1

def main():
	inp = stdin
	cases = int(stdin.readline().strip())
	while(cases != 0):
		line = stdin.readline().strip().split();
		s,w = int(line[0]), int(line[1]);
		a=w-s
		lista = []
		while(w != 0):
			line = stdin.readline().strip().split()
			lista.append((int(line[0]), int(line[1])));
			w -= 1;
		i = 0;
		adjacencyList = [ [(i,-1) for i in range(len(lista))]  for i in range(len(lista))];
		while(i != len(lista)):
			j = i+1;
			while(j != len(lista)):
				dist = math.hypot(lista[i][0] - lista[j][0], lista[i][1] - lista[j][1])
				adjacencyList[i][j] = (j, dist);
				j += 1;
			i += 1;
		cases -= 1;
		print('{:.2f}'.format(kruskal(adjacencyList,a)))


main();