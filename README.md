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
<img src="pics/1.png" width=200 height=280 />
---
### 根据codelist爬取所有地区的职位
- 爬取内容包含：signal、省、市、职位名称、薪资、公司名称、工作经验、学历要求、公司规模。
<img src="pics/3.png" width=300 height=40 />
- signal字段作用在于重复爬取时跳过已爬取的页面。
- 存入MongoDB中
<img src="pics/2.png" width=300 height=180 />

---
## 进行数据分析
### 读取数据
利用pandas读取数据库中数据
<img src="pics/4.png" width=360 height=190 />

---
### 添加新列：salary
利用正则提取出[职位薪资]
<img src="pics/5.png" width=360 height=190 />

---
### 数据清洗 
- 移除重复数据

<img src="pics/6.png" width=360 height=300 />

---

- 数据筛选过滤，去除过高和过低的薪资
<img src="pics/7.png" width=360 height=300 />
<img src="pics/9.png" width=360 height=300 />

- 去除与“数据分析”无关的岗位信息

---
## 数据可视化
<img src="pics/10.png" width=360 height=300 />

---

<img src="pics/11.png" width=360 height=300 />

---

<img src="pics/12.png" width=360 height=300 />

---

<img src="pics/14.png" width=360 height=300 />

---

<img src="pics/13.png" width=360 height=300 />

---

## 机器学习部分分析
<img src="pics/ML部分/过滤薪资.png" width=360 height=300 />

---

<img src="pics/ML部分/过滤后的分布.png" width=360 height=300 />

---

<img src="pics/ML部分/筛选岗位数量前150.png" width=300 height=200 />

---

<img src="pics/ML部分/属性合并.png" width=300 height=500 />

---

<img src="pics/ML部分/划分训练集与测试集.png" width=600 height=300 />

---

<img src="pics/ML部分/为标签编码.png" width=350 height=400 />

---
### **变量重要性**

<img src="pics/ML部分/变量重要性.png" width=350 height=400 />

---

<img src="pics/ML部分/重要性分析.png" width=500 height=150 />
