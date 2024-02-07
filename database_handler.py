import pymongo


def init_database():
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client['graduateDesign']['xhs']
    return db


def save_to_database(db, data_list, cursor):
    try:
        db.insert_many(data_list)
        print("数据保存成功")
    except:
        print("数据保存失败")
        print("当前cursor:", cursor)
