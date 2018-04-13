def toposort(G, indeg):
  ans,cand = list(),list()
  for u in range(len(indeg)):
    if indeg[u]==0: cand.append(u)
  while len(cand)!=0:
    ans.append(cand.pop())
    for v in G[ans[-1]]:
      indeg[v] -= 1
      if indeg[v]==0: cand.append(v)
  return (len(ans)==len(indeg), ans)