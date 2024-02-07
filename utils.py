import time
import random


# 随机化休眠时间
def random_sleep():
    sleep_time = random.uniform(5, 6)
    time.sleep(sleep_time)