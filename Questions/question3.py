""" Question 3: What can the relationships of the distribution of the board 
game "weights" from different decades tell us?

Expected Answer: We believe that the relationships of the normal distributions 
of the weights of board games through certain periods of time would shift to being 
"easier" from the start as more board games are being developed, then start 
spreading out to different complexity levels as the board game space gets more 
diverse over time (and is suitable for harder and more complex games) """

import pandas as pd
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt


file_path = '../boardgames1.csv'

data_df = pd.read_csv(file_path)

uniq_years = data_df['yearpublished'].unique()
print(uniq_years)
print(max(uniq_years))
print(min(uniq_years))
bc_weights = data_df.loc[data_df['yearpublished']<=0,'avgweight']
firsts_weights = data_df.loc[data_df['yearpublished'].between(1,1500),'avgweight']
seconds_weights = data_df.loc[data_df['yearpublished'].between(1501,1899),'avgweight']
nineteentens_weights = data_df.loc[data_df['yearpublished'].between(1900,1909),'avgweight']
twenties_weights = data_df.loc[data_df['yearpublished'].between(1920,1929),'avgweight']
thirties_weights = data_df.loc[data_df['yearpublished'].between(1930,1939),'avgweight']
fourties_weights = data_df.loc[data_df['yearpublished'].between(1900,1909),'avgweight']
fifties_weights = data_df.loc[data_df['yearpublished'].between(1950,1959),'avgweight']
sixties_weights = data_df.loc[data_df['yearpublished'].between(1960,1969),'avgweight']
seventies_weights = data_df.loc[data_df['yearpublished'].between(1970,1979),'avgweight']
eighties_weights = data_df.loc[data_df['yearpublished'].between(1980,1989),'avgweight']
nineties_weights = data_df.loc[data_df['yearpublished'].between(1990,1999),'avgweight']
twotousands_weights = data_df.loc[data_df['yearpublished'].between(2000,2009),'avgweight']
twentytens_weights = data_df.loc[data_df['yearpublished'].between(2010,2019),'avgweight']
twentytenties_weights = data_df.loc[data_df['yearpublished']>2020,'avgweight']

print(bc_weights)
print(firsts_weights)
print(seconds_weights)

weight_u = data_df['avgweight'].mean
weight_std = data_df['avgweight'].std
"""
print(weight_u)
print(weight_std)

x= np.linspace(start=0, stop=5, num=20000)
y= norm.pdf(x, loc=weight_u, scale=weight_std)

plt.plot(x,y,label='Fitted Normal')
plt.title('Fitted Normal Distribution for Board Game Weights')
plt.xlabel('X')
plt.ylabel('Probability Density')
plt.show()
"""
