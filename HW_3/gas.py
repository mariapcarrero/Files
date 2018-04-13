#Estudiante: Maria Paula Carrero Rivas
#Codigo tomado de la página del profesor Camilo Rocha
from sys import stdin

def mic_wf(L,H,a):
  a.sort()
  ans,low,n,ok,N = list(),L,0,True,len(a)
  while ok and low<H and n!=N:
    ok = a[n][0]<=low
    best,n = n,n+1
    while ok and n!=N and a[n][0]<=low:
      if a[n][1]>a[best][1]:
        best = n
      n += 1
    ans.append(best)
    low = a[best][1]
  ok = ok and low>=H
  if ok==False:
    ans = list()
  return len(ans)

def main():
  inp = stdin
  L, G = float('-inf'),float('-inf')
  while L != 0 and G != 0:
    l = [int(x) for x in inp.readline().strip().split()] #l tiene L y G
    L, G = l[0], l[1]
    if(L != 0 and G != 0):
      i = 0
      stations = list()
      while i != G:
        l1 = inp.readline().strip()
        xi,ri = [ int(x) for x in l1.split() ]
        stations.append([xi - ri,xi + ri])
        i+=1
      ans = mic_wf(0,L,stations)
      if  ans == 0:
        print(-1)
      else:
        print(G-ans)

main()

