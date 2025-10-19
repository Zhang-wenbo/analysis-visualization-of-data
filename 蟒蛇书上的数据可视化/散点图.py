import matplotlib.pyplot as plt

x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]#列表推导式，生成1-1000的平方
plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Reds,edgecolor='none',s=40)#画点函数,s是点的大小,设置edgecolor为none表示无轮廓
#设置图表标题并给坐标轴加上标签
plt.title("Square Numbers",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)

#设置每个坐标轴的取值范围
plt.axis([0,1100,0,1100000])#四个参数，x和y坐标的最大值和最小值

plt.savefig('squares_plot.png',bbox_inches='tight')
#第一个为文件名，第二个为保存的区域，bbox_inches='tight'表示裁剪掉空白区域，默认路径在该程序所在目录