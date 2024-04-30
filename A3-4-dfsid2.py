import copy
s=[['A'],['C','B'],[]]
g=[['C','B','A'],[],[]]
max_depth=3
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

#def dfid(s,g,open,closed):
for depth in range(1,max_depth+1):
  open=[s]
  closed=[]
  i=0
  while success==False and len(open)!=0:
    print('while loop')
    current=open.pop()
    i+=1
    print(current)
    closed.append(current)
    if g==current:
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
    print('Found at depth ',depth)
  else:
    print('Not Found at depth ',depth)






