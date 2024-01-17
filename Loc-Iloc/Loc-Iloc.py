import pandas as pd

df = pd.DataFrame({'Day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
                   'Weather': ['Sunny', 'Sunny', 'Sunny', 'Sunny', 'Cloudy', 'Shower', 'Shower'],
                   'Temperature': [12.45, 13.34, 18.00, 15.00, 8.00, 5.00, 5.54],
                   'Wind': [11, 12, 12, 13, 15, 16, 11],
                   'Humidity': [24, 26, 36, 50, 26, 35, 24]}).set_index('Day')


#Selecting a single value
print(df.loc['Tue', 'Temperature'])
print(df.iloc[1, 1])

#Selectig all rows of a specific column
print(df.loc[:, 'Temperature'])
print(df.iloc[:, 1])

#Selecting all columns of a specific row
print(df.loc['Mon', :])
print(df.iloc[0, :])

#selcting list of values
print(df.loc[['Mon', 'Tue'], 'Wind'])
print(df.iloc[[0, 1], 2])
print(df.loc['Thu', ['Temperature', 'Wind']])
print(df.iloc[3, [1, 2]])

#Slicing
print(df.loc['Mon':'Sun', 'Weather'])
print(df.iloc[0:7, 0])
print(df.loc['Mon', 'Weather':'Humidity'])
print(df.iloc[0, 0:4])
print(df.loc['Mon':'Fri':2, :])
print(df.iloc[0:5:2, :])

#Conditions and callable
print(df.loc[df['Temperature'] > 8.00, 'Weather':'Wind'])
print(df.loc[(df['Temperature'] > 8.00) & (df['Wind'] > 11), :])
print(df.iloc[list(df['Temperature'] > 8.00), 'Weather':'Wind'])
#Iloc doesn't accept boolean Series. I can use list to convert a Series into a boolean list
print(df.iloc[list((df['Temperature'] > 8.00) & (df['Wind'] > 11)), :])

print(df.loc[:, lambda df: ['Temperature', 'Wind']])
print(df.loc[lambda df: df['Temperature'] > 8.00, 'Weather':'Wind'])
print(df.iloc[:, lambda df: [1, 2]])
print(df.iloc[lambda df: list(df['Temperature'] > 8.00), 0:3])
