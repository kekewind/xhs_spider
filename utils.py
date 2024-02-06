import time
import random


# 随机化休眠时间
def random_sleep():
    sleep_time = random.uniform(1, 2)  # 1到3秒之间的随机时间
    time.sleep(sleep_time)