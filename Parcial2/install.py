#Estudiante: Maria Paula Carrero Rivas
#Trabajado con: Juan Fernando Escobar y Juan Sebastian Rivera
# mic fue tomado de la página del profesor, pero fue modificado sin usar L,H

from sys import stdin
import math
a = list()

def distance(x,y):
    ans = math.sqrt((x * x) - (y * y))
    return ans

def mic():
  global a
  a.sort(key=lambda x: x[1]) #ordeno por y
  n,N, contador = 0,len(a), 1
  while n!=N:
    best,n = n,n+1
    while n!=N:
      if a[n][0]>a[best][1]:
        best = n
        contador+=1
      n += 1
  return contador


def main():
	global a
	n, d = float('-inf'), float('-inf')
	n, d = [int(w) for w in stdin.readline().strip().split()]
	case = 1
	while n!=0 and d!=0:
	    a = list()
	    i, bandera = 0,0        
	    while i != n:
	        l = stdin.readline().strip()
	        x,y = [int(w) for w in l.split()]
	        if y > d:
	        	bandera = 1
	        if bandera == 0:
	        	valor = distance(d, y)
	        	izq, der = x - valor, x + valor
	        	a.append([izq, der, i])
	        i+=1
	    if bandera == 0: print('Case {0}: {1}'.format(case,mic()))
	    else: print('Case {0}: {1}'.format(case,-1))
	    case += 1
	    line = stdin.readline()
	    n, d = [int(w) for w in stdin.readline().strip().split()]

main()