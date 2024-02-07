import requests
from utils import *


def get_headers():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
        "Cookie": "a1=18986bdd105s5belewtqoqfddh2px6uca9dkwsvra50000738242; webId=72ee0f034d1675b848a049daabbd654f; gid=yYjYKDfS2f0KyYjYKDffyjMh82M2Dd1dE9AlfF0AiffxJT28UCK7SE888WqYJ4J8jq22ijW8; abRequestId=72ee0f034d1675b848a049daabbd654f; web_session=040069b46d6de75b74f183eb89374ba296c4c2; webBuild=4.1.6; cache_feeds=[]; unread={%22ub%22:%2265be6269000000002c034ade%22%2C%22ue%22:%2265c24fe70000000011001889%22%2C%22uc%22:16}; websectiga=f3d8eaee8a8c63016320d94a1bd00562d516a5417bc43a032a80cbf70f07d5c0; xsecappid=sns-topic"
    }

    return headers


def get_html(url, headers, method="get"):
    if method == "get":
        html = requests.get(url, headers=headers).content.decode("utf-8")
    else:
        html = requests.post(url, headers=headers).content.decode("utf-8")
    return html
