#Simplified Sudoku
#Erica Surcon - RPJ296 - 11363232 - CMPT145 - 02

#function w 1 input - file name
def simsudoku_checker(grid.txt):
  """
  Purpose: to verify the correctness of a simplified sudoku 
  Pre-conditions:
    grid.txt - a tabular file whose first line is the dimension of the sudoku board (should be a square so only one is needed) and the rest contain the sudoku board line by line, with the numbers eparate by spaces
  Post-conditions:
    console output detailing True or False to the question of if the simplified sudoku board is valid/correct
  Return: None
  """

  #setup
  #array module import
  import numpy as np
  #open file
  grid = open("grid.txt", "r")
  #initialize LoL + answer
  master = []
  correct = True
  
  #turn text file into list of lists of integers
  for l in grid:
    master.append([int(i) for i in l.split()])
  #initaializes n and removes from LoL
  n = master[0][0]
  del master [0]
  #create sudoku as array
  board = np.array(master)
  #create boolean array
  checklist = np.array(n/3,n/3)
  
  #verify values - iterate through 1-9 - if space already == True then failed
  for num in range(1,n+1):
    if correct == False:
      break
    for row in range(0,n,3):
      for column in range(0,n,3):
        if board[row][column] == num and checklist[row//3][column//3] == True:
          correct = False
        elif board[row][column] == num:
          checklist[row//3][column//3] == True
  
  #step4 - check if all values are true - if so print success
  
  #close file
  grid.close()
