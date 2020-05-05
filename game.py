def disp(game):
  for r in game:
    for c in r :
      print(c,end=" ")
    print("\n")


def move(game):
  player=int(input("Enter player number "))
  r=int(input("Enter row"))
  c=int(input("Enter column"))

  if game[r][c]!=0 :
    print("Invalid move......retry")
    
  else:
    game[r][c]=(1 if player==1 else 2)
    disp(game)
    
def check_win(game):
  #horizontal
  for r in game :
    if len(set(r))==1 and r[0]!=0:
      #print("the winner is player "+str(r[0])+" horizontally -- ")
      return int(r[0]) 

  #vertical
  
  for x in range(len(game)):
    v=[]
    for r in game:
      v.append(r[x])

    if len(set(v))==1 and v[0]!=0:
      #print("the winner is player "+str(v[0])+" vertically |")
      return int(v[0]) 
  
  #diagonal(\)
  v=[]  
  for x in range(len(game)) :
    v.append(game[x][x])


  if len(set(v))==1 and v[0]!=0:
    #print("the winner is player "+str(v[0])+" diagonally \\")
    return int(v[0]) 
    
    
    


  #diagonal(/)
  y=len(game)
  d=[]
  for x in range(y):
    d.append(game[x][y-x-1])
  if len(set(d))==1 and d[0]!=0:
    
    #print("the winner is player "+str(d[0])+" diagonally /")
    return int(d[0])


  return 0
  


  

if __name__== "__main__" :

  ans='y'
  while ans=='y':
    
    n=int(input("Enter the size of game"))
    game=[[0 for i in range(n)] for j in range(n)]

    m=0
    while 1 :
      move(game)
      m=m+1
      f=check_win(game)
      if f==1:
        print("WINNER IS PLAYER 1")
        break
      elif f==2:
        print("WINNER IS PLAYER 2")
        break
      elif m==n**2:
        print("IT IS A TIE ")
        break

  
    ans=input("DO YOU WANT TO CONTINUE")
    ans=ans.lower()  
    

  
  
  













  




    
