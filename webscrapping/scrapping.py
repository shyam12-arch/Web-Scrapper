# pip install beautifulsoup4
# pip install requests


from bs4 import BeautifulSoup
import requests
import pandas as pd
import pymysql as sql



url = "https://www.flipkart.com/search?q=camera&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY"
response = requests.get(url)

#print(response)  # response 200 means every thing is allright
#response 404 means not available
#response 500 means server down
#print(response.status_code)
#print(response.content)

htmlcontent = response.content
#soup = BeautifulSoup(htmlcontent)

#print(soup.prettify()) # looks like in a systematic way
soup = BeautifulSoup(htmlcontent,'html.parser')

#print(soup.prettify())  # now result come-out more systematically
#print(soup.title) ------> flipkart online shopping
#print(soup.title.name)  -----> gives title
#print(soup.title.parent.name) -----> link
#print(soup.p)
#print(soup.a)
#print(soup.find_all('a'))
#cls for close file
titles = []
prices = []
images = []
for d in soup.find_all('div',attrs={'class':'_2kHMtA'}):

    #print(d)
    title = d.find('div',attrs={'class':'_4rR01T'})
    #print(title)
    #titles.append(title.string)
    #print(title.string)

    price = d.find('div',attrs={'class':'_30jeq3 _1_WHN1'})
    #print(price.string)
    #prices.append(price.string)

    image = d.find('img',attrs={'class':'_396cs4 _3exPp9'})
    #images.append(image.get('src'))
    #print(image.get('src'))


    # database connectivity:
    con = sql.connect(host='localhost', user='root', passwd='Krish@4558$', database='manoj')
    cur = con.cursor() # create object help in query execution

    # data insertion:
    cur.execute("insert into aradhya values('%s','%s','%s')"%(title.string,price.string,image.get('src')))
    con.commit()  # for making parmanent change in table

#-------------------------------------------------------------
    # #create dictionary for convert above data into csv file format:
    # dictionary = {'title': titles,'price': prices,'image':images}
    # df = pd.DataFrame(dictionary)
    # df.to_csv('/Users/shyamtyagi/scrappings.csv')
#-------------------------------------------------------------







