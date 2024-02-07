from database_handler import *
from multiprocessing.dummy import Pool
from webpage_scraper import *
from id_list_cursor import *
from join_function import *


if __name__ == "__main__":

    # 实例化数据库
    DB = init_database()
    now_page_url = "https://www.xiaohongshu.com/web_api/sns/v3/page/notes?page_size=6&sort=time&page_id=5be6c322568677000137198d&cursor=&sid="
    has_more = True

    # 计数（两个停止条件）
    count = 0
    stop_threshold = 21000

    # 请求头
    headers = get_headers()

    # 多线程池
    pool = Pool(3)

    while has_more or count < stop_threshold:
        html_string = get_html(now_page_url, headers)
        list_url, cursor, has_more = get_id_and_cursor_value(html_string)
        count += (len(list_url))
        pool.map(get_and_write, zip(list_url, DB))

        if has_more:
            now_page_url = "https://www.xiaohongshu.com/web_api/sns/v3/page/notes?page_size=6&sort=time&page_id=5be6c322568677000137198d&cursor=%s&sid=" % cursor
            print("当前cursor{}".format(cursor))
        else:
            pool.close()  # 关闭进程池，不再接受新的进程
            break
        if count % 200:
            print("已爬取{}条".format(count))
            print("**********************")

    print("Finish！")
    print("共爬取{}条".format(count))
