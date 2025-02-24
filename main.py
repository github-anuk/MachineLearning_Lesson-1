#LINEAR REGRESSION 

#m = sum((xi-mean(x)) * (yi-mean(y))) / sum((xi – mean(x))^2)
#c = mean(y) – m * mean(x)

x=[1,2,4,3,5]
y=[1,3,3,2,5]

def findMean(a):
    return sum(a)/len(a)

meanX = findMean(x)
meanY= findMean(y)

#calculating slope
#m = sum((xi-mean(x)) * (yi-mean(y))) / sum((xi – mean(x))^2)

num = 0
den = 0

for i in range(len(x)):
    num=num + ((x[i]-meanX) * (y[i]-meanY))
    den = den+pow((x[i]-meanX),2)

m=num/den
print("m = ", m )

#calculating y-intercept(c-value)
#c = mean(y)-m*mean(x)

c=round(meanY - m*meanX,1)
print("c =",c)

#using ml algorithm
import numpy as np
from sklearn.linear_model import LinearRegression

X=np.array([[1],[2],[4],[3],[5]])
y=np.array([[1],[3],[3],[2],[5]])

reg = LinearRegression().fit(X,y)
print("m=",reg.coef_)
print("c=",reg.intercept_)