# version:1.0
# author:brandon
# date:2018/10/20

# common imports
import requests
import pymongo
# -------------


# 页面获取函数
def get():
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/69.0.3497.12 Safari/537.36 '
    }
    url = 'https://www.zhipin.com/common/data/city.json'
    response = requests.get(url, headers=header)
    return response.json()


def parse(data):
    cities = data['data']['cityList']
    for provence in cities:
        provence_name = provence['name']
        citylist = provence['subLevelModelList']
        for city in citylist:
            city_code = city['code']
            city_name = city['name']
            city_info = {
                '省': provence_name,
                '市': city_name,
                'code': city_code
            }
            print(city_info)
            save_to_mongo(city_info)


# 连接到MongoDB
MONGO_URL = 'localhost'
MONGO_DB = 'Graduation_project'
MONGO_COLLECTION = 'city'
client = pymongo.MongoClient(MONGO_URL, port=27017)
db = client[MONGO_DB]


def save_to_mongo(data):
    # 保存到MongoDB中
    try:
        if db[MONGO_COLLECTION].insert(data):
            print('存储到 MongoDB 成功')
    except Exception:
        print('存储到 MongoDB 失败')


if __name__ == '__main__':
    city = get()
    parse(city)
