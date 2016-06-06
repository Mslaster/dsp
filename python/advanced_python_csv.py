```
import csv
import pandas as pd

faculty=pd.read_csv('faculty.csv', index_col=0)

def emails(l):
    address_list=[]    
    for address in faculty[' email']:
        address_list.append(address)
    return address_list

fac_emails=emails(faculty)
    
a=open('emails.csv','w')
b=csv.writer(a)
for email in fac_emails:
    b.writerow([email])
a.close
```
