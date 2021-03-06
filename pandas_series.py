import pandas as pd

grades = pd.Series([87,100,94])

print(grades)

same_grade = pd.Series(98.6, range(3))

print(same_grade)



print(grades[0])
grades.count()
grades.mean()
grades.min()
grades.max()
grades.std()

print(grades.describe())
#You can specify custom indices with the index keyword elements
grades = pd.Series([87,100,94], index=['Wally',"Eva",'Same'])

print(grades)

# If you initialize a Series with a dictionary, its keys become
# the Series' indices, and its values become the Series' element values:

grades = pd.Series({"Wally": 87, "Eva": 100, 'Same': 94})

# you can access individual elements via square brackets containing a 
# custom index value:
print(grades['Eva'])
#100

print(grades.Wally)

print(grades.dtype)

print(grades.values)

hardware = pd.Series(['Hammer', 'Saw', 'Wrench'])

''' 0 Hammer
    1 Saw
    2 Wrench
    dtype: object'''

answer = hardware.str.contains('a')

print(answer)

hardware_upper = hardware.str.upper()

print(hardware_upper)

