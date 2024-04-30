import copy
s=[['A'],['C','B'],[]]
g=[[],['C','B','A'],[]]
open=[]
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

#def dfsid(s,g,open,closed):
open1=[s]
j=0
while success==False and open1!=open:
  print('2nd while')
  open=copy.deepcopy(open1)
  print(open)
  open1=[s]
  j+=1
  i=0
  while success==False and len(open1)!=0:
    print('while loop')
    current=open1.pop()
    i+=1
    print(current)
    closed.append(current)
    if g==current:
      success=True
    elif i<=j:
      print('else')
      states=generateMoves(current)
      print('moves generated:',states)
      for state in states:
        if state not in open1 and state not in closed:
          open1.append(state)
          print(open1)


if success:
  print('Found')
else:
  print('Not Found')



