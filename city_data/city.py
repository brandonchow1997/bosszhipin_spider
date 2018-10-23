# version:1.0
# author:brandon
# date:2018/10/20

# common imports
import pandas as pd


def city():
    city_data = pd.read_csv('city.csv')
    data = city_data[['code', '省', '市']]
    # print(data.values)
    city = data.values
    return city