def get_html(url):
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.text
    except(requests.RequestException,ValueError):
        return False


def get_python_news():
   html = get_html("https://github.com/Ivanov-Ivan-Ivanich/telegram/branches")
   if html:
        soup = BeautifulSoup(html,'html.parser')
        all_news = soup.find('div', id = ' repo-content-pjax-container', class_='repository-content')
        respons = []
        for news in all_news:
            title = news.find('div',class_ = 'd-flex flex-lg-justify-between')
            url = news.find('div', class_='Box-header d-flex flex-items-center flex-justify-between')
            a = news.find('a',class_='d-block d-md-none position-absolute top-0 bottom-0 left-0 right-0')['href']
            respons.append({
                "title":title,
                "url":url,
                "a":a
            })
        return respons