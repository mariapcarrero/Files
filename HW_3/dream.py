#Estudiante: Maria Paula Carrero Rivas
#Trabajado con: Juan Fernando Escobar y Juan Sebastian Rivera

from sys import stdin
MAX = 10000
dream = [ None for i in range(MAX) ]

def solve():
	global dream
	N = len(dream)
	n, suma, ceros = 0, 0, 3
	while (n != N):
		if dream[n] == '?':
			dream[n] = '0'
		if dream[n] == '1':
			if ceros == 3:
				ceros = 0
			else:
				ceros -= 1
		elif dream[n] == '0':
			if ceros == 3:
				suma += 1
			else:
				ceros += 1
		if ceros == 2:
			ceros = 3
			suma += 1
		n += 1
	if ceros == 3:
		return suma
	else:
		return 0


def main():
  global dream
  inp = stdin
  l = stdin.readline().strip()
  while len(l)>0:
    dream = list(l);
    if (len(dream) != 0):
      print(solve())
    else:
      print(0)
    l = stdin.readline().strip()

main()
