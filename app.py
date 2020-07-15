import os
from flask import Flask, render_template
from bs4 import BeautifulSoup as BS
import requests
import datetime
from datetime import date
from datetime import datetime
from datetime import timezone
import json

from flask_pymongo import PyMongo

today = date.today()
Now = datetime.now()
Retrieved = {"Retrieved on": Now}
print("Today's date:", today)

# Alwasat News
# create instance of Flask app
app = Flask(__name__)

MONGO_URL = os.environ.get('MONGO_URL')
if not MONGO_URL:
    MONGO_URL = "mongodb+srv://nswehli:900941196@lynews-7ygvg.mongodb.net/LyNews?retryWrites=true&w=majority"

mongo = PyMongo(
    app, uri=MONGO_URL)


# create route that renders index.html template


@app.route("/")
def Home():
    # Find one record of data from the mongo database

    news = mongo.db.News
    NewsData = news.find_one()
    sortedNews = news.find().sort("_id", -1).limit(1)

    for x in sortedNews:
        NewsData = x

    # Return template and data
    return render_template("index.html", Data=NewsData)


@app.route("/scrape")
def scrape():
    # Defining news dicts

    WasatNews = []
    Libya24News = []
    AlJazeeraNews = []
    Libya218News = []
    BBCArabic = []
    RTArabic = []
    AlRaed = []
    LibyaAhrar = []
    AlMarsad = []
    France24 = []
    Jamahrya = []
    LyPanoroma = []
    LyWatan = []
    Alsaaa24 = []
    EinLibya = []
    AlHadeth = []
    BawabaAfrica = []

    # In[20]:

    # AlWasat

    try:
        url = "http://alwasat.ly/section/libya"
        response = requests.get(url)
        soup = BS(response.text, 'html.parser')

        headlines = soup.find(class_="war-right")
        Link = headlines.find("a")["href"]
        News = headlines.find(class_="h4-larg-font").text

        WasatNewsHeadline = {"Headline": News, "Link": Link}
        WasatNews.append(WasatNewsHeadline)

        Subnews = soup.find_all(class_="section-page-news-with-img")
        for x in Subnews:
            subheadline = (x.find(class_="h4-small-font").text)
            subLink = (x("a")[0]["href"])
            subheadlines = {"Headline": subheadline, "Link": subLink}
            WasatNews.append(subheadlines)

        OtherNews = soup.find_all(class_="section-left-list")
        for x in OtherNews:
            OtherNews = (x.find(class_="h4-small-font-ext").text)
            Link = (x("a")[0]["href"])
            otherNews = {"Headline": OtherNews, "Link": Link}
            WasatNews.append(otherNews)

        WasatNews.append(Retrieved)

    except:
        print("Error with Alwasat")
    else:
        print("Successfully completed")

    # In[21]:
    # Libya24News
    try:
        url = "https://libya24.tv/category/news"
        response = requests.get(url)
        soup24 = BS(response.text, 'html.parser')
        newsLib24 = soup24.find_all("figure")
        for x in newsLib24:
            Headline = (x("a")[0]["title"])
            Link = (x("a")[0]["href"])
            News = {"Headline": Headline, "Link": Link}
            Libya24News.append(News)

        Libya24News.append(Retrieved)

    except:
        print("Error with Libya24News")
    else:
        print("Successfully completed")

    # In[22]:

    # AlJazeera

    # Updated on May 19,2020 because Aljazeera changed its website design

    try:
        url = "https://www.aljazeera.net/where/libya/"
        response = requests.get(url)
        soup = BS(response.text, 'html.parser')
        # news=soup.find_all(class_="container--section-top-grid")
        headlines = soup.find_all(class_="generic-card__title")
        for x in headlines[:10]:
            Headline = (x.get_text())
            Link = ("https://www.aljazeera.net"+x.find("a")["href"])
            news = {"Headline": Headline, "Link": Link}
            AlJazeeraNews.append(news)
        AlJazeeraNews.append(Retrieved)
    except:
        print("Error with Aljazeera")
    else:
        print("Successfully completed")

    # In[23]:

    # Libya 218
    try:
        url = "https://www.218tv.net/category/سياسة/أخبار-ليبيا"
        response = requests.get(url)
        soup = BS(response.text, 'html.parser')
        news = soup.find_all(class_="post-element")
        for x in news:
            Headline = (x.find(class_="featured-area")("a")[0]["aria-label"])
            Link = (x.find(class_="featured-area")("a")[0]["href"])
            MainHeadline = {"Headline": Headline, "Link": Link}
            Libya218News.append(MainHeadline)
        Libya218News.append(Retrieved)
    except:
        print("Error with Libya218News")
    else:
        print("Successfully completed")

    # In[24]:

    # BBCArabic
    try:
        url = "https://www.bbc.com/arabic/topics/cnq681w1w42t"
        response = requests.get(url)
        soup = BS(response.text, 'html.parser')
        results = soup.find_all(
            class_="qa-heading-link lx-stream-post__header-link")
        for x in results:
            Headline = (x.text.strip())
            Link = ("https://www.bbc.com/"+x["href"])
            Headlines = {"Headline": Headline, "Link": Link}
            BBCArabic.append(Headlines)
        BBCArabic.append(Retrieved)
    except:
        print("Error with BBCArabic")
    else:
        print("Successfully completed")

    # In[25]:

    # Russia Today

    try:
        url = "https://arabic.rt.com/focuses/63564-%D9%84%D9%8A%D8%A8%D9%8A%D8%A7/"
        response = requests.get(url)
        response
        soup = BS(response.text, 'html.parser')
        results = soup.find_all(class_="heading")
        for x in results:
            Headline = (x.text.strip())
            Link = ("https://arabic.rt.com"+x["href"])
            Headlines = {"Headline": Headline, "Link": Link}
            RTArabic.append(Headlines)
        RTArabic.append(Retrieved)
    except:
        print("Error with Russia Today")
    else:
        print("Successfully completed")

    # In[26]:

    try:
        url = "https://www.arraedlg.net/"
        response = requests.get(url)
        response
        soup = BS(response.text, 'html.parser')
        results = soup.find_all("h2", class_="post-box-title")
        for x in results:
            Headline = (x.text.strip())
            Link = (x("a")[0]["href"])
            Headlines = {"Headline": Headline, "Link": Link}
            AlRaed.append(Headlines)
        AlRaed.append(Retrieved)
    except:
        print("Error with AlRaed")
    else:
        print("Successfully completed")

    # In[27]:

    # AlAhrar
    try:
        url = "https://www.libyaalahrar.tv/local/"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
        }
        response = requests.get(url, headers=headers)
        soup = BS(response.text, 'html.parser')
        results = soup.find_all(class_="thumb-title")

        for x in results:
            Headline = (x.text)
            Link = f'https://libyaalahrar.tv/{(x("a")[0]["href"])}'
            Headlines = {"Headline": Headline, "Link": Link}
            LibyaAhrar.append(Headlines)

        LibyaAhrar.append(Retrieved)
    except:
        print("Error with AlAhrar")
    else:
        print("Successfully completed")

    # In[28]:

    # AlMarsad
    try:
        url = "https://almarsad.co/category/%d9%85%d8%ad%d9%84%d9%8a/"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',

        }
        response = requests.get(url, headers=headers)
        soup = BS(response.text, 'html.parser')
        results = soup.find_all(class_="cb-post-title")
        for news in results[:10]:
            Headline = (news.text.strip())
            Link = (news("a")[0]["href"])
            Headlines = {"Headline": Headline, "Link": Link}
            AlMarsad.append(Headlines)
        AlMarsad.append(Retrieved)
    except:
        print("Error with AlMarsad")
    else:
        print("Successfully completed")

    # In[29]:

    # France24
    try:

        url = "https://www.france24.com/ar/tag/%D9%84%D9%8A%D8%A8%D9%8A%D8%A7/"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
        }
        response = requests.get(url, headers=headers)
        soup = BS(response.text, 'html.parser')
        results = soup.find_all(class_="m-item-list-article")
        for news in results[:10]:
            Headline = (news.find(class_="article__title").text.strip())
            Link = ("https://www.france24.com/"+news("a")[0]["href"])
            Headlines = {"Headline": Headline, "Link": Link}
            France24.append(Headlines)
        France24.append(Retrieved)
    except:
        print("Error with France 24")
    else:
        print("Successfully completed")

    # In[30]:

    # AlHadeth

    try:
        url = "https://libyaalhadath.net/?cat=5"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
        }
        response = requests.get(url, headers=headers)
        soup = BS(response.text, 'html.parser')

        results = soup.find_all(class_="post-item-inner")
        for x in results:
            Headline = (x("a")[0]["title"])
            Link = (x("a")[0]["href"])
            Headlines = {"Headline": Headline, "Link": Link}
            AlHadeth.append(Headlines)
        AlHadeth.append(Retrieved)
    except:
        print("Error with AlHadeth")
    else:
        print("Successfully completed")

    # In[31]:

    # EinLibya
    try:
        url = "https://www.eanlibya.com/libya/"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
        }
        response = requests.get(url, headers=headers)
        soup = BS(response.text, 'html.parser')
        results = soup.find_all(class_="entry-title")

        for news in results[:10]:
            Headline = (news.find("a").text)
            Link = (news.find("a")["href"])
            Headlines = {"Headline": Headline, "Link": Link}
            EinLibya.append(Headlines)

        EinLibya.append(Retrieved)
    except:
        print("Error with Ein Libya")
    else:
        print("Successfully completed ")

    # In[32]:

    # alsaaa24
    try:
        url = "https://www.alsaaa24.com/libya/"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
        }
        response = requests.get(url, headers=headers)
        soup = BS(response.text, 'html.parser')
        results = soup.find_all(class_="post")

        for item in results[:10]:
            Headline = (item.find("a")["title"])
            Link = (item.find("a")["href"])
            Headlines = {"Headline": Headline, "Link": Link}
            Alsaaa24.append(Headlines)

        Alsaaa24.append(Retrieved)
    except:
        print("Error with Alsaaa 24")
    else:
        print("Successfully completed")

    # In[33]:
    # BawabaAfrica
    try:
        url = "https://www.afrigatenews.net/section/%D9%84%D9%8A%D8%A8%D9%8A%D8%A7/"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
        }
        response = requests.get(url, headers=headers)
        soup = BS(response.text, 'html.parser')

        results = soup.find(class_="section-content")
        news = results.find_all(class_="wt")
        for x in news:
            Headline = (x('a')[0].text)
            Link = ("https://www.afrigatenews.net/"+x('a')[0]["href"])
            Headlines = {"Headline": Headline, "Link": Link}
            BawabaAfrica.append(Headlines)
        BawabaAfrica.append(Retrieved)
    except:
        print("Error with Bawaba Africa")
    else:
        print("Successfully completed")

    # In[34]:
    # lIBYAaLWATAN
    try:
        url = "https://libyaschannel.com/category/libya/"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
        }
        response = requests.get(url, headers=headers)
        soup = BS(response.text, 'html.parser')
        results = soup.find_all(class_="xt-post-title")

        for item in results[:10]:
            Headline = (item.find("a")["title"])
            Link = (item.find("a")["href"])
            Headlines = {"Headline": Headline, "Link": Link}
            LyWatan.append(Headlines)

        LyWatan.append(Retrieved)
    except:
        print("Error with Libya Alwatan")

    else:
        print("Successfully completed")

    # In[35]:
    # lIBYAPanoroma
    try:

        url = "https://www.lpc.ly/category/news-2/"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
        }
        response = requests.get(url, headers=headers)
        soup = BS(response.text, 'html.parser')
        results = soup.find_all(class_="td-module-thumb")

        for item in results[:10]:
            Headline = (item.find("a")["title"])
            Link = (item.find("a")["href"])
            Headlines = {"Headline": Headline, "Link": Link}
            LyPanoroma.append(Headlines)

        LyPanoroma.append(Retrieved)
    except:
        print("Error with Libya Panoroma")
    else:
        print("Successfully completed")

    # In[36]:
    # Jamahrya
    try:
        url = "https://www.ljbctv.tv/libya"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
        }
        response = requests.get(url, headers=headers)
        soup = BS(response.text, 'html.parser')
        results = soup.find_all(class_="post-title")

        for item in results[:10]:
            Headline = (item.find("a").text)
            Link = (item.find("a")["href"])
            Headlines = {"Headline": Headline, "Link": Link}
            Jamahrya.append(Headlines)

        Jamahrya.append(Retrieved)
    except:
        print("Error with Jamahrya")
    else:
        print("Successfully completed")

    Now = datetime.now(timezone.utc)

    data = {"AlwasatNews": WasatNews, "Libya24News": Libya24News, "AlJazeera": AlJazeeraNews, "Libya218": Libya218News, "BBCArabic": BBCArabic, "RussiaToday": RTArabic,
            "AlRaed": AlRaed, "LibyaAhrar": LibyaAhrar, "AlMarsad": AlMarsad, "France24": France24, "AlHadeth": AlHadeth, "BawabaAfrica": BawabaAfrica, "EinLibya": EinLibya, "Alsaaa24": Alsaaa24, "LyWatan": LyWatan, "LyPanoroma": LyPanoroma, "Jamahrya": Jamahrya, "UpdateTime": Now}

    print(f"Data Scraping completed on {Now}")
    return render_template("index.html", Data=data)


@app.route("/api")
def api():
    news = mongo.db.News
    NewsData = []
    sortedNews = news.find()

    for item in sortedNews:
        NewsData.append(item)

    api = json.dumps(NewsData, indent=4, sort_keys=True,
                     default=str, ensure_ascii=False).encode('utf8')

    return api


if __name__ == "__main__":
    app.run(debug=True)
