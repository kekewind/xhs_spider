from database_handler import *
from id_list_cursor import *
from note_user_info import *
from webpage_scraper import *
from utils import *
import re


def get_and_write(url, db):

    data_dic = {"url": url}
    headers = get_headers()
    html = get_html(url, headers)
    random_sleep()

    note_string = re.findall('<script>window.__INITIAL_STATE__={(.*)}', html)[0]
    user_string = re.findall('"user":{.*?}', html)[1]
    data_dic.update(get_user_info(user_string))
    data_dic.update(get_note_info(note_string))

    save_to_database(db, data_dic, url)


