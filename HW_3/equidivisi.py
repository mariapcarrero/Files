from sys import stdin
#Estudiante: Maria Paula Carrero Rivas.
#Se usó el file de python para resolver Oil Deposits (DFS) que está en la página del profesor Camilo Rocha
#ID de estudiante: 8911963
grid,rows,cols = None,None,None
delta = [ (-1,0), (0,-1), (0,1), (1,0) ]

def dfs(visited, row, col):
  global grid,rows,cols,delta
  stack = [ (row, col) ] ; visited[row][col] = 1
  while len(stack)!=0:
    r,c = stack.pop()
    for dr,dc in delta:
      if 0<=r+dr<rows and 0<=c+dc<rows and visited[r+dr][c+dc]==0:
        if grid[r][c] == grid[r+dr][c+dc] and visited[r+dr][c+dc]==0:
          stack.append((r+dr,c+dc)) ; visited[r+dr][c+dc] = 1
      visited[r][c] = 2

def solve():
  ans = 0
  visited = [ [ 0 for c in range(rows) ] for r in range(rows) ]
  for r in range(rows):
    for c in range(rows):
       if visited[r][c]==0:
        ans += 1
        dfs(visited, r, c)
  return ans

def main():
  global grid,rows,cols
  rows = int(stdin.readline().strip())
  cols = rows
  while rows!=0:
    grid = [ [ rows for r in range(rows)] for c in range(rows)]
    listadePos = []
    for w in range(rows-1): 
      linea = stdin.readline().strip()
      listadePos = ([int(x) for x in linea.split() ])
      i = 0
      while i < len(listadePos)-1:
        valY = int(listadePos[i+1])-1
        valX = int(listadePos[i])-1
        grid[valX][valY] = w+1
        i +=2 #porque son parejas
    valor = solve()
    if valor != rows: print('wrong')
    else: print('good')
    rows = int(stdin.readline().strip())
    
main()
