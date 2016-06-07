
```
import csv
import pandas as pd

faculty=pd.read_csv('faculty.csv', index_col=0)
# 
faculty_dict={}
for name in faculty.index:    
    if name.split()[-1] not in faculty_dict.keys():    
        faculty_dict[name.split()[-1]]=[[faculty[' degree'][name], faculty[' title'][name], faculty[' email'][name]]]
    else:
       faculty_dict[name.split()[-1]].append([faculty[' degree'][name], faculty[' title'][name], faculty[' email'][name]])  
  ```
