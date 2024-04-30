import copy

ini=[[[2,-1,3],[1,8,4],[7,6,5]],0]
goal=[[1,2,3],[8,-1,4],[7,6,5]]

def heuristic(state):
  count=0
  for i in range(len(state[0])):
    for j in range(len(state[0])):
      if state[0][i][j]==goal[i][j]:
        count+=1
        if state[0][i][j]==-1:
          count-=1
  return count

print(heuristic(ini))

def evale(curr):
  return heuristic(curr)+curr[1]

def generateBestState(curr):
  best=[]
  i=0
  j=0
  for m in range(len(curr[0])):
    for n in range(len(curr[0])):
      if curr[0][m][n]==-1:
        i=m
        j=n
        break
  if i>=0 and i<len(curr[0])-1:
    curr1=copy.deepcopy(curr[0])
    curr1[i][j],curr1[i+1][j]=curr1[i+1][j],curr1[i][j]
    best.append([curr1,curr[1]+1])
  if i<len(curr[0]) and i>0:
    curr1=copy.deepcopy(curr[0])
    curr1[i][j],curr1[i-1][j]=curr1[i-1][j],curr1[i][j]
    best.append([curr1,curr[1]+1])
  if j>=0 and j<len(curr[0])-1:
    curr1=copy.deepcopy(curr[0])
    curr1[i][j],curr1[i][j+1]=curr1[i][j+1],curr1[i][j]
    best.append([curr1,curr[1]+1])
  if j<len(curr[0]) and j>0:
    curr1=copy.deepcopy(curr[0])
    curr1[i][j],curr1[i][j-1]=curr1[i][j-1],curr1[i][j]
    best.append([curr1,curr[1]+1])
  best.sort(key=evale,reverse=True)
  return best

print(generateBestState([[[2, 8, 3], [1, -1, 4], [7, 6, 5]], 1]))
print(evale([[[1, 2, 3], [-1, 8, 4], [7, 6, 5]], 2]))
print("Heloololololollo")


pq=[ini]
visited=[]
success=False
while success==False and len(pq)!=0:
  print('while loop')
  print(pq)
  curr=pq.pop(0)
  if curr[0]==goal:
    success=True
  else:
    print('else')
    states=generateBestState(curr)
    visited.append(curr[0])
    print('visited ',visited)
    print('states generated',states)
    for state in states:
      if state[0] not in visited:
        print('not in visited')
        pq.append(state)
        pq.sort(key=evale,reverse=True)
        # print(pq)

if success:
  print('Found')
else:
  print('Not Found')