
# coding: utf-8

# In[5]:


import requests
import csv
import bs4
from bs4 import BeautifulSoup


# In[6]:


listname = []
listscore = []
listprice = []
listaddr = []


# In[7]:


for i in range(1, 51):
    url = 'http://www.dianping.com/shenzhen/ch10/g110p%s' % i
    r = requests.get(url, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '  
                      '(KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'})
    r.encoding = 'utf8'
    mypage = BeautifulSoup(r.text)
    
    mytitle = mypage.find_all('div', attrs = {'class':'tit'})
    for title in mytitle:
        name = title.find('h4')
        listname.append(name.text)
        
    myrating = mypage.find_all('span', attrs = {'class':'comment-list'})
    for rating in myrating:
        score = rating.find('b')
        listscore.append(score.text)
        
    myprice = mypage.find_all('a', attrs = {'class':'mean-price'})
    for price in myprice:
        cost = price.find('b')
        if cost is not None:
            price_str = cost.text
            price = price = int(price_str[1:])//10*10
            print(price)
            listprice.append(price)
        else:
            listprice.append('无')
    
    mylocation = mypage.find_all('a', attrs = {'data-click-name':'shop_tag_region_click'})
    for location in mylocation:
        place = location.find('span')
        listaddr.append(place.text)

        
print(listname)
print(listscore)
print(listprice)
print(listaddr)


# In[8]:


with open('HW2_data.csv','w') as f:
    writer = csv.writer(f)
    header = ['name','rating','price/person','region']
    writer.writerow(header)
    writer.writerows(zip(listname,listscore,listprice,listaddr))

