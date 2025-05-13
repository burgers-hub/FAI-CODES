# copy the code from below according to your need
# dont copy the commented(#)lines 
# ask ser to enter to numbers and perfform arithmatc operations

a = int(input("enter the first number : "))
b = int(input("enter the second number : "))

ans = a+b #change the sign to perform different operations
print(f"the sum of {a} and {b} is : {ans}")


#ask user for number and compare them for even or odd

a= int(input("enter the number : "))
if a%2==0:
    print(f"{a} is even number")
else:
    print(f"{a} is odd number")
    
#explore the numpy library
import numpy as np

a = np.array([1,2,3,4,5])
b = np.array([6,7,8,9,10])

c = np.add(a,b) #.subtract(a,b) #.multiply(a,b) #.divide(a,b) for different operations
print(f"the sum of {a} and {b} is : {c}")    

#explore the pandas library

import pandas as pd
data = {
    'name': ['John', 'Jane', 'Jim'],
    'age': [28, 34, 29],
    'city': ['New York', 'Los Angeles', 'Chicago']
}
dataframe = pd.DataFrame(data)
print(dataframe)

#write a numpy progaram to find maximum and minimum value of an array
import numpy as np
a = np.array([1,2,3,4,5])
max_value = np.max(a)
min_value = np.min(a)
print(f"the maximum value of {a} is : {max_value}")
print(f"the minimum value of {a} is : {min_value}")

#write a progrsm for dataaframe and perform add,update ,delete operations

# Import the pandas library
import pandas as pd

# Create the initial DataFrame
data = {
    'name': ['John', 'Jane', 'Jim'],
    'age': [28, 34, 29],
    'city': ['New York', 'Los Angeles', 'Chicago']
}
dataframe = pd.DataFrame(data)
print("Original DataFrame:")
print(dataframe)

# Add a new row
new_row = {'name': 'Jack', 'age': 25, 'city': 'San Francisco'}
dataframe = dataframe.append(new_row, ignore_index=True)
print("\nDataFrame after adding a new row:")
print(dataframe)

# Update a row (e.g., update Jim's age to 30)
dataframe.loc[dataframe['name'] == 'Jim', 'age'] = 30
print("\nDataFrame after updating Jim's age:")
print(dataframe)

# Delete a row (e.g., delete the row where name is 'Jane')
dataframe = dataframe[dataframe['name'] != 'Jane']
print("\nDataFrame after deleting Jane's row:")
print(dataframe)
