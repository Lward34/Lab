"""Prompts a user to perform histogram analysis and plots for
    select variables on datasets. the first dataset represents the population change
    for specific dates for U.S. regions.The second dataset represents Housing data \
    over an extended period of time describing home age, number of bedrooms, and other
    variables. The first row provides a column name for each dataset.
    References:
    “NumPy for MATLAB Users (2020).” NumPy for MATLAB Users - NumPy v1.20 Manual, 2020,
    http: numpy.org/doc/stable/user/numpy-for-matlab-users.html.

    Deitel, P., &amp; Deitel, H. (2021) Python for programmers.
    https://learning.oreilly.com/library/view/python-for-programmers/9780135231364/ch05.xhtml
    """

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np



def column_data(csv_file , variable_name):
    """loads the specific column from csv file
    Args:None
    Returns:None
    """
    column = csv_file[ variable_name ]
    return column


def calculate_statistics(column):
    """Calculates the count, mean,standard deviation,
    min,max of given data"""
    # Calculates the specific statistic
    column = np.array ( column ).flatten ( )
    count = column.shape[ 0 ]
    mean = np.mean ( column )
    std_dev = np.std_dev ( column )
    minimum = np.min ( column )
    maximum = np.max ( column )
    return count , mean , std_dev , minimum , maximum


def histogram_data(column, column_name, filepath):
    """function displays the Histogram"""
    plt.hist(column, density=True, bias=15)
    plt.ylabel(column_name)
    plt.show()
    if __name__ == "__main__":
        filepath = "~/Downloads/sample.csv"
    column_name = "AGE"
    histogram_data ( column, column_name, filepath)



def housing_age_data():
    """Function displays the Housing data over an extended period
    of time describing home age, number of bedrooms, and other variables"""
    # load Housing csv file and displays the Housing Data
    housing = pd.read_csv ( "Housing.csv" )
    pd.options.display.float_format = "{:,.3f}".format
    housing_age = housing[ [ "AGE" ] ]
    housing_age.hist ( bins = 50 , figsize = (20 , 15) )
    print ( "The Histogram of this column is now displayed" )
    plt.show ( )
    print ( housing_age.describe ( ) )


def housing_bedrms_data():
    """Function displays the Housing data over an extended period
    of time describing home age, number of bedrooms, and other variables"""
    # load Housing csv file and displays the Housing Data
    housing = pd.read_csv ( "Housing.csv" )
    pd.options.display.float_format = "{:,.3f}".format
    housing_bedrms = housing[ [ "BEDRMS" ] ]
    housing_bedrms.hist ( bins = 50 , figsize = (20 , 15) )
    print ( "The Histogram of this column is now displayed" )
    plt.show ( )
    print ( housing_bedrms.describe ( ) )


def housing_built_data():
    """Function displays the Housing data over an extended period
    of time describing home age, number of bedrooms, and other variables"""
    # load Housing csv file and displays the Housing Data
    housing = pd.read_csv ( "Housing.csv" )
    pd.options.display.float_format = "{:,.3f}".format
    housing_built = housing[ [ "BUILT" ] ]
    housing_built.hist ( bins = 50 , figsize = (20 , 15) )
    print ( "The Histogram of this column is now displayed" )
    plt.show ( )
    print ( housing_built.describe ( ) )


def housing_rooms_data():
    """Function displays the Housing data over an extended period
    of time describing home age, number of bedrooms, and other variables"""
    # load Housing csv file and displays the Housing Data
    housing = pd.read_csv ( "Housing.csv" )
    pd.options.display.float_format = "{:,.3f}".format
    housing_rooms = housing[ [ "ROOMS" ] ]
    housing_rooms.hist ( bins = 50 , figsize = (20 , 15) )
    print ( "The Histogram of this column is now displayed" )
    plt.show ( )
    print ( housing_rooms.describe ( ) )


