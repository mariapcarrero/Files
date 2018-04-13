#Estudiante: Maria Paula Carrero Rivas
#Trabajado con: Juan Fernando Escobar
#Codigo: 8911963

from sys import stdin
MAX =400
dictionary = None
letras, graph, total, orden = None,None,None,None
letricas = None
def toposort(ans, indeg, contador):
	global letras, orden, graph, total, letricas,listadeletras
	cand = list()
	cambio = [str(x) for x in range(len(ans)+1)]
	for u in (letricas):
		if indeg[u]==0: cand.append(u)
	anst = ans
	contador +=1
	for i in range(len(cand)):
		candidato = (cand.pop())
		anst = ans + letras[candidato]
		if contador == len(letras):
			print(anst)
		else:
			indegtemp =indeg[:]
			indegtemp[candidato] -= 1
			for v in graph[candidato]:
				indegtemp[v] -= 1
			toposort(anst, indegtemp, contador)


def main():
	global dictionary, letras, orden,graph, total, lista, letricas
	letras = [ str(x) for x in stdin.readline().split()]
	orden = [ str(x) for x in stdin.readline().split()]
	while len(letras)!= 0:
		graph = [ list() for x in range(len(letras))]
		indeg = [ 0 for i in range (len(letras)) ]
		total = list()
		letricas = [ int for x in range(len(letras))]
		dictionary = dict()
		letras.sort()
		for w in range( len(letras)):
			dictionary[letras[w]] = w
		i =0
		for i in range( len(letras)):
			letricas[i] = int(dictionary[letras[i]])
		i =0
		letricas.sort(reverse= True)
		while i <= len(orden)-2:
			u,v = orden[i], orden[i+1]
			uval, vval = dictionary[u], dictionary[v]
			indeg[vval] +=1
			graph[uval].append(vval)
			i+=2
		(toposort('',indeg,0))
		letras = [ str(x) for x in stdin.readline().split()]
		if len(letras) != 0:
			print('')
		if len(letras) != 0:
			orden = [ str(x) for x in stdin.readline().split()] 

main()