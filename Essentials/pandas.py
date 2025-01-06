import pandas as pd
df = pd.read_csv('dta.csv')

df.fillna(0, inplace=true) # replaces null data with 0
df.drop_duplicates(inplace=true) #removes duplicates 

print("Total:", df['Sales'].sum())
print("Average:", df['Sales'].mean())