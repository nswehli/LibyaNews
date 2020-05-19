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

    url = "http://alwasat.ly/section/libya"
    response = requests.get(url)
    soup = BS(response.text, 'html.parser')

    WasatSubheadlines = []
    WasatOtherNews = []

    headlines = soup.find(class_="war-right")
    Link = headlines.find("a")["href"]
    News = headlines.find(class_="h4-larg-font").text
    Image = headlines.find("img")["src"]

    WasatNewsHeadline = {"Headline": News, "Link": Link, "Image": Image}

    Subnews = soup.find_all(class_="section-page-news-with-img")
    for x in Subnews:
        subheadline = (x.find(class_="h4-small-font").text)
        subLink = (x("a")[0]["href"])
        subheadlines = {"Headline": subheadline, "Link": subLink}
        WasatSubheadlines.append(subheadlines)

    OtherNews = soup.find_all(class_="section-left-list")
    for x in OtherNews:
        OtherNews = (x.find(class_="h4-small-font-ext").text)
        Link = (x("a")[0]["href"])
        otherNews = {"Headline": OtherNews, "Link": Link}
        WasatOtherNews.append(otherNews)

    WasatNews = {"Headline": WasatNewsHeadline,
                 "Subheadlines": WasatSubheadlines,
                 "OtherNews": WasatOtherNews
                 }

    url = "https://libya24.tv/category/news"
    response = requests.get(url)
    soup24 = BS(response.text, 'html.parser')
    newsLib24 = soup24.find_all("figure")

    Libya24News = []

    for x in newsLib24:
        Headline = (x("a")[0]["title"])
        Link = (x("a")[0]["href"])
        Image: (x("a")[0]["style"].strip("background-image: url()'')"))
        News = {"Headline": Headline, "Link": Link, "Image": Image}
        Libya24News.append(News)

    # AlJazeera
    # Updated on May 19,2020 because Aljazeera changed its website design

    url = "https://www.aljazeera.net/where/libya/"
    response = requests.get(url)
    soup = BS(response.text, 'html.parser')
    # news=soup.find_all(class_="container--section-top-grid")
    print(response)

    headlines = soup.find_all(class_="generic-card__title")

    AlJazeeraNews = []

    for x in headlines[:10]:
        Headline = (x.get_text())
        Link = ("https://www.aljazeera.net"+x.find("a")["href"])
        news = {"Headline": Headline, "Link": Link}
        AlJazeeraNews.append(news)

        # Libya 218

        url = "https://www.218tv.net/category/سياسة/أخبار-ليبيا"
        response = requests.get(url)
        soup = BS(response.text, 'html.parser')
        Libya218News = []
        news = soup.find_all(class_="post-element")
        for x in news:
            Headline = (x.find(class_="featured-area")("a")[0]["aria-label"])
            Link = (x.find(class_="featured-area")("a")[0]["href"])
            Image = (x.find(class_="featured-area")("img")[0]["src"])
            MainHeadline = {"Headline": Headline, "Link": Link, "Image": Image}
            Libya218News.append(MainHeadline)

    # BBCArabic
    url = "https://www.bbc.com/arabic/topics/cnq681w1w42t"
    response = requests.get(url)
    soup = BS(response.text, 'html.parser')
    BBCArabic = []
    results = soup.find_all(
        class_="qa-heading-link lx-stream-post__header-link")
    for x in results:
        Headline = (x.text.strip())
        Link = ("https://www.bbc.com/"+x["href"])
        Headlines = {"Headline": Headline, "Link": Link}
        BBCArabic.append(Headlines)

    # Russia Today

    url = "https://arabic.rt.com/focuses/63564-%D9%84%D9%8A%D8%A8%D9%8A%D8%A7/"
    response = requests.get(url)
    response
    soup = BS(response.text, 'html.parser')
    RTArabic = []
    results = soup.find_all(class_="heading")
    for x in results:
        Headline = (x.text.strip())
        Link = ("https://arabic.rt.com"+x["href"])
        Headlines = {"Headline": Headline, "Link": Link}
        RTArabic.append(Headlines)

    url = "https://www.arraedlg.net/"
    response = requests.get(url)
    response
    AlRaed = []
    soup = BS(response.text, 'html.parser')
    results = soup.find_all("h2", class_="post-box-title")
    for x in results:
        Headline = (x.text.strip())
        Link = (x("a")[0]["href"])
        Headlines = {"Headline": Headline, "Link": Link}
        AlRaed.append(Headlines)

        # AlAhrar
    url = "https://www.libyaalahrar.tv/local/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',

    }
    LibyaAhrar = []
    response = requests.get(url, headers=headers)
    soup = BS(response.text, 'html.parser')
    results = soup.find_all(class_="thumb-title")
    for x in results:
        Headline = (x.text)
        Link = (x("a")[0]["href"])
        Headlines = {"Headline": Headline, "Link": Link}
        LibyaAhrar.append(Headlines)

        # AlMarsad
    url = "https://almarsad.co/category/%d9%85%d8%ad%d9%84%d9%8a/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',

    }
    AlMarsad = []
    response = requests.get(url, headers=headers)
    soup = BS(response.text, 'html.parser')
    results = soup.find_all(class_="cb-post-title")
    for news in results[:10]:
        Headline = (news.text.strip())
        Link = (news("a")[0]["href"])
        Headlines = {"Headline": Headline, "Link": Link}
        AlMarsad.append(Headlines)

        # France24
    url = "https://www.france24.com/ar/tag/%D9%84%D9%8A%D8%A8%D9%8A%D8%A7/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
    }
    France24 = []
    response = requests.get(url, headers=headers)
    soup = BS(response.text, 'html.parser')
    results = soup.find_all(class_="m-item-list-article")
    print(response)
    for news in results[:10]:
        Headline = (news.find(class_="article__title").text.strip())
        Link = ("https://www.france24.com/"+news("a")[0]["href"])
        Headlines = {"Headline": Headline, "Link": Link}
        France24.append(Headlines)

        # AlHadeth
    url = "https://libyaalhadath.net/?cat=5"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
    }
    AlHadeth = []
    response = requests.get(url, headers=headers)
    soup = BS(response.text, 'html.parser')

    results = soup.find_all(class_="post-item-inner")
    for x in results:
        Headline = (x("a")[0]["title"])
        Link = (x("a")[0]["href"])
        Headlines = {"Headline": Headline, "Link": Link}
        AlHadeth.append(Headlines)

    # BawabaAfrica

    url = "https://www.afrigatenews.net/section/%D9%84%D9%8A%D8%A8%D9%8A%D8%A7/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
    }
    BawabaAfrica = []
    response = requests.get(url, headers=headers)
    soup = BS(response.text, 'html.parser')

    results = soup.find(class_="section-content")
    news = results.find_all(class_="wt")
    for x in news:
        Headline = (x('a')[0].text)
        Link = ("https://www.afrigatenews.net/"+x('a')[0]["href"])
        Headlines = {"Headline": Headline, "Link": Link}
        BawabaAfrica.append(Headlines)

    Now = datetime.now(timezone.utc)

    data = {"AlwasatNews": WasatNews, "Libya24News": Libya24News, "AlJazeera": AlJazeeraNews, "Libya218": Libya218News, "BBCArabic": BBCArabic, "RussiaToday": RTArabic,
            "AlRaed": AlRaed, "LibyaAhrar": LibyaAhrar, "AlMarsad": AlMarsad, "France24": France24, "AlHadeth": AlHadeth, "BawabaAfrica": BawabaAfrica, "UpdateTime": Now}

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
