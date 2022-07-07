"""Prompts a user to enter their phone number and zip code+4.
    Then user will enter values of two, 3x3 matrix and then select from options
    of addition, subtraction,matrix multiplication,
    and element by element multiplications.
    *********
    Lilian Ward
    February 5, 2021
    SDEV300
    *********
    References:
    “NumPy for MATLAB Users (2020).” NumPy for MATLAB Users - NumPy v1.20 Manual, 2020,
    http: numpy.org/doc/stable/user/numpy-for-matlab-users.html.

    Deitel, P., &amp; Deitel, H. (2021) Python for programmers.
    https://learning.oreilly.com/library/view/python-for-programmers/9780135231364/ch05.xhtml
    """
import re
import numpy as np


print ("************Welcome to the Python Matrix Application************")
while True:
    print ("Do you want to play the matrix Game?")
    response = input ( "Enter Y for Yes or N for No:")
    if response == "N":
        print ("***********Thanks for playing Python Numpy************")
        break
    while response not in ['Y' , 'N']:
        print ('invalid input,please try again')
        break
    else:
        while True:
            #Prompts a user to enter their phone number
            Phone = input ("Enter your phone number(XXX-XXX-XXXX): ")
            # Regular expression for checking the phone number format
            if not re.match ( r'\d{3}-\d{3}-\d{4}' , Phone ):
                print ("Invalid phone number format. Please re-enter:")
            else:
                break
        while True:
            #Prompts the user to enter the zipcode+4.
            zipcode = input ("Enter your zipcode+4(XXXXX-XXXX): ")
            # Regular expression for checking the zipcode format
            if not re.match( r'\d{5}-\d{4}', zipcode ):
                print ("Invalid zipcode format. Please re-enter: ")
            else:
                break
        while True:
            try:
                # Prompts the user to enter the first matrix
                print ("Enter your first 3x3 matrix:")
                a = [ ]
                for i in range (3):
                    # Reading row by row
                    row = input ( ).split ( )
                    # Converting each element to integer
                    row = list (map(int , row))
                    # Adding row to the matrix
                    a.append (row)
                break
            except ValueError:
                print ("Invalid input, enter integer values")
            # Printing first matrix
        print ("Your first 3x3 matrix is:")
        for i in range (3):
            for j in range (3):
                print(a[i][j] , end = " ")
            print( )
        while True:
            try:
                # Prompts the user to enter the second matrix
                print ("Enter your second 3x3 matrix:")
                b = [ ]
                for i in range (3):
                # Reading row by row
                    row = input ( ).split ( )
                # Converting each element to integer
                    row = list (map(int , row ))
                # Adding row to the matrix
                    b.append (row)
                break
            except ValueError:
                print ("Invalid input, enter integer values")
            # Printing second matrix
        print ("Your second 3x3 matrix is:")
        for i in range (3):
            for j in range (3):
                print ( b[i][j] , end = " ")
            print( )
        # Menu for matrix operations
        print ("Select a Matrix Operation from the list below:")
        print ("a. Addition")
        print ("b. Subtraction")
        print ("c. Matrix Multiplication")
        print ("d. Element by element multiplication")
        choice = input( )
        # Addition of two 3x3 Matrix
        if choice == "a":
            print ( "You selected Addition. The results are:")
            # converting list to numpy arrays
            a = np.array (a)
            b = np.array (b)
            # addition of matrices
            c = a + b
            for i in range (3):
                for j in range (3):
                    print(c[i][j] , end = " ")
                print( )
            print ("The Transpose is:")
           # function for finding the transpose
            t = np.transpose (c)
            for i in range (3):
                for j in range (3):
                    print (t[i][j] , end = " ")
                print( )
            print ("The row and column mean values of the results are:")
            # Function mean with axis =1 finds row means
            print ("Row:" , np.mean ( c , axis = 1 ))
            # Function mean with axis =0 finds column means
            print ("Column:" , np.mean ( c , axis = 0 ))
        # Subtraction of two 3x3 Matrix
        if choice == "b":
            print ("You selected Subtraction. The results are:")
            a = np.array (a)
            b = np.array (b)
            # subtraction of matrices
            c = a - b
            for i in range (3):
                for j in range (3):
                    print ( c[i][j] , end = " ")
                print( )
            print ( "The Transpose is:" )
            # function for finding the transpose
            t = np.transpose (c)
            for i in range (3):
                for j in range (3):
                    print ( t[i][j] , end = " ")
                print( )
            print ("The row and column mean values of the results are:")
            # Function mean with axis =1 finds row means
            print ("Row:" , np.mean ( c , axis = 1 ))
            # Function mean with axis =0 finds column means
            print ("Column:" , np.mean ( c , axis = 0 ))
        # Multiplication of two 3x3 Matrix
        if choice == "c":
            print ("You selected Matrix Multiplication. The results are:")
            # For getting matrix multiplication use the function matrix instead of array in numpy
            c = np.matmul (a,b)
            for i in range (3):
                for j in range (3):
                    print ( c[i][j] , end = " ")
                print( )
            print ("The Transpose is:" )
            # function for finding the transpose
            c = np.transpose (c)
            for i in range (3):
                for j in range (3):
                    print ( c[i][j] , end = " ")
                print( )
            print ("The row and column mean values of the results are:")
            # Function mean with axis =1 finds row means
            print ("Row:" , np.mean ( c , axis = 1))
            # Function mean with axis =0 finds column means
            print ("Column:" , np.mean ( c , axis = 0))
        #Element by element multiplication of two 3x3 Matrix
        if choice == "d":
            print ("You selected Element by Element Multiplication. The results are:")
            a = np.array (a)
            b = np.array (b)
        # Elementary wise multiplication
            c = np.multiply (a , b)
            for i in range (3):
                for j in range (3):
                    print (c[i][j] , end = " ")
                print( )
            print ("The Transpose is:")
            # function for finding the transpose
            t = np.transpose (c)
            for i in range (3):
                for j in range (3):
                    print (t[i][j] , end = " ")
                print( )
            print ("The row and column mean values of the results are:")
            # Function mean with axis =1 finds row means
            print ("Row:" , np.mean ( c , axis = 1 ))
            # Function mean with axis =0 finds column means
            print ("Column:" , np.mean ( c , axis = 0 ))
