#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tweepy
import pandas as pd
import re


# In[2]:


consumer_key = "ho2tPaRaYSyQsFpA8tx82evZU"
consumer_secret = "EQkcU19GTKAZ66J3yCLmnGE1aUQNnEMEkUK5y1SXRObMePpSYB"
access_token = "1399618413262106624-fCJCuarQik1HX8eXGhMAy9pbCKTvdc"
access_token_secret = "TFaPhwkccwre3eAUUW3d7XIZ1S3seYcA1PKDxpqRdGVdi"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit = True)


# In[ ]:


df=[]
posts= tweepy.Cursor(api.search,q="washing machine",tweet_mode="extended").items(1000)
for i in posts:
    df.append([i.full_text,i.favorite_count,i.created_at])

df=pd.DataFrame(df,columns=['tweets','likes','time'])
df


# In[ ]:


import string
def clean_text(text):
    ''' , and '''
    text = text.lower()
    text = re.sub(r'\[.*?\]', '', text)
    text = re.sub(r'[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub(r'\w*\d\w*', '', text)
    return text
  
df = pd.DataFrame(df.tweets.apply(lambda x: clean_text(x)))
df


# In[ ]:


def getSubjectivity(text):
    return TextBlob(text).sentiment.subjectivity

def getPolarity(text):
    return TextBlob(text).sentiment.polarity

umn
df['Subjectivity'] = df['tweets'].apply (getSubjectivity)
df['Polarity'] = df['tweets'].apply(getPolarity)

df


# In[ ]:


allWords=' '.join( [twts for twts in df['tweets']] )
wordCloud = WordCloud(width = 500, height=300, random_state 21, max_font_size 119).generate (allWords)


plt.imshow(wordCloud, interpolation ="bilinear" )
plt.axis('off')
plt.show()


# In[ ]:


def getAnalysis(score):
    if score < 0:
        return 'negative'
    elif score==0:
        return 'neutral'
    else:
        return 'positive'

df['Analysis']= df['Polarity'].apply(getAnalysis)
df
    


# In[ ]:


j=1
sortedDF = df.sort_values(by=['Polarity'])

for i in range(0,sortedDF.shape[0]):
    
    if(sortedDF ['Analysis'][i] == 'Positive'):
        print (str(j) + ') '+ sortedDF['tweets'][i])
        print()
        j=j+1


# In[ ]:


k=1
sortedDF = df.sort_values(by=['Polarity'], ascending='False')

for a in range(0,sortedDF.shape[0]):
    
    if(sortedDF ['Analysis'][a] == 'Negative'):
        print (str(k) + ') '+ sortedDF['tweets'][a])
        print()
        k=k+1


# In[ ]:


plt.figure (figsize=(8,6))
for i in range(0, df.shape[0]):
    plt.scatter (df['Polarity'][i], df['Subjectivity'][i], color= 'Blue')

plt.title('Sentiment Analysis')
plt.xlabel ('Polarity')
plt.ylabel('Subjectivity')
plt.show()


# In[ ]:




