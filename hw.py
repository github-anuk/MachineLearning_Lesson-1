import pandas as pd
import numpy as np

data = {
    "x": [0, 1, 2],
    "y": [30, 25, 35],
    
}

daaaf = pd.DataFrame(data)

daaaf.to_csv('data.csv', index=False)

data = pd.read_csv('data.csv')

X = data['x']
y = data['y']


def findMean(a):
    return sum(a)/len(a)

meanX = findMean(X)
meanY= findMean(y)

#calculating slope
#m = sum((xi-mean(x)) * (yi-mean(y))) / sum((xi – mean(x))^2)

num = 0
den = 0

for i in range(len(X)):
    num=num + ((X[i]-meanX) * (y[i]-meanY))
    den = den+pow((X[i]-meanX),2)

m=num/den
print("m = ", m )

#calculating y-intercept(c-value)
#c = mean(y)-m*mean(x)

c=round(meanY - m*meanX,1)
print("c =",c)


