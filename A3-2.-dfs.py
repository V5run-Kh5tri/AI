import copy
s=[['A'],['C','B'],[]]
g=[['C'],['A','B'],[]]
open=[s]
closed=[]
success=False

def generateMoves(s):
  states=[]
  for i in range(len(s)):
    #print(i)
    if (len(s[i])!=0):
     #print('hi')
      for j in range(len(s)):
        if j!=i:
          s1=copy.deepcopy(s)
          x=s1[i].pop(0)
          s1[j].insert(0,x)
          states.append(s1)
        else:
          continue
  return states

#def dfs(s,g,open,closed,):
while success==False and len(open)!=0:
  print('while loop')
  current=open.pop()
  print(current)
  closed.append(current)
  if g==current:
    success=True
  else:
    print('else')
    states=generateMoves(current)
    print('moves generated:',states)
    for state in states:
      if state not in open and state not in closed:
        open.append(state)
        print(open)

if success:
  print('Found')
else:
  print('Not Found')



