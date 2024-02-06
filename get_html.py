import requests


def get_html(url, headers, method="get"):
    if method == "get":
        html = requests.get(url, headers=headers).content.decode("utf-8")
    else:
        html = requests.post(url, headers=headers).content.decode("utf-8")
    return html
