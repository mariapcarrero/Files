#Estudiante: Maria Paula Carrero Rivas
#Trabajado con: Juan Fernando Escobar y Juan Sebastian Quiceno

from sys import stdin

def solve(L,U,N, maxval):
    M =''
    i = 32 - maxval
    flagL, flagU = 1,1
    while i != 32:
        if N[i] == '1' :
            if L[i] == '1' and flagL == 1:
                M += '1'
            else: 
                M+= '0'
                if U[i] == '1': flagU = 0
        else:
            if U[i] == '0' and flagU == 1:
                M += '0'
            else: 
                M += '1'
                if L[i] == '0': flagL = 0
        i+=1
    return M

def main():
    line = stdin.readline().strip()
    while len(line)!=0:
        N,L,U = line.split()
        N=bin(int(N))[2:]
        L=bin(int(L))[2:]
        U=bin(int(U))[2:]
        maxval = max(len(N), len (L), len(U))
        N=N.zfill(32)
        L=L.zfill(32)
        U=U.zfill(32)
        answer =(solve(L,U,N, maxval))
        print(int(answer,2))
        line = stdin.readline().strip()

main()