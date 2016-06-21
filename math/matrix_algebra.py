# Matrix Algebra

1.1) dim(A)=2x3  
1.2) dim(B)=2x2
1.3) dim(C)=3x2
1.4) dim(D)=2x3
1.5) dim(u)=1x4
1.6) dim(w)=4x1

2.1) u+v=[9,7,-4,9]
2.2) u-v=[3,-3,-2,1]
2.3) 6u=[36,12,-18,30]
2.4) u.v=51
2.5) |u|=sqrt(74)

3.1) A+C="not defined"
3.2) A-C^T=[[-4,-7,-3],[3,6,4]]
3.3) C^T+3D=[[14,3,3],[2,7,9]]
3.4) BA=[[-1,-5,-1],[2,7,4]]
3.5) BA^T="not defined"

```
import numpy as np

A=np.array([[1,2,3],[2,7,4]])
B=np.array([[1,-1],[0,1]])
C=np.array([[5,-1],[9,1],[6,0]])
D=np.array([[3,-2,-1],[1,2,3]])
u=np.array([6,2,-3,5])
v=np.array([3,5,-1,4])
w=np.array([[1],[8],[0],[5]])


e2_1=u+v
e2_2=u-v
e2_3=6*u
e2_4=np.dot(u,v)
e2_5=np.linalg.norm(u)

e3_1=A+C
e3_2=A-np.transpose(C)
e3_3=np.transpose(C)+3*D
e3_4=np.dot(B,A)
e3_5=np.dot(B,np.transpose(A))
```
