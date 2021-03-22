import pandas as pd
import numpy as np

'Perform the following tasks with pandas Series:'
'Create a Series from the list [7, 11, 13, 17].'
l = [7,11,13,17]
x = pd.Series(l)
print(x)

'Create a Series with five elements that are all 100.0.'
x = pd.Series(100.0)
x = x.repeat(5)
print(x)

'Create a Series with 20 elements that are all random numbers in the range 0 to 100. Use method describe to produce the Series’ basic descriptive statistics.'
x = pd.Series(np.random.randint(0,100,20))
x.describe()
print(x)

"Create a Series called temperatures of the floating-point values 98.6, 98.9, 100.2 and 97.9. Using the index keyword argument, specify the custom indices 'Julie', 'Charlie', 'Sam' and 'Andrea'."
temperatures = pd.Series([98.6,98.9,100.2,97.9],index = ['Julie','Charlie','Sam','Andrea'])
print(temperatures)

'Form a dictionary from the names and values in Part (4), then use it to initialize a Series.'
dic = {'Julie':98.6,'Charlie':98.9,'Sam':100.2,'Andrea':97.9}
x = pd.Series(dic)
print(x)
