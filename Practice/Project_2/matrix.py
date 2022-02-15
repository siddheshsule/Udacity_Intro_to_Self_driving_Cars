from ast import Pass
import math
from math import sqrt
import numbers
import re
import numpy as np

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

def get_row(matrix, row):
    return matrix[row]

def get_column(matrix, column_number):
    column = []
    for r in range(len(matrix)):
        column.append(matrix[r][column_number])

    return column

def dot_product(vector_one, vector_two):
    result = 0
    
    for i in range(len(vector_one)):
        result += vector_one[i] * vector_two[i]

    return result

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid # grid == matrix
        self.h = len(grid) # No. of rows in the grid
        self.w = len(grid[0]) # No. of columns in the grid

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # TODO - your code here
        if self.h == 1:
            return self[0][0]
        else:
            return (self.g[0][0] * self.g[1][1]) - (self.g[1][0] * self.g[0][1])      # Passed  
     

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        # TODO - your code here
        result = 0
        for r in range(self.h):
            for c in range(self.w):
                if r == c:
                    result += self.g[r][c]
        
        return result   # Passed  

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        # TODO - your code here        
        inverse = []    
      
    
        # Check if matrix is 1x1 or 2x2.
        # Depending on the matrix size, the formula for calculating
        # the inverse is different. 
        if self.h == 1:
            inverse.append([1 / self.g[0][0]])
        elif self.h == 2:
        # If the matrix is 2x2, check that the matrix is invertible
            if self.g[0][0] * self.g[1][1] == self.g[0][1] * self.g[1][0]:
                raise ValueError('The matrix is not invertible.')
            else:
                # Calculate the inverse of the square 1x1 or 2x2 matrix.
                a = self.g[0][0]
                b = self.g[0][1]
                c = self.g[1][0]
                d = self.g[1][1]

                factor = 1 / (a * d - b * c)

                inverse = [[d, -b],[-c, a]]

                for i in range(len(inverse)):
                    for j in range(len(inverse[0])):
                        inverse[i][j] = factor * inverse[i][j]
    
        return Matrix(inverse) # PAssed

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        matrix_transpose = []
        # Loop through columns on outside loop
        for c in range(self.w):
            new_row = []
        # Loop through columns on inner loop
            for r in range(self.h):
            # Column values will be filled by what were each row before
                new_row.append(self.g[r][c])
            matrix_transpose.append(new_row)
    
        return Matrix(matrix_transpose)  # Passed

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        #   
        # TODO - your code here
            # initialize matrix to hold the results
        matrixSum = []

        # --matrix to hold a row for appending sums of each element
        row = []
        result =[]
        for r in range(self.h):
            row = [] # reset the list
            for c in range(self.w):
                row.append(self.g[r][c] + other.g[r][c]) # add the matrices
            matrixSum.append(row)
        result = matrixSum
        return Matrix(result)   # Passed
        

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
        # TODO - your code here
                
        result = []
                
        for i in range(self.h):
            row = []
            
            for j in range(self.w):
                temp = (-1) * self.g[i][j]
                row.append(temp)
            result.append(row)                 
        return Matrix(result) # Passed
        


    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        #   
        # TODO - your code here
        matrixSub = []

        # matrix to hold a row for appending sums of each element
        row = []
        for i in range(self.h):
            row = []
            new_row = []
            for j in range(self.w):
                sr_ij = self.g[i][j] - other.g[i][j]
                new_row.append(sr_ij)
            matrixSub.append(new_row)

        return Matrix(matrixSub)  #PAssed
         

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #   
        # TODO - your code here
        # def matrix_multiplication(matrixA, matrixB):
            
        # Store the number of rows in A and the number of columns in B.
        # This will be the size of the output matrix
        m_rows = len(self.g)
        p_columns = len(other.g[0])
        
        # empty list that will hold the product of AxB
        result = []

        
        # For loop within a for loop. The outside for loop will 
        # iterate through m_rows. The inside for loop will iterate 
        # through p_columns.
        for r in range(m_rows):
            # Accumulate the values of a row (reset each loop)
            row_result = []
            # Grab current A row
            rowA = get_row(self.g, r)
            
            for c in range(p_columns):
                # Grab current B column
                colB = get_column(other.g, c)
                # Calculate the dot product of the A row and the B column
                dot_prod = dot_product(rowA, colB)
                # And append to row_result
                row_result.append(dot_prod)
        
            # Add the row_result to the result matrix
            result.append(row_result)

        return Matrix(result)

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            pass
            #   
            # TODO - your code here
            result = []
                    
            for i in range(self.h):
                row = []
                new_row = []
                for j in range(self.w):
                    temp = other * self.g[i][j]
                    row.append(temp)
                result.append(row)                 
            return Matrix(result) # Passed
    
    
    