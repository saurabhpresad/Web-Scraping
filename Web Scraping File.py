#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
import requests
import ast
from bs4 import BeautifulSoup
from time import sleep
from random import randint

actor_name = []
movie_name = []
movie_list = []


#Function to iterate through different pages of the site
pages = np.arange(1,11,1)
for page in pages:
    page = requests.get("https://www.imdb.com/list/ls058011111/?sort=list_order,asc&mode=detail&page="+str(page))
    soup = BeautifulSoup(page.text,'html.parser')
    actor_data = soup.findAll('div',attrs ={'class':'lister-item mode-detail'} )
    sleep(randint(2,8))
    for store in actor_data:
        name = store.h3.a.text
        name = name.rstrip("\n")
        actor_name.append(name)
    #print(actor_name)
        for store in actor_data:
            link_url = store.find_all("a")[1]["href"]
#     print(f"Apply here: {link_url}\n")
            a = str("https://www.imdb.com")+link_url+str("?ref_=nmls_kf")
            movie_name.append(a)
    #print(movie_name)
    
        data_combined = dict(zip(actor_name,movie_name))
        movie_data = str(data_combined)
        m_data = ast.literal_eval(movie_data)
#Function to iterate the keys of dictionary which gives the actor's page link as values and then use that link to find the movie names of that page.
def checkKey(dict, key):      
    if key in dict:
        movie_link = dict[key]
        n = str(movie_link)
        
        #Using the link of actor's page to access the movie names and print 
        movie_data_1 =requests.get(str(movie_link)) 
        soup1 = BeautifulSoup(movie_data_1.text,"html.parser")
        movie_data_1 = soup1.findAll('div',attrs={'class':['filmo-row odd','filmo-row even']})
        sleep(randint(2,8))
        for store_1 in movie_data_1:
            name_1 = store_1.b.a.text
            name_1 = name_1.rstrip("\n")
            movie_list.append(name_1)
        print(movie_list)

    else:
        print("Actor not present in the list")
        



# In[6]:


movie_list =[]
act_name = input("Enter your actor name : ").title()
act_name1= " "+act_name
checkKey(data_movies,act_name1)


# In[ ]:




