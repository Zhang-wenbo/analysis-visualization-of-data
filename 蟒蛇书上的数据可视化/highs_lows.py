import csv

from matplotlib import pyplot as plt
from datetime import datetime

#从文件中获取日期信息和最高气温和最低气温
filename = "death_valley_2014.csv"#一般而言，都要将文件名存储到filename中

"""
reader处理文件中以逗号分隔的第一行数据，并将每项数据都作为一个元素存储在列表中。
 文件头AKDT表示阿拉斯加时间(Alaska Daylight Time)，其位置表明每行的第一个值都是日期或 时间。
 文件头Max TemperatureF指出每行的第二个值都是当天的最高华氏温度。
"""
with open(filename) as f:
    reader = csv.reader(f)#调用csv.reader()方法，创建一个与该文件相关的阅读器(read)对象，并存储到reader中
    header_row = next(reader)#调用它会返回文件的下一行，因为只调用了next()一次，因此得到的是文件的第一行，其中包含文件头

    dates,highs,lows = [],[],[]
    for row in reader:#遍历每行
        try:
            current_date = datetime.strptime(row[0],"%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date,'missing date')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)


#根据数据绘制图形
fig = plt.figure(dpi=128,figsize=(10,6))#分辨率及尺寸

plt.plot(dates,highs,c="red",alpha=0.5)#使用plt.plot()函数绘制折线图
plt.plot(dates,lows,c="blue",alpha=0.5)#alpha设置透明度
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)#传如x值和两个y值

#设置图形的格式
plt.title("Daily high and lower temperatures - 2014\nDeath Valley,CA",fontsize=20)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()#fig.autofmt_xdate()来绘制 斜的日期标签，以免它们彼此重叠
plt.ylabel("Temperature (F)",fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)#设置刻度标签
plt.yticks(range(0, 120, 10))#传入纵坐标刻度

plt.show()