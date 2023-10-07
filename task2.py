# Data frames
import pandas as pd
import random

import scipy.stats as ss
from scipy.stats.contingency import crosstab

coffee_chocolate = [['Coffee','Chocolate']]*43
coffee_plain = [['Coffee','Plain']]*57
tea_chocolate = [['Tea','Chocolate']]*56
tea_plain = [['Tea','Chocolate']]*56

raw_data = coffee_chocolate + coffee_plain + tea_chocolate + tea_plain
#shuffle the data
random.shuffle(raw_data)
# Zip the list - make the rows columns and the columns rows
# Interchange the outer and inner lists
drink, biscuit = list(zip(*raw_data))  #2 lists, one with Grnder and 1 with medium.

# create a data frame
df = pd.DataFrame({'drink': drink, 'biscuit': biscuit})

df

# Perform Crosstabs Contingency.

cross = ss.contingency.crosstab(df['drink'], df['biscuit'])
# Show.
cross

cross.elements(df)