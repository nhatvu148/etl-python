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


def when_to_eat(food_type):
    if food_type == 'fruit':
        return 'morning'
    elif food_type == 'veggie':
        return 'dinner'
    elif food_type == 'junk':
        return 'weekend'
    else:
        return 'no recommendation'


# use the function to populate a new column
df['when_to_eat'] = df['type'].map(when_to_eat)
print(df)


# write and apply a function that recommends eating junk food only
