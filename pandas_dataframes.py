import pandas as pd

grades_dict = {'Wally': [87,96,70],
'Eva': [100,87,90],
'Sam': [94,77,90],
'Katie': [100,81,82],
'Bob': [83,65,85]}

print(grades_dict)

grades = pd.DataFrame(grades_dict)

print(grades)

grades.index = ['Test1', 'Test2', 'Test3']

#print(grades["Eva"])

#print(grades.Sam) 

#print(grades.loc['Test1'])

#print(gardes.iloc[1])

print(grades.loc['Test1':'Test3'])

print(grades.iloc[0:2])

print(grades.loc[['Test1','Test3']])

print(grades.iloc[0,2])

# View only Eva and Katie's grades for Test1 and Test2

print(grades.loc["Test1":'Test2', ['Eva','Katie']])

print(grades.iloc[0:1,[1,3]])

above_90 = grades[grades>90]

print(above_90)

b_grades = grades[(grades>=80) & (grades < 90)]

print(b_grades)

print(grades.at['Test1','Eva'])

print(grades.iat[1,2])

grades.at['Test2','Eva'] = 100

print(grades)


pd.set_option('precision', 2)
print(grades.describe())

print(grades.T.describe())

print(grades.T.mean())

grades.sort_index(ascending = False)

print(grades)

grades.sort_index(axis=1)

print(grades)

grades.T.sort_values(by='Test1', ascending=False)

print(grades)