
# coding: utf-8

# In[166]:


file=open("C:\\Users\\ajayr\\Desktop\\python\\trainingSet.txt","r")


# In[167]:


y=[]
x=[]
for line in file.readlines():
    lines=line.split(",")
    x.append(float(lines[0]))
    y.append(float(lines[1]))
print(x)
print(y)


# In[168]:


n=len(x)
print(n)


# In[169]:


print(sum(x))


# In[170]:


meanx=(sum(x))/n
print(meanx)


# In[171]:


meany=(sum(y))/n
print(meany)


# In[157]:


#Variance = sum((x - mean(x))^2)
def getVariance():
    variance=0
    for i in range(19):
        vari=((x[i]-meanx)**2)
        variance=vari+variance
    print(variance)


# In[173]:


#Covariance = sum((x(i) - mean(x)) * (y(i) - mean(y)))
def getCovariance():
    covariance=0
    for i in range(19):
        cova=(x[i]-meanx)*(y[i]-meany)
        covariance=cova+covariance
    print(covariance)


# In[175]:


#slope = covariance (X,Y)/variance(X)

slope=(covariance)/(variance)
print(slope)


# In[176]:


#intercept = mean(Y) - (slope*mean(X))
intercept=meany-(slope*meanx)
print(intercept)


# In[177]:


#Y = (slope*X) + intercept
def predict_Y():
    for i in range(19):
        y=(slope*x[i])+intercept
        print(y)


# In[179]:


x=1.25
y=(slope*x)+intercept
print(y)


# In[172]:


getVariance()


# In[174]:


getCovariance()


# In[178]:


predict_Y()

