# version:1.0
# author:brandon
# date:2018/10/20

# common imports
import requests
import re
from lxml import etree
import time
import random
import pymongo
import pandas as pd
# -------------
# 导入模块
import city


# 页面获取函数
def get_page(page, city_code):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/69.0.3497.12 Safari/537.36 '
    }
    print('正在爬取第', page, '页')
    url = 'https://www.zhipin.com/c{code}-p100511/?page={page}&ka=page-{page}'.format(code=city_code, page=page)
    response = requests.get(url, headers=header)
    return response.text
# --------------


# 页面解析函数
def parse(html, city, provence, page):
    # data = json.loads(data)
    # print(data)
    # 观察数据结构可得
    data = etree.HTML(html)
    # 取工资均值
    items = data.xpath('//*[@id="main"]/div/div[2]/ul/li')
    for item in items:
        job_title = item.xpath('./div/div[1]/h3/a/div[1]/text()')[0]
        job_salary = item.xpath('./div/div[1]/h3/a/span/text()')[0]
        job_company = item.xpath('./div/div[2]/div/h3/a/text()')[0]
        job_experience = item.xpath('./div/div[1]/p/text()[2]')[0]
        job_degree = item.xpath('./div/div[1]/p/text()[3]')[0]
        company_scale = item.xpath('./div/div[2]/div/p/text()[3]')[0]
        # 取薪资均值----------------
        avg_salary = average(job_salary)
        # -------------------------
        signal = city + str(page)
        print(provence, '|', city, '|', job_title, '|', job_salary, '|', job_company, '|', job_experience, '|', job_degree, '|', company_scale,
              '|', avg_salary)
        job = {
            'signal': signal,
            '省': provence,
            '城市': city,
            '职位名称': job_title,
            '职位薪资': job_salary,
            '公司名称': job_company,
            '工作经验': job_experience,
            '学历要求': job_degree,
            '公司规模': company_scale
        }
        save_to_mongo(job)
# ---------------------------------------


# 均值函数
def average(job_salary):
    # 取薪资均值----------------
    pattern = re.compile('\d+')
    salary = job_salary
    try:
        res = re.findall(pattern, salary)
        avg_salary = 0
        sum = 0
        for i in res:
            a = int(i)
            sum = sum + a
            avg_salary = sum / 2
    except Exception:
        avg_salary = 0
    # 函数返回值
    return avg_salary


# 连接到MongoDB
MONGO_URL = 'localhost'
MONGO_DB = 'Graduation_project'
MONGO_COLLECTION = 'jobs_info'
client = pymongo.MongoClient(MONGO_URL, port=27017)
db = client[MONGO_DB]


# 检查是否已爬过
check = pd.DataFrame(list(db[MONGO_COLLECTION].find()))
check_list = check[['signal']]
grouped = check_list.groupby(check['signal'])
# -----------------


def save_to_mongo(data):
    # 保存到MongoDB中
    try:
        if db[MONGO_COLLECTION].insert(data):
            print('存储到 MongoDB 成功')
    except Exception:
        print('存储到 MongoDB 失败')


def jobspider(city_code, city, provence):
    # 最大爬取页数
    MAX_PAGE = 30
    for i in range(1, MAX_PAGE + 1):
        job_signal = city + str(i)
        # print(job_signal)
        if job_signal in grouped.size().index:
            continue
        else:
            try:
                html = get_page(i, city_code)
                # ------------ 解析数据 ---------------
                parse(html, city, provence, i)
                print('-' * 100)
                time.sleep(random.randint(0, 3))
            except Exception:
                break


if __name__ == '__main__':
    # 获取市ID
    citylist = city.city()
    for city in citylist:
        city_code = city[0]
        provence = city[1]
        city = city[2]
        # 职位爬虫
        jobspider(city_code, city, provence)
        # -----------------
