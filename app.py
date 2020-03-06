import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from flask import Flask, render_template

app=Flask(__name__)

def gethtml(url):
        #opening up the connection and loading up the webpage
        uClient=uReq(url)
        page_html=uClient.read()
        uClient.close()
        return page_html

@app.route('/', methods=["GET" , "POST"])
def news():
        NEWS={ "World":[], "India":[], "Sports":[], "Business":[], "Tech":[]}

        myurl='https://timesofindia.indiatimes.com/world'         
        (page_html)=gethtml(myurl)

        #html parsing
        page_soup=soup(page_html,"html.parser")
        container = page_soup.find("div",{"id":"c_wdt_list_1"})
        cont=container.findAll('a')

        i=0
        #print("----------------------------------WORLD----------------------------")
        while(i<len(cont)):
                co=cont[i]
                W_news=co.getText()
                NEWS['World'].append(W_news)
                i=i+1

        myurl='https://timesofindia.indiatimes.com/india'
        (page_html)=gethtml(myurl)

        #html parsing
        page_soup=soup(page_html,"html.parser")
        container = page_soup.findAll("div",{"id":"c_wdt_list_1"})
        cont=container[1].findAll('a')
        i=0
        #print("----------------------------------iNDIA----------------------------")
        while(i<len(cont)):
                co=cont[i]
                I_news=co.getText()
                NEWS['India'].append(I_news)
                i=i+1

        myurl='https://timesofindia.indiatimes.com/sports'
        (page_html)=gethtml(myurl)
        #html parsing
        page_soup=soup(page_html,"html.parser")
        container = page_soup.find("div",{"class":"top-newslist small"})
        cont=container.findAll('a')
        i=0
        #print("----------------------------------SPORTS----------------------------")
        while(i<len(cont)):
                co=cont[i]
                S_news=co.getText()
                NEWS['Sports'].append(S_news)
                i=i+1

        myurl='https://timesofindia.indiatimes.com/business'
        (page_html)=gethtml(myurl)
        #html parsing
        page_soup=soup(page_html,"html.parser")
        container = page_soup.find("div",{"id":"c_wdt_list_2"})
        cont=container.findAll('a')
        i=0
        #print("----------------------------------BUISNESS----------------------------")
        while(i<len(cont)):
                co=cont[i]
                B_news=co.getText()
                NEWS['Business'].append(B_news)
                i=i+1

        myurl='https://indianexpress.com/section/technology/tech-news-technology/'
        (page_html)=gethtml(myurl)
        #html parsing
        page_soup=soup(page_html,"html.parser")
        container = page_soup.find("div",{"class":"nation"})
        cont=container.findAll('a')
        i=0
        #print("----------------------------------TECH----------------------------")     
        while(i<len(cont)):
                co=cont[i]
                T_news=co.getText()
                NEWS['Tech'].append(T_news)
                i=i+1
        

        return render_template("news1.html", news=NEWS)

if __name__ == '__main__':
        app.run(debug=True)
