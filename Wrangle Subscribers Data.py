# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 00:42:45 2018

@author: Harsh Kava
"""

#Importing libraries
import pandas as pd
import numpy as np
import dateutil

#1: Load data directly from the provided URL instead of downloading and loading as csv (file size: ~ 180MB)
def getFileFromURL():
    try:
        import urllib.request
        urllib.request.urlretrieve("https://s3.amazonaws.com/orim-misc-data/assessment/subscribers.csv", "subscribers.csv")
    except Exception as e:
        print('Exception in getting file from url.')
        print('Exception is ::',e)
    
    
getFileFromURL()


try:
    df = pd.read_csv('subscribers.csv')
    #df = df[1:100]
except Exception as e:
    print('Exception in readind file from local disk.')
    print('Exception is ::',e)

#2: Count number of subscribers we acquired each year and month by referral source
df['Signup'] = df['Signup'].apply(dateutil.parser.parse, dayfirst=True)
df.groupby([df['Signup'].dt.year.rename('year'), df['Signup'].dt.month.rename('month')])['referral_source'].count()




#remove [] from the string

df['ebb_preferences'] = df['ebb_preferences'].str.replace('[','')
df['ebb_preferences'] = df['ebb_preferences'].str.replace(']','')
df['ebb_preferences'] = df['ebb_preferences'].str.replace('"','')


#creating set to identify all different types of genres
all_genre = set()
val = df['ebb_preferences'].unique()

for i in val:
    if str(i) != 'nan':
    #print(row['ebb_preferences'])
        x=i.split(',')
        #print(x)
        if(len(x) >0):
                for j in x:
                    j= j.replace('"','')
                    print(j)
                    if j not in all_genre:
                        all_genre.add(j) 

#creating new column called count_preferences
df['count_preferences'] = ''

#3: Create a new column counting number of preferences subscribers select. If the
#value of ebb_preference is empty, subscriber will receive all the genres that are
#available.

for index, row in df.iterrows():
       if not (pd.isnull(row['ebb_preferences'])):
           x = row['ebb_preferences'].split(',')
       else:
           x=all_genre
       df.at[index, 'count_preferences']=len(x) 
       #print(len(x))


#4: Convert ebb_preference column values into their own binary columns.
df = pd.concat([df, df['ebb_preferences'].str.get_dummies(',')], axis=1); df

# For checking if the downloaded data has specific values which appeared in results
#y = df.loc [ df ['c'] == 1 ];