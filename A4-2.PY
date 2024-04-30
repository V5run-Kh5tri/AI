import copy
ini=[[2,-1,3],[1,8,4],[7,6,5]]
goal=[[1,2,3],[8,-1,4],[7,6,5]]

def heuristic(state):
  count=0
  for i in range(len(state)):
    for j in range(len(state)):
      if state[i][j]!=goal[i][j]:
        count+=1
        if state[i][j]==-1:
          count-=1
  return count

print(heuristic(ini))

def generateBestState(curr):
  best=[]
  i=0
  j=0
  for m in range(len(curr)):
    for n in range(len(curr)):
      if curr[m][n]==-1:
        i=m
        j=n
        break
  if i>=0 and i<len(curr)-1:
    curr1=copy.deepcopy(curr)
    curr1[i][j],curr1[i+1][j]=curr1[i+1][j],curr1[i][j]
    best.append(curr1)
  if i<len(curr) and i>0:
    curr1=copy.deepcopy(curr)
    curr1[i][j],curr1[i-1][j]=curr1[i-1][j],curr1[i][j]
    best.append(curr1)
  if j>=0 and j<len(curr)-1:
    curr1=copy.deepcopy(curr)
    curr1[i][j],curr1[i][j+1]=curr1[i][j+1],curr1[i][j]
    best.append(curr1)
  if j<len(curr) and j>0:
    curr1=copy.deepcopy(curr)
    curr1[i][j],curr1[i][j-1]=curr1[i][j-1],curr1[i][j]
    best.append(curr1)
  best.sort(key=heuristic)
  return best

print(generateBestState(ini))

pq=[ini]
visited=[]
success=False
h=len(ini)**2
while success==False and len(pq)!=0:
  print('while loop')
  print(pq)
  curr=pq.pop(0)
  h=heuristic(curr)
  if heuristic(curr)==0:
    success=True
  else:
    print('elif')
    states=generateBestState(curr)
    visited.append(curr)
    print('visited ',visited)
    print('states generated',states)
    for state in states:
      if state not in visited and heuristic(state)<h:
        pq.append(state)
        h=heuristic(state)
        pq.sort(key=heuristic)
        print(pq)

if success:
  print('Found')
else:
  print('Not Found')