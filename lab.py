
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



def gitlab():
    htmlab = get_html("https://gitlab.com/Ivanov-Ivan-Ivanich/logi/-/commit/37d6ebd38f6e6eb9f350fcd86d032359fc7ae713#4f4721bd6f055e0b9ae1a31a41a2388dd98c4902")
    if htmlab:
        soup = BeautifulSoup(htmlab,'html.parser')
        all_news1 = soup.find('li',  id = "note_849139238",class_="timeline-entry note-wrapper note note-row-849139238 fade-in-full")
        
        respons1 = []
        
        for news1 in all_news1:
            title1 = soup.find('p').text
            respons1.append({
                "title1":title1
            })
        return respons1