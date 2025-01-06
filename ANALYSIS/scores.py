import numpy as np 
import pandas as pd 

df = pd.read_csv(r'C:\Users\asus\Test\ANALYSIS\scores.csv')  
data = df.values  #convert to numpy array


max_scores = np.max(data, axis=0)
min_scores = np.min(data, axis=0)


print(f"Max scores:  {max_scores}")
print(f"Min scores:  {min_scores}")