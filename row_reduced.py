import numpy as np
#Imports NumPy library

def row_swap(m, i, j) :
  """
  Swap rows i and j of matrix m.
  """
  mp = m.copy() # make a copy of the input matrix
  t = mp[i,:].copy() # copy row i of mp, need to copy since next line changes mp
  mp[i,:] = mp[j,:] # copy row j of mp into row i
  mp[j,:] = t # put the copy of the original row i into row j
  return mp
#row_swap performs the operation in Guassian elimination known as "row swapping,"
#where two rows of an augmented matrix are switched.

def scalar_mult(m, i, c) :
  """
  Multiply row i of matrix m by c.
  """
  mp = m.copy() # make a copy of the input matrix
  mp[i,:] = c*mp[i,:] # multiply row i by c and put it back into row i
  return mp
#scalar_mult performs the operation in Guassian elimination known as "scalar multiplication,"
#where a row of values in an augmented matrix are multiplied by a chosen scalar.

def row_add(m, i, j, c) :
  """
  Multiply row i of matrix m by c, add to row j, and replace row j.
  """
  mp = m.copy() # make a copy of the input matrix
  mp[j,:] = c*mp[i,:]+mp[j,:] # multiply row i by c, add to row j, and put sum back into row j
  return mp
#row_add performs the operation in Guassian elimination known as "row addition,"
#where one chosen row is multiplied by a chosen scalar (c) and then added to another
#row in the augmented matrix.

def row_reduced(a,b,c,d,e,f):
    m = np.array([[a,b,c],[d,e,f]])
    #Here, the user will use the definition and 
    
    print('initial matrix')
    print(m)
    #Prints what was originally defined as "m" - the matrix to be worked on.
    
    if m[0,0] == 0.0:
        print('Performing a row swap on rows 0 and 1.')
        m = row_swap(m,0,1)
        print(m)   
        #This checks to see if the top-left element of the matrix is a non-zero element.
        #This is the first step of the Gaussian elimination algorithm.
        
    if m[0,0] != 1.0:
        print('Performing a scalar multiplication')
        print('Multiplying it by a factor of '+str(1/m[0,0])+'.')
        m = scalar_mult(m,0,(1/m[0,0]))
        print(m)
        #This checks if the top-left element is equal to one. If it isn't , it will
        #multiply that row by a scalar number so that it will become one.
        
    if m[1,0] != 0.0:
        print('Performing a row add on Row 1 with Row 0')
        m = row_add(m,0,1,(-m[1,0]))
        print(m)
        #This check to see if the bottom left element is equal to zero. If not,
        #It will be subtracted by the first row (which is multiplied by a scalar
        #that is opposite by equal to the bottom left element). This is to ensure
        #The first column will result in [1,0].
        
    if m[1,1] != 1.0:
        print('Performing a scalar multiplication on Row 1')
        print('multiplying Row 1 by a factor of '+str(m[1,1])+'.')
        m = scalar_mult(m,1,(1/m[1,1]))
        print(m)
        #This checks to see if the bottom-middle element is equal to one. If not,
        #the row will be multiplied by a scalar that will turn that element to one.
    if m[0,1] != 0.0:
        print('Performing a row addition on Row 0 with Row 1')
        m = row_add(m,1,0,(-m[0,1]))
        print(m)
        #This checks to see if the top-middle element is equal to zero. If not, the
        #row will be subtracted by the bottom row (which is multiplied by a scalar
        #that is opposite but equal to the top-middle element).
    
    if (m[0,0] == 1.0) and (m[1,1] == 1.0):
        print('This is the final matrix!')
        print(m)
        print('The answer to this matrix is x = '+str(m[0,2])+' and y = '+str(m[1,2])+'.')
        #Finally, this last loop will check to see if the matrix is row reduced,
        #or that the top-left and bottom-middle elements are equal to one. If they
        #(which the should be, from our previous loops), the program will print what
        #what the results for the matrix are in an x,y format.