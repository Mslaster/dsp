[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

>>    
```   
import math                                   
import nsfg
df = nsfg.ReadFemPreg()   
firsts=df[df.birthord==1]   
others=df[df.birthord>1]   
firsts_wgt=firsts.totalwgt_lb
others_wgt=others.totalwgt_lb   
def Cohens_Effect_Size(a,b):
    diff=a.mean()-b.mean()   
    var1=a.var()
    var2=b.var()
    n1,n2=len(a),len(b)
    pooled_var= (n1*var1+n2*var2)/(n1+n2)
    d=diff/math.sqrt(pooled_var)
    return d   
print Cohens_Effect_Size(firsts_wgt,others_wgt)
```   
Cohens D effect is -.088673, which is more significant than the difference in pregnancy length  
