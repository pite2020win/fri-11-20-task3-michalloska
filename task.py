#Matrix. 


#Write a class that can represent any 4𝑥4 real matrix. 
#Include two functions to calculate the sum and dot product of two matrices. 
#Next, write a program that imports this library module and use it to perform calculations.
# You CAN'T use numpy.
#Examples:
#
# matrix_1 = Matrix(4.,5.,6.,7.)
# matrix_2 = Matrix(2.,2.,2.,1.)
#
# matrix_3 = matrix_2 @ matrix_1
# matrix_4 = matrix_2 + matrix_1
# matrix_4 = 6 + matrix_1
# matrix_4 = matrix_1 + 6
#
# expand your solution to include other operations like
# - subtraction 
# - inversion
# - string representation 
#
#Try to expand your implementation as best as you can. 
#Think of as many features as you can, and try implementing them.
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)
#Delete these comments before commit!
#
#Good luck.
import logging 

class matrix_2x2:

  def __init__(self, data = "None", width = 2, height = 2):
    self.width = width
    self.height = height
    self.Matrix = [[0 for i in range(self.width)] for j in range(self.height)]
    if data != "None":
      for i in range(self.width):
        for j in range(self.height):
          self.Matrix[i][j] = data[i][j]


  def displayMatrix(self):
    logging.info("Displaying a Matrix:")
    for i in range(self.width):
      for j in range(self.height):
        print("{} ".format(self.Matrix[i][j]), end='')
      print("\n")

def add_matrices(matrix1, matrix2):
  pass

if __name__ == "__main__":
  logging.basicConfig(level=logging.DEBUG)

  filledMatrix1 = matrix_2x2([[1,2],[3,4]])
  filledMatrix2 = matrix_2x2([[4,3],[2,1]])
  emptyMatrix = matrix_2x2()
  filledMatrix1.displayMatrix()
  filledMatrix2.displayMatrix()
  emptyMatrix.displayMatrix()

  sum_product = add_matrices(filledMatrix1, filledMatrix2)