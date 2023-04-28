from flask import render_template, Flask
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)
@app.route('/', methods=["GET", "POST"])
def index():
        
    url = 'https://www.businesstoday.in/technology/news'

    r0 = requests.get(url=url)

    soup = BeautifulSoup(r0.content, "html.parser")

    headlines = []
    headline_soup = soup.find_all('div', {"class": "widget-listing"}, limit=20)
    img_links = []

    desc = []

    for idx in headline_soup:
        headlines.append(idx.div.div.a['title'])
        desc.append(idx.find('p').text)
        img_links.append(idx.div.a.img['data-src'])

    datetime = []
    dt_soup = soup.find_all("div", {"class": "widget-listing-content-section"}, limit=20)
    hyperlinks = []

    for dt in dt_soup:
        res = dt.span.text.split(":")
        datetime.append(res[-1])
        hyperlinks.append(dt.h2.a['href'])
    
    data = {
        "headlines": headlines,
        "description": desc,
        "timestamp": datetime,
        "hyperlinks": hyperlinks,
        "image": img_links,
        "length": 20
    }

        
    return render_template("base.html", data=data)