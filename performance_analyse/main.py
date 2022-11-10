# yang shen 20009101459
# This is my performance analyse project.
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# read_file = pd.read_excel("excel_data/202210result.xlsx")
# read_file.to_csv("excel_data/202210result.csv", index=None, header=True)  #将原始excel数据转化为csv格式
result = pd.read_csv("excel_data/202210result.csv", encoding='utf-8')

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.style.use("ggplot")

result.rename(columns={'思想道德素质(M1)': 'M1', '专业理论素质(M2)': 'M2',
                       '创新创业精神与实践能力(M3)': 'M3', '文化素质(M4)': 'M4',
                       '劳动能力和身心素质(M5)': 'M5'}, inplace=True)
Ms_max = result.总成绩.max()
M1_max = result.M1.max()
M2_max = result.M2.max()
M3_max = result.M3.max()
M4_max = result.M4.max()
M5_max = result.M5.max()
M_max = [Ms_max, M1_max, M2_max, M3_max, M4_max, M5_max]
labels = np.array(['总成绩', 'M1', 'M2', 'M3', 'M4', 'M5'])

print('请输入您的学号：')
numberstr = input()
beststu = result.loc[0, labels].values
numberlist = list(numberstr)
number = 0
for i in range(len(numberlist)):
    number += int(numberlist[i]) * 10**(len(numberlist)-i-1)    #将学号转化为数字格式

namerow = result[result.学号.isin([number])]
row = namerow.index[0]
score = namerow.loc[row, labels].values
mean = result.loc[:, labels].mean()
mean = np.array(mean)
name = namerow.姓名.values[0]
myrank = result.loc[:, labels].rank(method='first', ascending=False).loc[row]   #求各项成绩排名

print('是否要显示您的各项成绩排名（y/n）：')
ord = input()
if ord == 'y':
    print(myrank)

#实现显示成绩蜘蛛图
angles = np.linspace(0, 2*np.pi, len(labels), endpoint=False)
angles0 = np.concatenate((angles, [angles[0]]))
score0 = np.concatenate((score, [score[0]]))
beststu0 = np.concatenate((beststu, [beststu[0]]))
M_max0 = np.concatenate((M_max, [M_max[0]]))
mean0 = np.concatenate((mean, [mean[0]]))
fig = plt.figure()
ax = fig.add_subplot(111, polar=True)
ax.plot(angles0, score0, 'o-', linewidth=2)
ax.plot(angles0, beststu0, 'o-', linewidth=2)
ax.plot(angles0, M_max0, 'o-', linewidth=2)
ax.plot(angles0, mean0, 'o-', linewidth=2)
ax.fill(angles0, score0, alpha=0.25)
ax.fill(angles0, beststu0, alpha=0.25)
ax.fill(angles0, M_max0, alpha=0.25)
ax.fill(angles0, mean0, alpha=0.25)
ax.set_thetagrids(angles * 180/np.pi, labels)
ax.set_title(name+' '+numberstr)
ax.grid(True)
plt.legend(['我的成绩', '总成绩最高', '各项最高', '平均成绩'])
print('是否要显示您的成绩蜘蛛图（y/n）：')
ord = input()
if ord == 'y':
    plt.show()

#实现分离各班级成绩排名
class11 = result[result['班级'] == 2001011]
class12 = result[result['班级'] == 2001012]
class13 = result[result['班级'] == 2001013]
class14 = result[result['班级'] == 2001014]
class15 = result[result['班级'] == 2001015]
class16 = result[result['班级'] == 2001016]
class17 = result[result['班级'] == 2001017]

# class11.to_csv('excel_data/class11.csv', index=False, encoding='utf-8')
# class12.to_csv('excel_data/class12.csv', index=False, encoding='utf-8')
# class13.to_csv('excel_data/class13.csv', index=False, encoding='utf-8')
# class14.to_csv('excel_data/class14.csv', index=False, encoding='utf-8')
# class15.to_csv('excel_data/class15.csv', index=False, encoding='utf-8')
# class16.to_csv('excel_data/class16.csv', index=False, encoding='utf-8')
# class17.to_csv('excel_data/class17.csv', index=False, encoding='utf-8')

#实现各班级总成绩和各模块成绩平均值的求值和柱状图显示
print('是否显示各班总成绩和各模块平均值柱状图（y/n）：')
ord = input()
classmean = result.groupby('班级').agg(np.mean)[labels]
classmean.plot(kind='bar')
plt.title('各班总成绩和各模块平均值')
if ord == 'y':
    plt.show()

#实现总成绩前100名各班级人数统计和饼状图显示
print('是否显示前100名各班人数占比饼状图（y/n）：')
ord = input()
head100 = result.head(100).groupby('班级').size()
plt.pie(head100.values[:], labels=head100.index, autopct='%.2f%%')
plt.title('前100名各班人数占比')
if ord == 'y':
    plt.show()

