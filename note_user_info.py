import re


def get_note_info(note_string, note_dic={}):
    """
    提取帖子发布时间、标题、主体内容
    Parameters
    ----------
    note_string
    note_dic

    Returns
    -------
    note_dic
    """
    note_dic["note_time"] = re.findall(r'"time":(\d+)', note_string)[0]
    note_dic["note_title"] = re.findall('"title":"(.*?)"', note_string)[0]
    note_dic["note_desc"] = re.findall('"desc":"(.*?)"', note_string)[0]

    return note_dic


def get_user_info(user_string, user_dic):
    """
    提取帖子发布者
    Parameters
    ----------
    user_string
    user_dic

    Returns
    -------
    user_dic
    """
    user_dic["user_id"] = re.findall('"userId":"(.*?)"', user_string)[0]
    user_dic["nickname"] = re.findall('"nickname":"(.*?)"', user_string)[0]
    user_dic["ipLocation"] = re.findall('"ipLocation":"(.*?)"', user_string)[0]

    return user_dic
