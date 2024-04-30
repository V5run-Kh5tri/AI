import copy
s=[['A'],['C','B'],[]]
g=['C','B','A']
depth=1
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

#def dls(s,g,open,closed):
i=0
while success==False and len(open)!=0:
  print('while loop')
  current=open.pop()
  i+=1
  print(current)
  closed.append(current)
  if g in current:
    success=True
  elif i<=depth:
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



