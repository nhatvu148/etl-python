import pandas as pd
data = [
    [1, 'banana',  'sweet', 'fruit', 4.1],
    [2, 'orange',  'sweet', 'fruit', 4.3],
    [3, 'mango',   'sweet', 'fruit', 4.7],
    [4, 'lime',    'tart',  'fruit', 3.9],
    [5, 'lemon',   'tart',  'fruit', 3.5],
    [6, 'spinach', 'bland', 'veggie', 3],
    [7, 'lettuce', 'bland', 'veggie', 3.4],
    [8, 'pizza',   'tasty', 'junk', 4.5],
    [9, 'burger',  'tasty', 'junk', 4.7]
]

df = pd.DataFrame(data)
df.columns = ['food_id', 'food', 'profile', 'type', 'taste_score']
print(df.head())
print('\n\n')
print(df.dtypes)