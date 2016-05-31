# Hint:  use Google to find python function

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'   

####b)  
date_start = '12312013'  
date_stop = '05282015'  

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  

```from datetime import datetime

def days_elapsed(start_date,end_date,date_format):
    start = datetime.strptime(start_date, date_format)
    stop = datetime.strptime(end_date, date_format)
    delta=stop-start
    return delta.days
    
dates=[('01-02-2013','07-28-2015','%m-%d-%Y'),('12312013','05282015','%m%d%Y'),('15-Jan-1994','14-Jul-2015','%d-%b-%Y')]

for vals in dates:
    print days_elapsed(*vals)```
