import json


def get_id_and_cursor_value(html):
    """
    获取id值和指向下一页的游标
    Parameters
    ----------
    html

    Returns
    -------

    """
    json_data = json.loads(html)
    # 获取游标值
    cursor = json_data["data"]["cursor"]
    has_more = json_data["data"]["has_more"]
    list_url = []
    # 获取该html中的6个帖子id值
    for note in json_data["data"]["notes"]:
        note_id = note["id"]
        url = "https://www.xiaohongshu.com/explore/%s" % note_id
        list_url.append(url)

    return list_url, cursor, has_more
