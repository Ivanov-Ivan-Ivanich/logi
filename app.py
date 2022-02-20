from urllib import response
import requests
import os
from bs4 import BeautifulSoup
import json
def get_html(url):
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.text
    except(requests.RequestException,ValueError):
        return False


def get_python_news():
   html = get_html("https://github.com/Ivanov-Ivan-Ivanich/logi/blob/mergeLog/merge.log")
   if html:
        soup = BeautifulSoup(html,'html.parser')
        all_news = soup.find('table', class_="highlight tab-size js-file-line-container js-code-nav-container js-tagsearch-file")
        
        respons = []
        for news in all_news:
            title = soup.find('td',id="LC1",class_="blob-code blob-code-inner js-file-line").text
            respons.append({
                "title":title
            })
        return respons
    