def housing_utility_data():
    """Function displays the Housing data over an extended period
    of time describing home age, number of bedrooms, and other variables"""
    # load Housing csv file and displays the Housing Data
    housing = pd.read_csv ( "Housing.csv" )
    pd.options.display.float_format = "{:,.3f}".format
    housing_utility = housing[ [ "UTILITY" ] ]
    housing_utility.hist ( bins = 50 , figsize = (20 , 15) )
    print ( "The Histogram of this column is now displayed" )
    plt.show ( )
    print ( housing_utility.describe ( ) )


while True:
    print ( "************Welcome to the Python Data Analysis App************" )
    print ( 'Select the file you want to analyze:' )
    print ( '1. Population Data' )
    print ( '2. Housing Data' )
    print ( '3. Exit the program' )
    option = input ( )
    # checks the response and manages the options
    # Perform the operation for the selection1.
    if option == '1':
        print ( 'You have entered the Population Data.' )
        print ( 'Select the Column you want to analyze:' )
        print ( 'a.Pop April 1' )
        print ( 'b.Pop Jul 1' )
        print ( 'c.Change Pop' )
        print ( 'd.Exit Column' )
        choice = input ( )
        if choice == 'a':
            print ( 'You selected Pop Apr 1' )
            print ( 'The statistic for this column are:' )
            pop_df = pd.read_csv ( "PopChange.csv" )
            pd.options.display.float_format = "{:,.2f}".format
            pop_period = pop_df[ [ "Pop Apr 1" ] ].describe ( )
            print ( pop_period )
            pop_period.hist ( bins = 100 , figsize = (20 , 15) )
            # Displays histogram of all the selected columns
            print ( "The Histogram of this column is now displayed" )
            plt.show ( )
        if choice == 'b':
            print ( 'You selected Pop Jul 1' )
            print ( 'The statistic for this column are:' )
            pop = pd.read_csv ( "PopChange.csv" )
            pd.options.display.float_format = "{:,.2f}".format
            pop_period = pop[ [ "Pop Jul 1" ] ].describe ( )
            print ( pop_period )
            pop_period.hist ( bins = 100 , figsize = (20 , 15) )
            # Displays histogram of all the selected columns
            print ( "The Histogram of this column is now displayed" )
            plt.show ( )
        if choice == 'c':
            print ( 'You selected Change Pop' )
            print ( 'The statistic for this column are:' )
            pop = pd.read_csv ( "PopChange.csv" )
            pd.options.display.float_format = "{:,.2f}".format
            pop_change = pop[ [ "Change Pop" ] ].describe ( )
            print ( pop_change )
            pop_change.hist ( bins = 50 , figsize = (20 , 15) )
            # Displays histogram of all the selected columns
            print ( "The Histogram of this column is now displayed" )
            plt.show ( )
        if choice == 'd':
            print ( 'You selected to exit the column menu' )
        if choice not in ('a', 'b', 'c', 'd'):
            print('Invalid input. Please try again.')
    #Perform the operation for the selection2.
    elif option == '2':
        print ( 'You selected Housing Data' )
        print ( 'Select the column you want to analyze:' )
        print ( 'a.AGE' )
        print ( 'b.BEDRMS' )
        print ( 'c.BUILT' )
        print ( 'd.ROOMS' )
        print ( 'e.UTILITY' )
        print ( 'f.Exit Column' )
        choice = input ( )
        if choice == 'a':
            housing_age_data ( )
        if choice == 'b':
            housing_bedrms_data ( )
        if choice == 'c':
            housing_built_data ( )
        if choice == 'd':
            housing_rooms_data ( )
        if choice == 'e':
            housing_utility_data ( )
        if choice == 'f':
            print ( 'You selected to exit the column menu' )
        if choice not in ('a', 'b', 'c', 'd','e','f'):
            print('Invalid input. Please try again.')
    elif option == '3':
        print ( "************Thanks for using the Data Analysis App**************" )
        break
    # Checks for valid user input
    else:
        print ( "That is not a correct entry, please select 1-3" )
