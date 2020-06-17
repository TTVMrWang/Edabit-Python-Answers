def game_of_life(board):
  w=len(board[0])+2
  h=len(board)+2
  board = [[0]*w] + [[0]+row+[0] for row in board] + [[0]*w]
  ans=''
  for i in range(1, h-1):
      for j in range(1, w-1):
          active = sum(board[i+di][j+dj] for di in (-1,0,1) for dj in (-1,0,1) if di or dj)
          ans += "_I"[3 - board[i][j] <= active <= 3]
      ans += '\n'
  return ans[:-1]
