[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

>> ```   
import random
import thinkstats2
import thinkplot
sample=[]
for i in range(1000):
    sample.append(random.random())   
pmf=thinkstats2.Pmf(sample)
cdf=thinkstats2.Cdf(sample)
thinkplot.Pmf(pmf)
thinkplot.show()
thinkplot.Cdf(cdf)
thinkplot.show()   
```
The distribution is close to uniform but not perfect.
