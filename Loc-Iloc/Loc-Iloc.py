import pandas as pd

df = pd.DataFrame({'Day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
                   'Weather': ['Sunny', 'Sunny', 'Sunny', 'Sunny', 'Cloudy', 'Shower', 'Shower'],
                   'Temperature': [12.45, 13.34, 18.00, 15.00, 8.00, 5.00, 5.54],
                   'Wind': [11, 12, 12, 13, 15, 16, 11],
                   'Humidity': [24, 26, 36, 50, 26, 35, 24]}).set_index('Day')


print(df)
