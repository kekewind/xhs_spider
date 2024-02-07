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

    list_data = []
    # 获取该html中的6个帖子id值
    for note_id in json_data["data"]["notes"]:
        dic_data = {"note_id": note_id, "url": "https://www.xiaohongshu.com/explore/%s" % note_id }
        list_data.append(dic_data)

    return list_data, cursor
