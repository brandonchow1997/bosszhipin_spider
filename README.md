# BOSS直聘的数据分析
---
## 库依赖
- 基于Python3.6
- Jupyter Notebook
- pyecharts
- pymongo
- pandas
- numpy
---
## 爬虫实现过程
### 分析URL
![url](pics/url.png)
- c后的编号对应不同城市
- page后的数字则对应页码

---

### 爬取所有省、市对应的code
city.py实现地区与对应code的爬取
![效果图1](pics/1.png)

---
### 根据codelist爬取所有地区的职位
- 爬取内容包含：signal、省、市、职位名称、薪资、公司名称、工作经验、学历要求、公司规模。
![效果图3](pics/3.png)
- signal字段作用在于重复爬取时跳过已爬取的页面。
- 存入MongoDB中
![效果图2](pics/2.png)

---
## 进行数据分析
### 读取数据
利用pandas读取数据库中数据
![效果图4](pics/4.png)

---
### 添加新列：salary
利用正则提取出[职位薪资]
![效果图5](pics/5.png)

---
### 数据清洗 
- 移除重复数据

![效果图6](pics/6.png)

---

- 数据筛选过滤，去除过高和过低的薪资
![效果图7](pics/7.png)
![效果图9](pics/9.png)

- 去除与“数据分析”无关的岗位信息

---
## 数据可视化
![效果图10](pics/10.png)

---

![效果图11](pics/11.png)

---

![效果图12](pics/12.png)

---

![效果图14](pics/14.png)

---

![效果图13](pics/13.png)



---
