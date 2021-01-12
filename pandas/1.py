import numpy as np
import pandas as pd

s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
print(s)
print(s.index)

#Series can be instantiated from dicts
d = {'b': 1, 'a': 0, 'c': 2}
s2 = pd.Series(d)
print(s2)

input = {'Name':pd.Series(['John','Bran','Caret','Joha','Sam']),
   'Marks':pd.Series([44,48,75,33,99]),
   'Roll_num':pd.Series([1,2,3,4,5])
}
 
#Creating a DataFrame
data_frame = pd.DataFrame(input)
print(data_frame)
