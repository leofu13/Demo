import pandas as pd

data = {'Name': ['Arabica', 'Robusta', 'Liberica'],
        'Origin': ['SouthAmerica', 'Africa', 'SEA'],
        'Score': [8, 7, 9] 
        }

df = pd.DataFrame(data)
Score = df['Score'].mean()

print("MeanScore:", Score)
print(df)

