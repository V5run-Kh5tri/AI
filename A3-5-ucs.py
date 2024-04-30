from queue import PriorityQueue
graph=[[0,2,0,4,0,0,0],[2,0,4,5,0,0,8],[0,4,0,0,4,6,0],[5,5,0,2,0,0,1],[0,0,4,2,0,3,7],[0,0,6,0,3,0,3],[0,1,0,6,7,3,0]]
start=0
goal=6
pq=[]
pq.append([0,start])
visited={}
success=False
minCost=1000
while len(pq)!=0:
  print(pq)
  p=pq.pop(0)
  if p[1]==goal:
    if minCost>p[0]:
      minCost=p[0]
      print(minCost)
  else:
    if p[1] not in visited:
      for i in range(len(graph)):
        if graph[p[1]][i]!=0:
          pq.append([(p[0]+graph[p[1]][i]),i])
      visited[p[1]]=p[0]
      print(visited)
      pq.sort()
    else:
      if visited[p[1]]>p[0]:
        visited[p[1]]=p[0]
        print(visited)

print(minCost)


  