import pandas as pd
import numpy as np
from nltk import *
import jieba
import random
import matplotlib.pyplot as plt
from wordcloud import WordCloud


#文本分词
with open (r'E:\数据分析\天龙八部.txt',encoding='utf-8') as f:
    data=f.read()
file_list = jieba.lcut(data)
#  删除停用词
tyc = open(r'E:\数据分析\中文停用词表.txt',encoding = 'utf-8')
stop = tyc.read()
file_data = []
for word in file_list:
    if word == '乔峰':
        file_data.append('萧峰')
    if word == '段公子':
        file_data.append('段誉')
    if word not in stop:
        file_data.append(word)       
#词频统计
num = FreqDist(file_data)
num_list = num.most_common()
#词云显示
font = "C:\Windows\Fonts\STXINGKA.TTF"
wc=WordCloud(font_path=font,background_color='white',width=2500,height=1200).generate(" ".join(file_data))
plt.imshow(wc)
plt.axis('off')
plt.show()


#角色分析
file_pe = []
for word in file_data:
    if word == '萧峰' or word == '段誉' or word == '虚竹' or word == '王语嫣' or word == '慕容复' or word == '段正淳' or word == '木婉清' or word == '鸠摩智' or word == '游坦之' or word == '丁春秋':
        file_pe.append(word)
#词频统计
num1 = FreqDist(file_pe)
num_list1 = num1.most_common()
#角色柱状图
x_data = list(num1.keys())
y_data = list(num1.values())
# 正确显示中文和负号
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False
# 画图，plt.bar()可以画柱状图
for i in range(len(x_data)):
	plt.bar(x_data[i], y_data[i])
# 设置图片名称
plt.title("主要人物")
# 设置x轴标签名
plt.xlabel("角色")
# 设置y轴标签名
plt.ylabel("出现次数")
# 显示
plt.show()


#门派分析
file_se = []
for word in file_data:
    if word == '天龙' or word == '少林' or word == '天山' or word == '逍遥派' or word == '星宿' or word == '丐帮' or word == '一品堂'  or word == '姑苏'  or word == '灵鹫':
        file_se.append(word)
#词频统计
num2 = FreqDist(file_se)
num_list2 = num2.most_common()

x_data = list(num2.keys())
y_data = list(num2.values())
for i in range(len(x_data)):
	plt.bar(x_data[i], y_data[i])
plt.title("主要势力")
plt.xlabel("门派")
plt.ylabel("出现次数")
plt.show()


#国家分析
file_wg = []
for word in file_data:
    if word == '大宋' or word == '契丹' or word == '大理' or word == '西夏' or word == '吐蕃' :
        file_wg.append(word)
#词频统计
num3 = FreqDist(file_wg)
num_list3 = num3.most_common()
#饼图
x_data = list(num3.keys())
y_data = list(num3.values())
plt.title('势力图')
plt.pie(list(num3.values()),labels=['大理','契丹','大宋','西夏','吐蕃'],autopct='%1.1f%%')
plt.show()