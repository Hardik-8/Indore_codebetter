import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

df=pd.dataframe({'day':['monday','tuesday','wednesday','thursday','friday','saturday','sunday'],
                'sales':[100,200,300,400,500,600,700]})
df.plot(kind='line')
plt.show()