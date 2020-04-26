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
    
def check_win(game):
  #horizontal
  for r in game :
    if len(set(r))==1 and r[0]!=0:
      print("the winner is player "+str(r[0])+" horizontally -- ")
      return 'w'

  #vertical
  
  for x in range(len(game)):
    v=[]
    for r in game:
      v.append(r[x])

    if len(set(v))==1 and v[0]!=0:
      print("the winner is player "+str(v[0])+" vertically |")
      return 'w'
  
  #diagonal(\)
  v=[]  
  for x in range(len(game)) :
    v.append(game[x][x])


  if len(set(v))==1 and v[0]!=0:
    print("the winner is player "+str(v[0])+" diagonally \\")
    return ' w'
    
    
    


  #diagonal(/)
  y=len(game)
  d=[]
  for x in range(y):
    d.append(game[x][y-x-1])
  if len(set(d))==1 and d[0]!=0:
    
    print("the winner is player "+str(d[0])+" diagonally /")
    return 'w'  


  

if __name__==main :
  n=int(input("Enter the size of game"))
  game=[[0 for i in range(n)] for j in range(n)]
  
    

  
  
  













  




    
