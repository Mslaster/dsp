[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

>>```    
import scipy.stats
def to_metric(inches):
    return inches*2.54
min_h=to_metric(70)
max_h=to_metric(73)
bmg=scipy.stats.norm.cdf(max_h, loc=178 ,scale=7.7 )-scipy.stats.norm.cdf(min_h,loc=178,scale=7.7)
print bmg
```
Approximately 34% of the US male population can qualify for the Blue Men Group.
